/* ===== PyLearn Playground =====
   A small IDE: multi-file editor, stdin box, run/stop, package imports.
   Code runs in py-worker.js (Web Worker), so Stop actually stops. */

const PG = {
  key: "pylearn_playground_v1",
  worker: null,
  running: false,
  editor: null,
  files: {},          // { "main.py": "print('hi')", ... }
  active: "main.py",
  booted: false,
};

const PG_DEFAULT = `# Playground - write any Python here, then press Run (Ctrl+Enter)

name = input("What's your name? ")   # type answers in the Input box below
print(f"Hello, {name}!")

total = sum(n * n for n in range(1, 11))
print("Sum of squares 1..10 =", total)
`;

const PG_EXAMPLES = {
  "Calculator": `import math\n\nradius = 3\nprint("area  =", round(math.pi * radius ** 2, 4))\nprint("2**64 =", 2 ** 64)\nprint("17/5  =", 17 / 5, "| floor:", 17 // 5, "| rest:", 17 % 5)\n`,
  "Read input": `# Put a few lines in the Input (stdin) box, then Run\nnumbers = []\nwhile True:\n    try:\n        line = input("number> ")\n    except EOFError:\n        break\n    numbers.append(float(line))\n\nprint("count:", len(numbers))\nprint("sum:  ", sum(numbers))\nif numbers:\n    print("mean: ", sum(numbers) / len(numbers))\n`,
  "Standard library": `import json, random, statistics\nfrom datetime import date\n\nrandom.seed(42)\nrolls = [random.randint(1, 6) for _ in range(20)]\nprint("rolls:", rolls)\nprint("mean:", statistics.mean(rolls), "mode:", statistics.mode(rolls))\nprint(json.dumps({"today": str(date.today()), "rolls": rolls})[:60], "...")\n`,
  "NumPy (auto-installs)": `import numpy as np\n\na = np.arange(1, 13).reshape(3, 4)\nprint(a)\nprint("column means:", a.mean(axis=0))\nprint("A @ A.T =\\n", a @ a.T)\n`,
  "Two files": `# main.py imports helper.py - add files with "+ File"\nfrom helper import shout\n\nprint(shout("modules work here too"))\n`,
};

// ---------- storage ----------
function pgLoad() {
  try {
    const saved = JSON.parse(localStorage.getItem(PG.key));
    if (saved && saved.files && Object.keys(saved.files).length) {
      PG.files = saved.files;
      PG.active = saved.files[saved.active] !== undefined ? saved.active : Object.keys(saved.files)[0];
      PG.stdin = saved.stdin || "";
      return;
    }
  } catch { /* fall through to defaults */ }
  PG.files = { "main.py": PG_DEFAULT };
  PG.active = "main.py";
  PG.stdin = "Mats";
}

function pgSave() {
  pgSyncEditor();
  const stdinEl = document.getElementById("pg-stdin");
  if (stdinEl) PG.stdin = stdinEl.value;
  try {
    localStorage.setItem(PG.key, JSON.stringify({ files: PG.files, active: PG.active, stdin: PG.stdin }));
  } catch (e) { console.warn("[playground] save failed:", e); }
}

function pgSyncEditor() {
  if (PG.editor) PG.files[PG.active] = PG.editor.getValue();
}

// ---------- worker ----------
function pgKillWorker() {
  if (PG.worker) { PG.worker.terminate(); PG.worker = null; }
  PG.booted = false;
}

function pgWorker() {
  if (PG.worker) return PG.worker;
  PG.worker = new Worker("py-worker.js");
  PG.worker.onmessage = (ev) => {
    const m = ev.data;
    if (m.type === "stdout" || m.type === "stderr") pgAppend(m.text, m.type);
    else if (m.type === "status") pgStatus(m.text);
    else if (m.type === "ready") PG.booted = true;
    else if (m.type === "fatal") { pgAppend(m.text + "\n", "stderr"); pgFinish(1, 0); }
    else if (m.type === "done") pgFinish(m.rc, m.ms);
  };
  PG.worker.onerror = (e) => {
    pgAppend("Worker error: " + (e.message || e.filename || "unknown") + "\n", "stderr");
    pgFinish(1, 0);
  };
  return PG.worker;
}

// ---------- output ----------
function pgOut() { return document.getElementById("pg-output"); }

function pgAppend(text, kind) {
  const out = pgOut();
  if (!out) return;
  if (out.dataset.empty === "1") { out.textContent = ""; out.dataset.empty = "0"; }
  const span = document.createElement("span");
  if (kind === "stderr") span.className = "pg-err";
  span.textContent = text;
  out.appendChild(span);
  out.scrollTop = out.scrollHeight;
}

function pgStatus(text) {
  const el = document.getElementById("pg-status");
  if (el) el.textContent = text || "";
}

function pgFinish(rc, ms) {
  PG.running = false;
  const btn = document.getElementById("pg-run");
  if (btn) { btn.disabled = false; btn.textContent = "▶ Run"; }
  const stop = document.getElementById("pg-stop");
  if (stop) stop.disabled = true;
  pgStatus(rc === 0 ? `finished in ${ms} ms` : `exited with errors (${ms} ms)`);
}

// ---------- actions ----------
function pgRun() {
  if (PG.running) return;
  pgSave();
  PG.running = true;
  const btn = document.getElementById("pg-run");
  btn.disabled = true; btn.textContent = "⏳ Running...";
  document.getElementById("pg-stop").disabled = false;
  const out = pgOut();
  out.textContent = ""; out.dataset.empty = "0";
  out.className = "output-body pg-output";
  pgStatus(PG.booted ? "running..." : "starting Python engine...");
  pgWorker().postMessage({
    type: "run",
    code: PG.files[PG.active],
    files: PG.files,
    stdin: PG.stdin || "",
  });
}

function pgStop() {
  if (!PG.running) return;
  pgKillWorker();
  pgAppend("\n^C stopped by user (Python engine will reload on next run)\n", "stderr");
  pgFinish(1, 0);
}

function pgNewFile() {
  let name = prompt("New file name:", "helper.py");
  if (!name) return;
  name = name.trim().replace(/[^\w.\-]/g, "_");
  if (!name.endsWith(".py")) name += ".py";
  if (PG.files[name] !== undefined) { pgSwitch(name); return; }
  pgSyncEditor();
  PG.files[name] = name === "helper.py"
    ? 'def shout(text):\n    return text.upper() + "!"\n'
    : `# ${name}\n`;
  PG.active = name;
  pgSave();
  renderPlayground(document.getElementById("app"));
}

function pgDeleteFile() {
  const name = PG.active;
  if (Object.keys(PG.files).length === 1) { alert("Keep at least one file."); return; }
  if (!confirm(`Delete ${name}?`)) return;
  delete PG.files[name];
  PG.active = Object.keys(PG.files)[0];
  pgSave();
  renderPlayground(document.getElementById("app"));
}

function pgSwitch(name) {
  if (name === PG.active) return;
  pgSyncEditor();
  PG.active = name;
  pgSave();
  renderPlayground(document.getElementById("app"));
}

function pgLoadExample(name) {
  if (!name) return;
  const code = PG_EXAMPLES[name];
  if (code === undefined) return;
  pgSyncEditor();
  PG.files[PG.active] = code;
  if (name === "Two files" && PG.files["helper.py"] === undefined) {
    PG.files["helper.py"] = 'def shout(text):\n    return text.upper() + "!"\n';
  }
  if (name === "Read input") PG.stdin = "3\n4.5\n10\n";
  pgSave();
  renderPlayground(document.getElementById("app"));
}

function pgDownload() {
  pgSave();
  const blob = new Blob([PG.files[PG.active]], { type: "text/x-python" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = PG.active;
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}

function pgUpload(input) {
  const file = input.files && input.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = () => {
    pgSyncEditor();
    const name = file.name.replace(/[^\w.\-]/g, "_");
    PG.files[name] = String(reader.result);
    PG.active = name;
    pgSave();
    renderPlayground(document.getElementById("app"));
  };
  reader.readAsText(file);
  input.value = "";
}

function pgReset() {
  if (!confirm("Reset the playground to the starter file? Your files here will be deleted.")) return;
  localStorage.removeItem(PG.key);
  pgLoad();
  renderPlayground(document.getElementById("app"));
}

// ---------- view ----------
function renderPlayground(app) {
  if (PG.editor) {                       // dispose previous instance on re-render
    try { PG.editor.toTextArea(); } catch { /* DOM already gone */ }
    PG.editor = null;
    if (typeof currentEditor !== "undefined") currentEditor = null;
  }
  if (!Object.keys(PG.files).length) pgLoad();

  const tabs = Object.keys(PG.files).map(n =>
    `<button class="pg-tab ${n === PG.active ? "active" : ""}" onclick="pgSwitch('${n}')">${escapeHtml(n)}</button>`
  ).join("");

  const examples = Object.keys(PG_EXAMPLES).map(n =>
    `<option value="${escapeHtml(n)}">${escapeHtml(n)}</option>`).join("");

  app.innerHTML = `
    <button class="back-btn" onclick="navigate('/dashboard')">← All Topics</button>

    <div class="exercise-header">
      <h2>🧪 Playground</h2>
      <div class="exercise-meta">
        <span class="diff-badge diff-1">Your own code</span>
      </div>
    </div>
    <div class="exercise-description">
      <p>A small Python IDE that runs entirely in your browser - nothing is uploaded. The standard library works out of the box, and <code>import numpy</code>-style imports are downloaded on demand the first time you use them.</p>
    </div>

    <div class="pg-toolbar">
      <div class="pg-tabs">${tabs}<button class="pg-tab pg-tab-add" onclick="pgNewFile()" title="New file">+ File</button></div>
      <div class="pg-tools">
        <select class="pg-select" onchange="pgLoadExample(this.value); this.value=''">
          <option value="">Examples…</option>${examples}
        </select>
        <button class="action-btn" onclick="pgDownload()" title="Download this file">⬇ Save</button>
        <label class="action-btn" title="Open a .py file">⬆ Open<input type="file" accept=".py,.txt" hidden onchange="pgUpload(this)"></label>
        <button class="action-btn" onclick="pgDeleteFile()" title="Delete this file">🗑</button>
        <button class="action-btn" onclick="pgReset()" title="Reset playground">🔄</button>
      </div>
    </div>

    <div class="editor-wrapper">
      <div class="editor-toolbar">
        <span>${escapeHtml(PG.active)}</span>
        <span class="pg-run-group">
          <button class="action-btn" id="pg-stop" onclick="pgStop()" disabled>■ Stop</button>
          <button class="run-btn" id="pg-run" onclick="pgRun()">▶ Run</button>
        </span>
      </div>
      <textarea id="pg-editor">${escapeHtml(PG.files[PG.active])}</textarea>
    </div>

    <div class="pg-io">
      <div class="pg-io-col">
        <div class="output-header">Input (stdin) — one <code>input()</code> answer per line</div>
        <textarea id="pg-stdin" class="pg-stdin" spellcheck="false" oninput="pgSave()">${escapeHtml(PG.stdin || "")}</textarea>
      </div>
      <div class="pg-io-col">
        <div class="output-header">Output <span id="pg-status" class="pg-status"></span></div>
        <pre id="pg-output" class="output-body idle pg-output" data-empty="1">Press ▶ Run (or Ctrl+Enter) to run ${escapeHtml(PG.active)}</pre>
      </div>
    </div>

    <p class="subtle" style="margin-top:12px">
      Ctrl+Enter runs · Stop kills a runaway loop · files are kept in this browser only.
    </p>
  `;

  const ta = document.getElementById("pg-editor");
  PG.editor = CodeMirror.fromTextArea(ta, {
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
      "Ctrl-Enter": pgRun,
      "Cmd-Enter": pgRun,
      Tab: (cm) => cm.replaceSelection("    "),
    },
  });
  PG.editor.on("blur", pgSave);
  currentEditor = PG.editor;   // so render() disposes it on navigation

  // Warm the engine up in the background so the first Run feels instant
  if (!PG.booted) pgWorker().postMessage({ type: "init" });
}

pgLoad();
