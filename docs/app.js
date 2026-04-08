/* ===== PyLearn App ===== */

const TOPIC_META = {
  variables:   { icon: "📦", color: "#3b82f6" },
  data_types:  { icon: "🔤", color: "#8b5cf6" },
  conditionals:{ icon: "🔀", color: "#f59e0b" },
  functions:   { icon: "⚙️", color: "#10b981" },
  lists_sets:  { icon: "📋", color: "#ef4444" },
  dictionaries:{ icon: "📖", color: "#ec4899" },
  fastapi_ex:  { icon: "🚀", color: "#06b6d4" },
  api_calling: { icon: "🌐", color: "#f97316" },
};

const DIFF_LABELS = ["", "Beginner", "Easy", "Medium", "Hard", "Challenge"];

let exerciseData = null;
let pyodideReady = false;
let pyodideLoading = false;
let pyodide = null;
let currentEditor = null;
let eli5Mode = localStorage.getItem("pylearn_eli5") !== "false"; // ON by default

// ELI5 explanations for each topic — super simple analogies
const ELI5_INTROS = {
  variables: "🧒 <b>Think of it like this:</b> A variable is like putting a sticker on a jar. The sticker is the name, and whatever's inside the jar is the value. When you write <code>age = 10</code>, you're putting the number 10 into a jar labeled 'age'. You can look inside the jar anytime, and you can swap what's inside!",
  data_types: "🧒 <b>Think of it like this:</b> Everything in Python has a type, just like in real life. A number like 5 is different from the word \"five\". A price like $3.50 is different from just 3. And \"yes\" or \"no\" answers are their own thing too. Python needs to know what type something is so it knows what you can do with it!",
  conditionals: "🧒 <b>Think of it like this:</b> Imagine you're at a fork in the road. If it's raining, you take the path with a roof. If it's sunny, you take the open path. That's what if/else does in code — it checks something and picks which path to follow!",
  functions: "🧒 <b>Think of it like this:</b> A function is like a recipe. You give it ingredients (inputs), it follows the steps, and gives you back a finished dish (output). Instead of writing the same cooking steps every time, you just say \"make pancakes\" and the recipe does the rest!",
  lists_sets: "🧒 <b>Think of it like this:</b> A list is like a train with numbered cars. Car #0 has one thing, car #1 has another. You can add cars, remove cars, or look at what's in any car. A set is like a bag of unique marbles — you can never have two of the same color!",
  dictionaries: "🧒 <b>Think of it like this:</b> A dictionary is like a real dictionary! But instead of words → definitions, you can have anything → anything. Like a phone book: you look up a person's name (the key) and get their phone number (the value). Super useful!",
  fastapi_ex: "🧒 <b>Think of it like this:</b> An API is like a waiter in a restaurant. You (the app) tell the waiter what you want, the waiter goes to the kitchen (the server), and brings back your food (the data). FastAPI helps you build that waiter!",
  api_calling: "🧒 <b>Think of it like this:</b> Calling an API is like ordering delivery through an app. You tell the app what you want (the request), it sends your order to the restaurant (the server), and food shows up at your door (the response). You're learning how to place those orders with code!",
};

function toggleEli5() {
  eli5Mode = !eli5Mode;
  localStorage.setItem("pylearn_eli5", eli5Mode);
  document.body.classList.toggle("eli5-mode", eli5Mode);
  document.getElementById("eli5-toggle").classList.toggle("active", eli5Mode);
  // Re-render if on a topic or exercise page
  const route = getRoute();
  if (route.view === "topic" || route.view === "exercise") render();
}

// Apply ELI5 on load
if (eli5Mode) document.body.classList.add("eli5-mode");

// ===== Progress (localStorage) =====
const progress = {
  _key: "pylearn_progress",
  _data: null,

  load() {
    try {
      this._data = JSON.parse(localStorage.getItem(this._key)) || {};
    } catch { this._data = {}; }
    if (!this._data.completed) this._data.completed = {};
    if (!this._data.streakDate) this._data.streakDate = "";
    if (!this._data.streak) this._data.streak = 0;
    if (!this._data.totalAttempts) this._data.totalAttempts = 0;
  },

  save() { localStorage.setItem(this._key, JSON.stringify(this._data)); },

  markCompleted(exerciseId) {
    this._data.completed[exerciseId] = true;
    this._data.totalAttempts++;
    const today = new Date().toISOString().slice(0, 10);
    if (this._data.streakDate === today) {
      // same day, no change
    } else {
      const yesterday = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
      this._data.streak = this._data.streakDate === yesterday ? this._data.streak + 1 : 1;
      this._data.streakDate = today;
    }
    this.save();
  },

  isCompleted(exerciseId) { return !!this._data.completed[exerciseId]; },

  countCompleted(topicId) {
    if (!exerciseData) return 0;
    const topic = exerciseData.topics.find(t => t.id === topicId);
    if (!topic) return 0;
    return topic.exercises.filter(e => this.isCompleted(e.id)).length;
  },

  totalCompleted() { return Object.keys(this._data.completed).length; },
  getStreak() { return this._data.streak || 0; },
};

progress.load();

// ===== Data Loading =====
async function loadExercises() {
  if (exerciseData) return exerciseData;
  const resp = await fetch("exercises.json");
  exerciseData = await resp.json();
  return exerciseData;
}

// ===== Pyodide =====
async function ensurePyodide() {
  if (pyodideReady) return pyodide;
  if (pyodideLoading) {
    while (!pyodideReady) await new Promise(r => setTimeout(r, 200));
    return pyodide;
  }
  pyodideLoading = true;
  document.getElementById("pyodide-loading").classList.remove("hidden");

  // Load Pyodide script
  await new Promise((resolve, reject) => {
    const s = document.createElement("script");
    s.src = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js";
    s.onload = resolve;
    s.onerror = reject;
    document.head.appendChild(s);
  });

  pyodide = await loadPyodide();

  // Install pydantic shim for FastAPI exercises
  await pyodide.runPythonAsync(`
class _FieldInfo:
    def __init__(self, **kw): self.__dict__.update(kw)

def Field(*a, **kw): return _FieldInfo(**kw)

class _ModelMeta(type):
    def __new__(mcs, name, bases, ns):
        cls = super().__new__(mcs, name, bases, ns)
        anns = {}
        for b in bases:
            anns.update(getattr(b, '__annotations__', {}))
        anns.update(ns.get('__annotations__', {}))
        cls.model_fields = {k: v for k, v in anns.items()}
        return cls

class BaseModel(metaclass=_ModelMeta):
    def __init__(self, **kw):
        anns = {}
        for cls in type(self).__mro__:
            anns.update(getattr(cls, '__annotations__', {}))
        for k in anns:
            if k in kw:
                setattr(self, k, kw[k])
            elif hasattr(type(self), k):
                setattr(self, k, getattr(type(self), k))
        for k, v in kw.items():
            if k not in anns:
                setattr(self, k, v)
    def model_dump(self, exclude=None):
        anns = {}
        for cls in type(self).__mro__:
            anns.update(getattr(cls, '__annotations__', {}))
        d = {k: getattr(self, k) for k in anns if hasattr(self, k)}
        if exclude:
            d = {k: v for k, v in d.items() if k not in exclude}
        return d
    def dict(self, **kw): return self.model_dump(**kw)

class EmailStr(str): pass

def field_validator(*a, **kw):
    def dec(f): return f
    return dec

import types
pydantic = types.ModuleType('pydantic')
pydantic.BaseModel = BaseModel
pydantic.Field = Field
pydantic.EmailStr = EmailStr
pydantic.field_validator = field_validator
import sys
sys.modules['pydantic'] = pydantic
  `);

  pyodideReady = true;
  document.getElementById("pyodide-loading").classList.add("hidden");
  return pyodide;
}

async function runPython(code, testCode) {
  const py = await ensurePyodide();
  let stdout = "";
  let error = null;
  let passed = false;

  py.setStdout({ batched: (msg) => { stdout += msg + "\n"; } });
  py.setStderr({ batched: (msg) => { stdout += msg + "\n"; } });

  try {
    // Run user code
    await py.runPythonAsync(code);

    // Run test code if provided
    if (testCode && testCode.trim() && !testCode.startsWith("pass")) {
      // Check for expected_output test
      if (testCode.includes("__expected_output__")) {
        const expectedMatch = testCode.match(/__expected_output__\s*=\s*['"](.*)['"]|__expected_output__\s*=\s*"""(.*)"""/s);
        if (expectedMatch) {
          const expected = (expectedMatch[1] || expectedMatch[2] || "").trim();
          const actual = stdout.trim();
          if (actual !== expected) {
            error = `Expected output:\n  ${expected}\nGot:\n  ${actual}`;
          } else {
            passed = true;
          }
        }
      } else {
        // Run assertion tests
        try {
          await py.runPythonAsync(testCode);
          passed = true;
        } catch (e) {
          const msg = e.message || String(e);
          // Extract just the assertion message
          const assertMatch = msg.match(/AssertionError: (.+)/s) || msg.match(/AssertionError:\s*(.+)/s);
          error = assertMatch ? assertMatch[1].trim() : msg.split("\n").pop().trim();
        }
      }
    } else {
      passed = true; // No tests = just run
    }
  } catch (e) {
    const msg = e.message || String(e);
    // Make error messages beginner-friendly
    error = friendlyError(msg);
  }

  // Clean up namespace for next run
  try {
    await py.runPythonAsync(`
import sys
_keep = set(sys.modules.keys())
for _k in list(globals().keys()):
    if _k.startswith('_') or _k in ('sys','pydantic','BaseModel','Field','EmailStr','field_validator','types'): continue
    try: del globals()[_k]
    except: pass
`);
  } catch {}

  return { stdout: stdout.trim(), error, passed };
}

function friendlyError(msg) {
  const lines = msg.split("\n");
  const last = lines[lines.length - 1] || msg;

  if (last.includes("NameError"))
    return last.replace(/.*NameError:\s*/, "NameError: ") +
      "\n\nThis means you used a variable or function name that hasn't been created yet. Check your spelling!";
  if (last.includes("SyntaxError"))
    return last.replace(/.*SyntaxError:\s*/, "SyntaxError: ") +
      "\n\nThis means Python can't understand your code. Check for missing colons, quotes, or parentheses.";
  if (last.includes("TypeError"))
    return last.replace(/.*TypeError:\s*/, "TypeError: ") +
      "\n\nThis means you're using the wrong type of data. For example, trying to add a number and text together.";
  if (last.includes("IndentationError"))
    return "IndentationError: Your code isn't lined up correctly.\n\nIn Python, spacing matters! Code inside if/for/def must be indented with spaces.";

  return last;
}

// ===== Router =====
function navigate(path) {
  window.location.hash = path;
}

function getRoute() {
  const hash = window.location.hash.slice(1) || "/";
  const parts = hash.split("/").filter(Boolean);
  if (parts.length === 0) return { view: "welcome" };
  if (parts[0] === "dashboard") return { view: "dashboard" };
  if (parts[0] === "topic" && parts[1]) return { view: "topic", topicId: parts[1], tab: parts[2] || "lesson" };
  if (parts[0] === "exercise" && parts[1]) return { view: "exercise", exerciseId: parts[1] };
  return { view: "welcome" };
}

// ===== Rendering =====
function render() {
  const route = getRoute();
  const app = document.getElementById("app");

  // Update badges
  document.getElementById("streak-badge").textContent =
    `🔥 ${progress.getStreak()}`;
  document.getElementById("progress-badge").textContent =
    `✓ ${progress.totalCompleted()}/${exerciseData ? exerciseData.total_exercises : "..."}`;

  // Destroy old editor
  if (currentEditor) { currentEditor.toTextArea(); currentEditor = null; }

  switch (route.view) {
    case "welcome": renderWelcome(app); break;
    case "dashboard": renderDashboard(app); break;
    case "topic": renderTopic(app, route.topicId, route.tab); break;
    case "exercise": renderExercise(app, route.exerciseId); break;
    default: renderWelcome(app);
  }

  app.classList.add("fade-in");
  setTimeout(() => app.classList.remove("fade-in"), 300);
  window.scrollTo(0, 0);
}

function renderWelcome(app) {
  app.innerHTML = `
    <div class="welcome-hero">
      <h1>🐍 Learn Python Interactively</h1>
      <p class="tagline">400 hands-on exercises. Zero setup. Runs in your browser.</p>
      <button class="start-btn" onclick="navigate('/dashboard')">Start Learning →</button>
    </div>

    <div class="welcome-section">
      <h2>👋 What is this?</h2>
      <p>PyLearn is a free, interactive app that teaches you Python programming from absolute zero. You don't need to install anything — everything runs right here in your browser, even on your phone!</p>
      <p>Whether you've never written a line of code or want to sharpen your skills, this app guides you step by step with clear explanations and instant feedback.</p>
    </div>

    <div class="welcome-section">
      <h2>🤔 What is Python?</h2>
      <p>Python is one of the most popular programming languages in the world. Think of it as a way to give instructions to your computer — like writing a recipe that a very literal robot chef will follow exactly.</p>
      <p>People use Python to build websites, analyze data, create AI, automate boring tasks, and much more. It's famous for being easy to read — it almost looks like English!</p>
      <div class="example-box">
        <span class="comment"># This is Python code. See? It's readable!</span><br>
        name = "World"<br>
        print(f"Hello, {name}!")<br>
        <div class="output">→ Hello, World!</div>
      </div>
    </div>

    <div class="welcome-section" style="background:linear-gradient(135deg,#fef9c3,#fef3c7);border:2px solid #f59e0b">
      <h2>🧒 "Explain Like I'm 5" Mode</h2>
      <p>See the <strong>🧒 ELI5</strong> button in the top-right corner? It's <strong>ON by default</strong>.</p>
      <p>When it's on, every topic and exercise gets extra-simple explanations using everyday analogies — like explaining variables as "labeled jars" or functions as "recipes". Perfect if you've never coded before!</p>
      <p>If you already know some programming, you can click it to turn it off and see just the standard descriptions.</p>
    </div>

    <div class="welcome-section">
      <h2>📖 How to use PyLearn</h2>
      <ul>
        <li><strong>Pick a topic</strong> — Start with "Variables" if you're brand new</li>
        <li><strong>Read the lesson</strong> — Each topic has a lesson explaining the concept in plain English</li>
        <li><strong>Try the examples</strong> — Run the code examples to see how they work</li>
        <li><strong>Do the exercises</strong> — Write code, click Run, get instant feedback</li>
        <li><strong>Use hints</strong> — Stuck? Each exercise has hints to guide you</li>
        <li><strong>Check the solution</strong> — Learn from the answer if you need to</li>
      </ul>
    </div>

    <div class="welcome-section">
      <h2>🎯 What you'll learn</h2>
      <ul>
        <li><strong>Variables</strong> — How to store and name data (like labeled boxes)</li>
        <li><strong>Data Types</strong> — Numbers, text, true/false, and how to work with them</li>
        <li><strong>Conditionals</strong> — Making decisions in code (if this, do that)</li>
        <li><strong>Functions</strong> — Reusable blocks of code (like recipes)</li>
        <li><strong>Lists & Sets</strong> — Collections of items (like shopping lists)</li>
        <li><strong>Dictionaries</strong> — Key-value lookups (like a phone book)</li>
        <li><strong>FastAPI</strong> — Building web APIs with Python</li>
        <li><strong>API Calling</strong> — Talking to other services from your code</li>
      </ul>
    </div>

    <div class="welcome-section">
      <h2>💻 Your first Python code</h2>
      <p>Here's what it looks like. Don't worry about understanding every detail yet — you'll learn all of this step by step!</p>
      <div class="example-box">
        <span class="comment"># Create a variable (a labeled box)</span><br>
        my_name = "Alex"<br><br>
        <span class="comment"># Use it in a message</span><br>
        print(f"Hi, I'm {my_name}!")<br><br>
        <span class="comment"># Do some math</span><br>
        age = 25<br>
        next_year = age + 1<br>
        print(f"I'm {age} now, and {next_year} next year")<br>
        <div class="output">→ Hi, I'm Alex!<br>→ I'm 25 now, and 26 next year</div>
      </div>
      <p style="margin-top:12px">Ready? Let's go! 👇</p>
      <button class="start-btn" onclick="navigate('/dashboard')" style="margin-top:12px">Start with Variables →</button>
    </div>
  `;
}

function renderDashboard(app) {
  const topics = exerciseData.topics;
  let cards = "";

  for (const topic of topics) {
    const meta = TOPIC_META[topic.id] || { icon: "📘", color: "#666" };
    const lesson = (window.PYLEARN_LESSONS || {})[topic.id];
    const subtitle = lesson?.subtitle || `${topic.exercise_count} exercises`;
    const completed = progress.countCompleted(topic.id);
    const pct = Math.round(completed / topic.exercise_count * 100);

    cards += `
      <div class="topic-card" onclick="navigate('/topic/${topic.id}')">
        <div class="icon">${meta.icon}</div>
        <div class="info">
          <h3>${topic.title}</h3>
          <p>${subtitle}</p>
          <div class="progress-bar"><div class="progress-fill" style="width:${pct}%"></div></div>
          <div class="progress-text">${completed}/${topic.exercise_count} completed</div>
        </div>
      </div>
    `;
  }

  app.innerHTML = `
    <div class="dashboard-header">
      <h1>Your Learning Path</h1>
      <p>Pick a topic to start learning. We recommend going in order!</p>
    </div>
    <div class="topic-grid">${cards}</div>
  `;
}

function renderTopic(app, topicId, activeTab) {
  const topic = exerciseData.topics.find(t => t.id === topicId);
  if (!topic) { navigate("/dashboard"); return; }

  const meta = TOPIC_META[topicId] || { icon: "📘" };
  const lesson = (window.PYLEARN_LESSONS || {})[topicId];

  let content = "";

  if (activeTab === "lesson") {
    // ELI5 intro box
    const eli5Intro = ELI5_INTROS[topicId] || "";
    const eli5Box = eli5Intro ? `<div class="eli5-box"><div class="eli5-label">🧒 Explain Like I'm 5</div>${eli5Intro}</div>` : "";

    if (lesson && lesson.sections) {
      let sectionsHtml = eli5Box;
      for (const sec of lesson.sections) {
        let examplesHtml = "";
        if (sec.examples) {
          for (const ex of sec.examples) {
            const outputHtml = ex.output ? `<span class="output-line">→ ${escapeHtml(ex.output)}</span>` : "";
            examplesHtml += `
              <div class="lesson-example">
                <div class="lesson-example-header">
                  <span>Example</span>
                  <button class="try-btn" onclick="tryExample(this, ${escapeAttr(JSON.stringify(ex.code))})">▶ Try it</button>
                </div>
                <pre>${escapeHtml(ex.code)}${outputHtml}</pre>
                ${ex.explanation ? `<div class="lesson-example-explain">${ex.explanation}</div>` : ""}
              </div>
            `;
          }
        }
        sectionsHtml += `
          <div class="lesson-section">
            <h3>${sec.title}</h3>
            ${sec.content}
            ${examplesHtml}
          </div>
        `;
      }

      // Tips
      let tipsHtml = "";
      if (lesson.tips && lesson.tips.length) {
        tipsHtml = `<div class="tips-box"><h3>💡 Pro Tips</h3>`;
        for (const tip of lesson.tips) {
          tipsHtml += `<div class="tip-item">${tip}</div>`;
        }
        tipsHtml += `</div>`;
      }

      // Mistakes
      let mistakesHtml = "";
      if (lesson.common_mistakes && lesson.common_mistakes.length) {
        mistakesHtml = `<div class="mistakes-box"><h3>⚠️ Common Mistakes</h3>`;
        for (const m of lesson.common_mistakes) {
          mistakesHtml += `
            <div class="mistake-item">
              <div class="wrong">❌ ${escapeHtml(m.mistake)}</div>
              <div class="right">✅ ${escapeHtml(m.fix)}</div>
              ${m.code ? `<div class="mistake-fix">${escapeHtml(m.code)}</div>` : ""}
            </div>
          `;
        }
        mistakesHtml += `</div>`;
      }

      content = `
        <div class="lesson-content">${sectionsHtml}</div>
        ${tipsHtml}
        ${mistakesHtml}
        <div style="text-align:center;margin-top:24px">
          <button class="start-btn" onclick="navigate('/topic/${topicId}/exercises')">Start Exercises →</button>
        </div>
      `;
    } else {
      content = `
        <div class="lesson-content">
          <div class="lesson-section">
            <h3>Lesson coming soon!</h3>
            <p>The detailed lesson for this topic is being prepared. In the meantime, jump into the exercises — each one includes helpful hints and descriptions.</p>
          </div>
        </div>
        <div style="text-align:center;margin-top:24px">
          <button class="start-btn" onclick="navigate('/topic/${topicId}/exercises')">Start Exercises →</button>
        </div>
      `;
    }
  } else {
    // Exercise list
    let items = "";
    topic.exercises.forEach((ex, i) => {
      const done = progress.isCompleted(ex.id);
      const dots = Array.from({length: 5}, (_, d) =>
        `<div class="diff-dot ${d < ex.difficulty ? 'active' : ''}"></div>`
      ).join("");

      items += `
        <div class="exercise-item ${done ? 'completed' : ''}" onclick="navigate('/exercise/${ex.id}')">
          <div class="exercise-num">${i + 1}</div>
          <div class="info">
            <h4>${ex.title}</h4>
            <div class="diff-dots">${dots}</div>
          </div>
          ${done ? '<span class="check-icon">✓</span>' : ''}
        </div>
      `;
    });
    content = `<div class="exercise-list">${items}</div>`;
  }

  app.innerHTML = `
    <button class="back-btn" onclick="navigate('/dashboard')">← All Topics</button>
    <div class="topic-header">
      <div class="icon">${meta.icon}</div>
      <div>
        <h1>${topic.title}</h1>
        <p>${progress.countCompleted(topicId)}/${topic.exercise_count} completed</p>
      </div>
    </div>
    <div class="tab-bar">
      <button class="tab ${activeTab === 'lesson' ? 'active' : ''}" onclick="navigate('/topic/${topicId}/lesson')">📖 Lesson</button>
      <button class="tab ${activeTab === 'exercises' ? 'active' : ''}" onclick="navigate('/topic/${topicId}/exercises')">✏️ Exercises</button>
    </div>
    ${content}
  `;
}

function renderExercise(app, exerciseId) {
  // Find exercise and its topic
  let exercise = null, topic = null, exIndex = -1;
  for (const t of exerciseData.topics) {
    const idx = t.exercises.findIndex(e => e.id === exerciseId);
    if (idx !== -1) {
      exercise = t.exercises[idx];
      topic = t;
      exIndex = idx;
      break;
    }
  }
  if (!exercise) { navigate("/dashboard"); return; }

  const meta = TOPIC_META[topic.id] || { icon: "📘" };
  const diffLabel = DIFF_LABELS[exercise.difficulty] || "Unknown";

  // Format description: convert `code` to <code>code</code>
  const desc = exercise.description.replace(/`([^`]+)`/g, "<code>$1</code>");

  // ELI5 explanation for exercises (difficulty 1-2 get extra hand-holding)
  let eli5ExHtml = "";
  if (exercise.difficulty <= 2) {
    const eli5Tip = ELI5_INTROS[topic.id] || "";
    if (eli5Tip) {
      eli5ExHtml = `<div class="eli5-box" style="margin-bottom:16px"><div class="eli5-label">🧒 Remember</div>${eli5Tip}</div>`;
    }
  }

  // Concepts
  let conceptsHtml = "";
  if (exercise.concepts && exercise.concepts.length) {
    conceptsHtml = `<div class="exercise-concepts">${exercise.concepts.map(c =>
      `<span class="concept-tag">${c}</span>`).join("")}</div>`;
  }

  // Starter code
  const starterCode = exercise.starter_code ||
    `# ${exercise.title}\n# ${exercise.description.slice(0, 80)}\n\n# Write your code below:\n`;

  // Navigation
  const prevEx = exIndex > 0 ? topic.exercises[exIndex - 1] : null;
  const nextEx = exIndex < topic.exercises.length - 1 ? topic.exercises[exIndex + 1] : null;

  app.innerHTML = `
    <button class="back-btn" onclick="navigate('/topic/${topic.id}/exercises')">← ${topic.title} Exercises</button>

    <div class="exercise-header">
      <h2>${meta.icon} #${exIndex + 1}: ${exercise.title}</h2>
      <div class="exercise-meta">
        <span class="diff-badge diff-${exercise.difficulty}">${diffLabel}</span>
        ${progress.isCompleted(exercise.id) ? '<span class="diff-badge diff-1">✓ Completed</span>' : ''}
      </div>
    </div>

    ${eli5ExHtml}
    <div class="exercise-description">
      <p>${desc}</p>
      ${conceptsHtml}
    </div>

    <div class="editor-wrapper">
      <div class="editor-toolbar">
        <span>solution.py</span>
        <button class="run-btn" id="run-btn" onclick="runExercise()">▶ Run & Check</button>
      </div>
      <textarea id="code-editor">${escapeHtml(starterCode)}</textarea>
    </div>

    <div class="output-panel">
      <div class="output-header">Output</div>
      <div class="output-body idle" id="output">Click "Run & Check" to test your code</div>
    </div>

    <div class="action-bar">
      <button class="action-btn" onclick="showHint()">💡 Hint <span id="hint-counter">(${exercise.hints.length} available)</span></button>
      <button class="action-btn" onclick="showSolution()">👀 Show Solution</button>
      <button class="action-btn" onclick="resetCode()">🔄 Reset</button>
    </div>

    <div id="hint-area"></div>
    <div id="solution-area"></div>

    <div class="exercise-nav">
      <button class="nav-btn" ${prevEx ? `onclick="navigate('/exercise/${prevEx.id}')"` : 'disabled'}>← Previous</button>
      <span style="color:var(--text-dim);font-size:0.85rem">${exIndex + 1} of ${topic.exercises.length}</span>
      <button class="nav-btn primary" ${nextEx ? `onclick="navigate('/exercise/${nextEx.id}')"` : 'disabled'}>Next →</button>
    </div>
  `;

  // Initialize CodeMirror
  const textarea = document.getElementById("code-editor");
  currentEditor = CodeMirror.fromTextArea(textarea, {
    mode: "python",
    theme: "dracula",
    lineNumbers: true,
    matchBrackets: true,
    autoCloseBrackets: true,
    indentUnit: 4,
    tabSize: 4,
    indentWithTabs: false,
    lineWrapping: true,
    extraKeys: {
      "Ctrl-Enter": runExercise,
      "Cmd-Enter": runExercise,
      Tab: (cm) => cm.replaceSelection("    "),
    },
  });

  // Store exercise data for use in handlers
  app._exercise = exercise;
  app._hintIndex = 0;
  app._starterCode = starterCode;
}

// ===== Exercise Handlers =====
async function runExercise() {
  const exercise = document.getElementById("app")._exercise;
  if (!exercise || !currentEditor) return;

  const btn = document.getElementById("run-btn");
  const output = document.getElementById("output");
  btn.disabled = true;
  btn.textContent = "⏳ Running...";
  output.className = "output-body idle";
  output.textContent = "Running your code...";

  const code = currentEditor.getValue();
  const result = await runPython(code, exercise.test_code);

  if (result.passed) {
    const wasAlreadyDone = progress.isCompleted(exercise.id);
    progress.markCompleted(exercise.id);

    output.className = "output-body pass";
    let text = "✅ All tests passed!";
    if (result.stdout) text = result.stdout + "\n\n" + text;
    output.textContent = text;

    // Update badges without re-rendering
    document.getElementById("streak-badge").textContent = `🔥 ${progress.getStreak()}`;
    document.getElementById("progress-badge").textContent = `✓ ${progress.totalCompleted()}/${exerciseData.total_exercises}`;
    const metaEl = document.querySelector(".exercise-meta");
    if (metaEl && !metaEl.innerHTML.includes("Completed")) {
      metaEl.innerHTML += ' <span class="diff-badge diff-1">✓ Completed</span>';
    }

    // Show celebration toast
    if (!wasAlreadyDone) {
      showCelebration(exercise);
    }
  } else {
    output.className = "output-body fail";
    let text = "❌ Not quite right.";
    if (result.error) text += "\n\n" + result.error;
    if (result.stdout) text = "Output:\n" + result.stdout + "\n\n" + text;
    output.textContent = text;

    // Shake the output panel for feedback
    output.parentElement.classList.add("shake");
    setTimeout(() => output.parentElement.classList.remove("shake"), 500);
  }

  btn.disabled = false;
  btn.textContent = "▶ Run & Check";
}

function showCelebration(exercise) {
  // Find next exercise
  let nextEx = null;
  for (const t of exerciseData.topics) {
    const idx = t.exercises.findIndex(e => e.id === exercise.id);
    if (idx !== -1 && idx < t.exercises.length - 1) {
      nextEx = t.exercises[idx + 1];
      break;
    }
  }

  // Celebration messages based on streak
  const total = progress.totalCompleted();
  const messages = [
    "Nice work! You got it! 🎉",
    "Awesome! Keep going! 💪",
    "Nailed it! You're learning fast! 🚀",
    "Perfect! Python is clicking! ⚡",
    "Brilliant! You're on fire! 🔥",
  ];
  const msg = messages[Math.min(Math.floor(total / 10), messages.length - 1)];

  // Milestone messages
  let milestone = "";
  if (total === 1) milestone = "🏆 First exercise completed!";
  else if (total === 10) milestone = "🏆 10 exercises done! You're getting the hang of it!";
  else if (total === 25) milestone = "🏆 25 down! Quarter of the way there!";
  else if (total === 50) milestone = "🏆 50 exercises! You're unstoppable!";
  else if (total === 100) milestone = "🏆 100! A true Python learner!";
  else if (total === 200) milestone = "🏆 200! Halfway through everything!";
  else if (total === 400) milestone = "🏆🏆🏆 ALL 400 COMPLETE! You're a Python hero!";
  else if (total % 50 === 0) milestone = `🏆 ${total} exercises completed!`;

  const nextBtn = nextEx
    ? `<button class="start-btn" onclick="this.closest('.celebration-toast').remove(); navigate('/exercise/${nextEx.id}')">Next Exercise →</button>`
    : `<button class="start-btn" onclick="this.closest('.celebration-toast').remove(); navigate('/dashboard')">Back to Topics →</button>`;

  const toast = document.createElement("div");
  toast.className = "celebration-toast";
  toast.innerHTML = `
    <div class="celebration-content">
      <div class="celebration-emoji">✅</div>
      <div class="celebration-msg">${msg}</div>
      ${milestone ? `<div class="celebration-milestone">${milestone}</div>` : ""}
      <div class="celebration-stats">
        Total completed: <strong>${total}/400</strong> &nbsp;|&nbsp; Streak: <strong>🔥 ${progress.getStreak()} day${progress.getStreak() !== 1 ? 's' : ''}</strong>
      </div>
      <div class="celebration-actions">
        ${nextBtn}
        <button class="action-btn" onclick="this.closest('.celebration-toast').remove()">Stay here</button>
      </div>
    </div>
  `;
  document.body.appendChild(toast);

  // Auto-dismiss after 15s
  setTimeout(() => { if (toast.parentNode) toast.remove(); }, 15000);
}

function showHint() {
  const exercise = document.getElementById("app")._exercise;
  const idx = document.getElementById("app")._hintIndex;
  const area = document.getElementById("hint-area");

  if (!exercise || idx >= exercise.hints.length) return;

  area.innerHTML += `<div class="hint-box">💡 Hint ${idx + 1}: ${exercise.hints[idx]}</div>`;
  document.getElementById("app")._hintIndex = idx + 1;

  const remaining = exercise.hints.length - idx - 1;
  document.getElementById("hint-counter").textContent =
    remaining > 0 ? `(${remaining} more)` : "(no more)";
}

function showSolution() {
  const exercise = document.getElementById("app")._exercise;
  if (!exercise || !exercise.solution) return;

  const area = document.getElementById("solution-area");
  if (area.innerHTML) { area.innerHTML = ""; return; }

  area.innerHTML = `
    <div class="solution-box">
      <div class="editor-toolbar">
        <span>✅ Solution</span>
        <button class="try-btn" onclick="loadSolution()">Load into editor</button>
      </div>
      <pre>${escapeHtml(exercise.solution)}</pre>
    </div>
  `;
}

function loadSolution() {
  const exercise = document.getElementById("app")._exercise;
  if (exercise && currentEditor) {
    currentEditor.setValue(exercise.solution);
  }
}

function resetCode() {
  const starterCode = document.getElementById("app")._starterCode;
  if (currentEditor && starterCode) {
    currentEditor.setValue(starterCode);
  }
  document.getElementById("output").className = "output-body idle";
  document.getElementById("output").textContent = 'Click "Run & Check" to test your code';
  document.getElementById("hint-area").innerHTML = "";
  document.getElementById("solution-area").innerHTML = "";
  document.getElementById("app")._hintIndex = 0;
  const exercise = document.getElementById("app")._exercise;
  if (exercise) {
    document.getElementById("hint-counter").textContent = `(${exercise.hints.length} available)`;
  }
}

async function tryExample(btn, code) {
  const py = await ensurePyodide();
  let output = "";
  py.setStdout({ batched: (msg) => { output += msg + "\n"; } });
  py.setStderr({ batched: (msg) => { output += msg + "\n"; } });

  try {
    await py.runPythonAsync(code);
    btn.textContent = output.trim() ? `→ ${output.trim()}` : "✓ Ran OK";
  } catch (e) {
    btn.textContent = "⚠️ Error";
  }
  setTimeout(() => { btn.textContent = "▶ Try it"; }, 4000);
}

// ===== Utilities =====
function escapeHtml(s) {
  const div = document.createElement("div");
  div.textContent = s;
  return div.innerHTML;
}

function escapeAttr(s) {
  return s.replace(/'/g, "\\'").replace(/"/g, "&quot;");
}

// ===== Init =====
window.addEventListener("hashchange", render);

(async function init() {
  await loadExercises();
  render();
})();
