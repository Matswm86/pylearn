/* ===== The AI Engineer Path =====
 * A five-phase study roadmap (Marina Wyss's method) with a per-topic video
 * sequence from the Visually Explained YouTube channel. Progress lives in
 * localStorage only (key: pylearn_path). Loaded after app.js, before tutor.js.
 */

const SCRIMBA_URL = "https://scrimba.com/learn-python-c03"; // verified 2026-09-03: "Learn Python for Free: Interactive Course"
const VE_CHANNEL_URL = "https://www.youtube.com/@VisuallyExplainedEducation";
const PATH_STORAGE_KEY = "pylearn_path";

// Single source of truth for every video used on the Path page and the
// per-topic Watch tabs. type: C = concept, P = practice problems, MP = mini-project.
const PATH_VIDEOS = {
  // Setup and numbers
  "5sgJsCah9bs": { title: "Google Colab for Python Beginners", type: "C", min: 8 },
  "r1vsfDMO-WE": { title: "Python Math Operators", type: "C", min: 3 },
  "_nNJ3EPtXKk": { title: "Google Colab and Math Operators", type: "P", min: 5 },
  "1lGXcaK6vqs": { title: "Python Integers vs Floats", type: "C", min: 5 },
  "jhCVoDCGLfE": { title: "Integers vs Floats", type: "P", min: 6 },
  // Strings and variables
  "vheAwWSyEC8": { title: "Python Strings", type: "C", min: 5 },
  "Z1D8Ngmwojk": { title: "Strings", type: "P", min: 6 },
  "KQQ10D0lits": { title: "Python Variables", type: "C", min: 6 },
  "ad7Po7WWhT0": { title: "Variables", type: "P", min: 5 },
  "H_TPIAEJl68": { title: "Python F-strings", type: "C", min: 7 },
  // Conditionals
  "3wkrYGmUqMk": { title: "Python Booleans and Conditionals", type: "C", min: 9 },
  "zz_d8ucpybM": { title: "Booleans and Conditionals", type: "P", min: 5 },
  "BmEYxeuHg58": { title: "Python Elif and Logical Expressions", type: "C", min: 15 },
  "6mpympBuBvg": { title: "Elif and Logical Expressions", type: "P", min: 7 },
  // Collections
  "spjE6cmV1Cs": { title: "Python Lists", type: "C", min: 9 },
  "P0BiDPiZQn0": { title: "Lists", type: "P", min: 6 },
  "11WrzU81q68": { title: "Python Lists vs Tuples vs Sets", type: "C", min: 6 },
  "F1cvQYQ2Qts": { title: "Lists vs Tuples vs Sets", type: "P", min: 7 },
  "4t10v2QmTHU": { title: "Python Dictionaries", type: "C", min: 10 },
  "3OovyajyELQ": { title: "Dictionaries", type: "P", min: 5 },
  // Loops
  "cAkKalfEPtg": { title: "Python For Loops", type: "C", min: 8 },
  "TobtUSykK64": { title: "For Loops", type: "P", min: 4 },
  "DUnY6l482Lk": { title: "List Comprehensions", type: "C", min: 9 },
  "je2hZUyq7IA": { title: "Nested Loops", type: "C", min: 7 },
  "u5V8j66lYcI": { title: "Python enumerate() Function", type: "C", min: 5 },
  "1cG6RpAH9Xk": { title: "Python zip() Function", type: "C", min: 6 },
  "4Q-_naaryTw": { title: "Enumerate() and Zip()", type: "MP", min: 5 },
  "x6L-QdezfaY": { title: "Python While Loops", type: "C", min: 10 },
  "MqMMFCFtnKU": { title: "While Loops", type: "P", min: 4 },
  // Input, errors, functions, modules
  "Gqv7S21CHD4": { title: "Python User Input", type: "C", min: 4 },
  "XN3udSTGAOM": { title: "Python Error Handling", type: "C", min: 5 },
  "pCzhxrs0CBk": { title: "User Input / Error Handling", type: "P", min: 5 },
  "KW6qncswzHw": { title: "Python Functions", type: "C", min: 14 },
  "hFIo05dSD0U": { title: "Functions: 3 Key Practice Problems", type: "P", min: 8 },
  "7MOzepKojbw": { title: "Intro to Python Libraries and Modules", type: "C", min: 17 },
  "_Eq31_ki3FE": { title: "Libraries and Modules", type: "P", min: 14 },
  // APIs and JSON
  "4rmBOxn0PdI": { title: "JSON in Python", type: "C", min: 14 },
  "BEPhyblKj8o": { title: "JSON in Python", type: "P", min: 6 },
  // Files
  "PXySDMxOPnI": { title: "Python File Handling", type: "C", min: 14 },
  "zaH0BBvzJ-0": { title: "File Handling", type: "P", min: 7 },
  "LffQVBq3P9o": { title: "Python Context Managers", type: "C", min: 14 },
  "1HHH6qpz9BE": { title: "Context Managers", type: "P", min: 7 },
  "IZ0tJVeKCKE": { title: "Python R-strings and Escape Sequences", type: "C", min: 5 },
  "sv8YTbeObHQ": { title: "Why Python Can't Find Your File (And How to Fix It)", type: "C", min: 11 },
  "PiO2dDvMiJo": { title: "CSV Files", type: "C", min: 3 },
  // Environments and modules
  "KZpYtNtGxSU": { title: "Python if __name__ == '__main__'", type: "C", min: 6 },
  // Read-real-code extras
  "FFpDsC6B2qw": { title: "Python *args vs **kwargs", type: "C", min: 11 },
  "ZA_zbYTNIRY": { title: "*args vs **kwargs", type: "P", min: 5 },
  "j6FCewxjrBM": { title: "Python Lambda Functions", type: "C", min: 8 },
  "3tyaO-OE0K0": { title: "Python Decorators", type: "C", min: 16 },
  "GWZf_B129zs": { title: "Python Generators", type: "C", min: 15 },
  "V_DzcyGTXW0": { title: "Regular Expressions (Regex)", type: "C", min: 11 },
  "AawczswiGI0": { title: "Regular Expressions (Regex)", type: "P", min: 5 },
  "jW3PChEAWWQ": { title: "Python Memoization", type: "C", min: 12 },
  "0qnmhFYTDas": { title: "Memoization", type: "P", min: 9 },
};

// Phase 1 step groups, in watch order. Each step: [videoId, pytorTopicId | null].
const PATH_GROUPS = [
  {
    id: "setup", title: "Setup and numbers",
    note: "The channel teaches in Google Colab; you work in a local virtual environment in a terminal instead. Watch the Colab video once for the vocabulary, then ignore it.",
    steps: [["5sgJsCah9bs", null], ["r1vsfDMO-WE", "data_types"], ["_nNJ3EPtXKk", "data_types"], ["1lGXcaK6vqs", "data_types"], ["jhCVoDCGLfE", "data_types"]],
  },
  {
    id: "strings", title: "Strings and variables",
    steps: [["vheAwWSyEC8", "data_types"], ["Z1D8Ngmwojk", "data_types"], ["KQQ10D0lits", "variables"], ["ad7Po7WWhT0", "variables"], ["H_TPIAEJl68", "variables"]],
  },
  {
    id: "conditionals", title: "Conditionals",
    steps: [["3wkrYGmUqMk", "conditionals"], ["zz_d8ucpybM", "conditionals"], ["BmEYxeuHg58", "conditionals"], ["6mpympBuBvg", "conditionals"]],
  },
  {
    id: "collections", title: "Collections",
    steps: [["spjE6cmV1Cs", "lists_sets"], ["P0BiDPiZQn0", "lists_sets"], ["11WrzU81q68", "lists_sets"], ["F1cvQYQ2Qts", "lists_sets"], ["4t10v2QmTHU", "dictionaries"], ["3OovyajyELQ", "dictionaries"]],
  },
  {
    id: "loops", title: "Loops",
    steps: [["cAkKalfEPtg", "loops"], ["TobtUSykK64", "loops"], ["DUnY6l482Lk", "loops"], ["je2hZUyq7IA", "loops"], ["u5V8j66lYcI", "loops"], ["1cG6RpAH9Xk", "loops"], ["4Q-_naaryTw", "loops"], ["x6L-QdezfaY", "loops"], ["MqMMFCFtnKU", "loops"]],
  },
  {
    id: "functions", title: "Input, errors, functions, modules",
    note: "Gap: the channel has no video on classes (just enough object-oriented Python to read it). Take that from Scrimba, or read one class in your own first project when you get there.",
    steps: [["Gqv7S21CHD4", null], ["XN3udSTGAOM", "api_calling"], ["pCzhxrs0CBk", "api_calling"], ["KW6qncswzHw", "functions"], ["hFIo05dSD0U", "functions"], ["7MOzepKojbw", null], ["_Eq31_ki3FE", null]],
  },
  {
    id: "apis", title: "APIs and JSON",
    note: "Gap: no requests / HTTP video and no environment-variable / API-key video on this channel. Both arrive with your first API project, which is where they belong.",
    steps: [["4rmBOxn0PdI", "api_calling"], ["BEPhyblKj8o", "api_calling"]],
  },
  {
    id: "files", title: "Files",
    note: "Watch \"Why Python Can't Find Your File\" before your first file exercise, not after your first FileNotFoundError.",
    steps: [["PXySDMxOPnI", null], ["zaH0BBvzJ-0", null], ["LffQVBq3P9o", null], ["1HHH6qpz9BE", null], ["IZ0tJVeKCKE", null], ["sv8YTbeObHQ", null], ["PiO2dDvMiJo", null]],
  },
  {
    id: "env", title: "Environments and modules",
    note: "Gap: no virtual-environment video. Create a venv by hand once more and explain to Pytor why it exists. NumPy and Pandas are not on this channel either: take them from Scrimba or from your first project's data. Do not go hunting for another channel; that is the study loop.",
    steps: [["KZpYtNtGxSU", null]],
  },
];

const PATH_EXTRAS = {
  id: "extras", title: "Read-real-code extras (watch when you meet them, not before)",
  note: "Not required for the exit gate. You will meet each of these the first day you read someone else's Python. Watch one the first time it blocks you.",
  steps: [["FFpDsC6B2qw", "functions"], ["ZA_zbYTNIRY", "functions"], ["j6FCewxjrBM", "functions"], ["3tyaO-OE0K0", "functions"], ["GWZf_B129zs", null], ["V_DzcyGTXW0", null], ["AawczswiGI0", null], ["jW3PChEAWWQ", null], ["0qnmhFYTDas", null]],
};

const PATH_GATES = [
  ["gate_1", "I can read unfamiliar code and explain what it does."],
  ["gate_2", "I can debug a failing test on my own."],
  ["gate_3", "I can reason about data flow and say where the system is likely to break."],
];

// Videos shown on each topic page's Watch tab.
const PATH_VIDEOS_BY_TOPIC = {
  variables: ["KQQ10D0lits", "ad7Po7WWhT0", "H_TPIAEJl68"],
  data_types: ["r1vsfDMO-WE", "_nNJ3EPtXKk", "1lGXcaK6vqs", "jhCVoDCGLfE", "vheAwWSyEC8", "Z1D8Ngmwojk", "IZ0tJVeKCKE"],
  conditionals: ["3wkrYGmUqMk", "zz_d8ucpybM", "BmEYxeuHg58", "6mpympBuBvg"],
  loops: ["cAkKalfEPtg", "TobtUSykK64", "x6L-QdezfaY", "MqMMFCFtnKU", "je2hZUyq7IA", "u5V8j66lYcI", "1cG6RpAH9Xk", "4Q-_naaryTw", "DUnY6l482Lk"],
  functions: ["KW6qncswzHw", "hFIo05dSD0U", "FFpDsC6B2qw", "ZA_zbYTNIRY", "j6FCewxjrBM", "3tyaO-OE0K0"],
  lists_sets: ["spjE6cmV1Cs", "P0BiDPiZQn0", "11WrzU81q68", "F1cvQYQ2Qts", "DUnY6l482Lk"],
  dictionaries: ["4t10v2QmTHU", "3OovyajyELQ", "4rmBOxn0PdI", "BEPhyblKj8o"],
  api_calling: ["4rmBOxn0PdI", "BEPhyblKj8o", "XN3udSTGAOM", "pCzhxrs0CBk"],
  fastapi_ex: ["KZpYtNtGxSU", "7MOzepKojbw", "_Eq31_ki3FE"],
};

// The other four phases: short, checkable summaries.
const PATH_PHASES = [
  {
    id: "p0", num: 0, title: "Math intuition", cap: "hard cap: 3 weeks",
    intro: "A rough mental map, not mastery. When week 3 ends, this phase ends, finished or not.",
    items: [
      ["p0_1", "3Blue1Brown, Essence of Linear Algebra (15 videos): know what a matrix does to a vector"],
      ["p0_2", "3Blue1Brown, Essence of Calculus: stop after the chain rule"],
      ["p0_3", "StatQuest: distributions, Bayes' theorem, p-values, confusion matrix"],
      ["p0_4", "3Blue1Brown, neural networks (4 videos)"],
    ],
  },
  {
    id: "p2", num: 2, title: "One escalating project", cap: "one project, four levels",
    intro: "A project of your own: your data, your problem, a real user. Not a tutorial follow-along, not a Kaggle notebook, not a to-do app nobody uses.",
    items: [
      ["p2_1", "L1: one LLM API call plus a simple interface, structured output, a fallback when the model fails"],
      ["p2_2", "L2: retrieval over your own data: chunking, embeddings, a vector store, an eval per component"],
      ["p2_3", "L3: an agent loop with read-only tools first; instrument it; grant write access only once the loop is reliable"],
      ["p2_4", "L4: specialist agents plus a checker agent; break it on purpose and write down what broke"],
    ],
  },
  {
    id: "p3", num: 3, title: "The five skills", cap: "what production teams actually pay for",
    intro: "Evals come first, not last. Most production AI work is level 2 or 3 done reliably.",
    items: [
      ["p3_1", "Evals: a written definition of \"good\" before the feature exists"],
      ["p3_2", "Context engineering: write, select, compress, isolate"],
      ["p3_3", "Production agents: retries, timeouts, malformed responses, graceful degradation"],
      ["p3_4", "LLMOps: deploy, monitor, latency, cost forecast, caching, provider-outage fallback"],
      [null, "Adaptability: a habit, not a checkbox"],
    ],
  },
  {
    id: "p4", num: 4, title: "Manufacture real experience", cap: "experience gets you hired, projects alone do not",
    intro: "You can create experience without being hired. Building for one real person is also how networking happens.",
    items: [
      ["p4_1", "Find one nonprofit or one real person with one real problem"],
      ["p4_2", "Ship a fix for free and measure what it saved them"],
      ["p4_3", "Put it on the CV as work experience, not as a portfolio project"],
      ["p4_4", "Ask that person for one introduction"],
    ],
  },
];

const PATH_TYPE_LABEL = { C: "Concept", P: "Practice", MP: "Mini-project" };

// Certification track. Facts from the official Microsoft study guides
// (skills measured, checked 2026-08-20); CertiAce pages read 2026-09-03.
const PATH_CERTS = {
  id: "certs",
  title: "Certification track: AI-901 → AI-103",
  cap: "runs alongside Phase 2; needs Phase 1 Python first",
  intro: "Certificates are a supplement, never the main signal. They get you past a screen; the project and the real experience get you the interview. Both exams below are live; AI-900, AI-102 and DP-100 retired in June 2026, so ignore any material that still names them. Per domain: read the official study guide's bullet list, do the Microsoft Learn module, then the CertiAce module with explanations on. The official Practice Assessment is the bar; a CertiAce mock is a signal.",
  exams: [
    {
      code: "AI-901", name: "Microsoft Azure AI Fundamentals",
      facts: "Passing score 700. No retirement date. Microsoft lists Python syntax and Azure familiarity as prerequisites, which is why this sits after Phase 1.",
      official: "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901",
      guide: "https://certiace.com/study-guides/ai-901",
      practice: "https://certiace.com/practice/AI-901",
      practiceNote: "249 questions; Modules, Randomizer, Practice Exam, AI Practice; free start, account for the full bank",
      domains: [
        ["c901_d1", "Identify AI concepts and capabilities", "40-45%"],
        ["c901_d2", "Implement AI solutions by using Microsoft Foundry", "55-60%"],
      ],
      gaps: null,
      steps: [
        ["c901_s1", "Read the official study guide once; note that over half the exam is hands-on Foundry"],
        ["c901_s2", "Microsoft Learn AI-901 learning path finished"],
        ["c901_s3", "CertiAce study guide read, both CertiAce modules done with explanations on"],
        ["c901_s4", "Official Practice Assessment (AI Skills Navigator) 800 or more, twice, one of them timed"],
        ["c901_s5", "Exam booked, on a personal Microsoft account (exam records are unrecoverable if you leave an organisation)"],
        ["c901_s6", "Passed"],
      ],
    },
    {
      code: "AI-103", name: "Azure AI Apps and Agents Developer Associate",
      facts: "The AI Engineer role certificate. Passing score 700, about 60 hours of study with labs. Domain 1 is a restatement of the five skills in Phase 3: model selection, retrieval, agent memory and tools, quotas and cost, monitoring for drift and grounding quality, keyless credentials. Studying for it is studying LLMOps.",
      official: "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103",
      guide: "https://certiace.com/study-guides/ai-103",
      practice: "https://certiace.com/practice/AI-103",
      practiceNote: "306 questions; Modules, Randomizer, Case Studies, Practice Exam, AI Practice; free start, account for the full bank",
      domains: [
        ["c103_d1", "Plan and manage an Azure AI solution", "25-30%"],
        ["c103_d2", "Implement generative AI and agentic solutions", "30-35%"],
        ["c103_d3", "Implement computer vision solutions", "10-15%"],
        ["c103_d4", "Implement text analysis solutions", "10-15%"],
        ["c103_d5", "Implement information extraction solutions", "10-15%"],
      ],
      gaps: {
        title: "Ten gaps, one lab each",
        note: "The parts of the exam that are Azure surface rather than concepts. Each one is a lab in the Azure free account, deleted the same day if it has a running cost.",
        items: [
          ["c103_g1", "Foundry project model: hub, project, connections"],
          ["c103_g2", "Azure OpenAI deployment mechanics: quotas, regions, content filters, managed identity"],
          ["c103_g3", "Azure AI Search: semantic ranker, integrated vectorisation, indexers, skillsets"],
          ["c103_g4", "Foundry Agent Service: single agent with tools, then multi-agent"],
          ["c103_g5", "Foundry evaluators: groundedness, relevance, similarity, safety"],
          ["c103_g6", "Azure AI Document Intelligence"],
          ["c103_g7", "Azure Content Understanding: documents, images, audio, video"],
          ["c103_g8", "Azure AI Speech: speech to text, text to speech"],
          ["c103_g9", "Azure Content Safety: Prompt Shields, groundedness detection, protected material"],
          ["c103_g10", "CI/CD into Foundry: Bicep or Azure DevOps"],
        ],
      },
      steps: [
        ["c103_s1", "Read the official study guide; plan hours by domain weight"],
        ["c103_s2", "Microsoft Learn AI-103 learning path finished"],
        ["c103_s3", "CertiAce study guide read, all four CertiAce modules done, case studies included"],
        ["c103_s4", "One CertiAce practice exam per week from week 3; official Practice Assessment 800 or more, timed"],
        ["c103_s5", "Exam booked"],
        ["c103_s6", "Passed"],
      ],
    },
  ],
};

// Deep dives: longer material that sits beside the path, not inside it.
// `onPath: true` means it is part of the work; `onPath: false` means optional
// theory that no AI engineering job requires.
const PATH_DEEPDIVES = {
  id: "deep",
  title: "Deep dives beside the path",
  cap: "one is on the path, one is optional theory",
  intro: "Two long documents that go far past what any phase asks for. Read the first when you reach the retrieval layer of your project. Read the second only if you want the mathematics for its own sake.",
  items: [
    {
      id: "dd_questions",
      onPath: true,
      badge: "On the path",
      title: "Embeddings, Vector Search & Retrieval: 30 questions",
      author: "@techNmak",
      where: "Phase 2, level 2, and the retrieval half of Phase 3",
      blurb: "Thirty questions with answers, covering pooling, cosine versus dot product, contrastive training, BM25, SPLADE, hybrid retrieval and Reciprocal Rank Fusion, cross-encoders, ColBERT late interaction, HNSW, IVF, Product Quantization, metadata filtering, index freshness, embedding-model migration, memory sizing, and the retrieval metrics. Every question is self-rated and saved.",
      href: "#/questions",
      linkText: "Open the 30 questions",
      internal: true,
    },
    {
      id: "dd_18657",
      onPath: false,
      badge: "Optional theory, off the path",
      title: "MIT 18.657: Mathematics of Machine Learning",
      author: "Philippe Rigollet, MIT, Fall 2015",
      where: "Nowhere. It is not a phase requirement and it is not a prerequisite for anything below.",
      blurb: "194 pages, 23 lectures of graduate statistical learning theory: empirical risk minimisation, concentration inequalities, VC dimension, Rademacher complexity, convex relaxations, boosting, support vector machines, mirror descent, stochastic and online optimisation, stochastic and adversarial bandits, Blackwell approachability. It answers how much data a method needs to reach a given accuracy. It teaches nothing about building on foundation models, and it assumes a first graduate course in statistics and measure-theoretic probability.",
      href: "https://ocw.mit.edu/courses/18-657-mathematics-of-machine-learning-fall-2015/",
      linkText: "MIT OpenCourseWare course page",
      internal: false,
      warning: "Phase 0 has a hard three-week cap for a reason: intuition, not mastery. This course is the opposite of that cap. Opening it before you have shipped the Phase 2 project is the classic way to spend six months feeling productive and shipping nothing.",
    },
  ],
};

// ===== Persistence =====
const pathProgress = {
  _data: null,
  load() {
    try { this._data = JSON.parse(localStorage.getItem(PATH_STORAGE_KEY)) || {}; }
    catch { this._data = {}; }
  },
  save() {
    try { localStorage.setItem(PATH_STORAGE_KEY, JSON.stringify(this._data)); }
    catch { /* storage unavailable: progress lives for this page view only */ }
  },
  isDone(id) { if (!this._data) this.load(); return !!this._data[id]; },
  set(id, done) {
    if (!this._data) this.load();
    if (done) this._data[id] = true; else delete this._data[id];
    this.save();
  },
  reset() { this._data = {}; try { localStorage.removeItem(PATH_STORAGE_KEY); } catch { /* ignore */ } },
};
pathProgress.load();

function pathPhase1Ids() {
  const ids = [];
  for (const g of PATH_GROUPS) for (const [vid] of g.steps) ids.push(vid);
  for (const [gid] of PATH_GATES) ids.push(gid);
  return ids;
}

function pathPhaseIds(phase) {
  return phase.items.map(([id]) => id).filter(Boolean);
}

function pathCount(ids) {
  const done = ids.filter(id => pathProgress.isDone(id)).length;
  return { done, total: ids.length, pct: ids.length ? Math.round(done / ids.length * 100) : 0 };
}

function pathCertIds() {
  const ids = [];
  for (const ex of PATH_CERTS.exams) {
    for (const [id] of ex.domains) ids.push(id);
    if (ex.gaps) for (const [id] of ex.gaps.items) ids.push(id);
    for (const [id] of ex.steps) ids.push(id);
  }
  return ids;
}

function pathAllIds() {
  const ids = pathPhase1Ids();
  for (const p of PATH_PHASES) ids.push(...pathPhaseIds(p));
  ids.push(...pathCertIds());
  return ids;
}

// ===== Event handlers (global, called from inline handlers) =====
function pathSetDone(id, done) {
  pathProgress.set(id, done);
  document.querySelectorAll(`[data-step="${id}"]`).forEach(el => el.classList.toggle("done", done));
  const strip = document.getElementById("path-progress");
  if (strip) strip.innerHTML = renderPathProgressStrip();
  document.querySelectorAll("[data-group-count]").forEach(el => {
    const ids = el.getAttribute("data-group-count").split(",");
    const c = pathCount(ids);
    el.textContent = `${c.done}/${c.total}`;
  });
}

function pathToggleEmbed(videoId, btn) {
  const box = document.getElementById(`embed-${videoId}`);
  if (!box) return;
  if (box.hidden) {
    if (!box.firstChild) {
      const iframe = document.createElement("iframe");
      iframe.src = `https://www.youtube-nocookie.com/embed/${videoId}`;
      iframe.title = (PATH_VIDEOS[videoId] || {}).title || "Video";
      iframe.loading = "lazy";
      iframe.allow = "accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      iframe.referrerPolicy = "strict-origin-when-cross-origin";
      iframe.setAttribute("allowfullscreen", "");
      box.appendChild(iframe);
    }
    box.hidden = false;
    if (btn) btn.textContent = "▲ Hide";
  } else {
    box.hidden = true;
    if (btn) btn.textContent = "▶ Watch";
  }
}

function resetPathProgress() {
  if (!confirm("Reset your path progress? This clears every checkbox on this page. Exercise progress is not affected.")) return;
  pathProgress.reset();
  render();
}

// ===== Renderers =====
function renderPathStep(videoId, topicId, opts = {}) {
  const v = PATH_VIDEOS[videoId];
  if (!v) return "";
  const done = pathProgress.isDone(videoId);
  const title = (v.type === "P" ? "Practice: " : "") + v.title;
  let topicLink = "";
  if (topicId && !opts.compact && typeof exerciseData !== "undefined" && exerciseData) {
    const topic = exerciseData.topics.find(t => t.id === topicId);
    if (topic) {
      const n = progress.countCompleted(topicId);
      topicLink = `<a class="path-topic-link" href="#/topic/${topicId}/exercises">Pytor exercises: ${escapeHtml(topic.title)} (${n}/${topic.exercise_count} done) →</a>`;
    }
  }
  return `
    <div class="path-step ${done ? "done" : ""}" data-step="${videoId}">
      <label class="path-check" title="Mark done">
        <input type="checkbox" ${done ? "checked" : ""} onchange="pathSetDone('${videoId}', this.checked)">
      </label>
      <div class="path-step-main">
        <div class="path-step-title">${escapeHtml(title)}</div>
        <div class="path-step-meta">
          <span class="path-pill pill-${v.type}">${PATH_TYPE_LABEL[v.type]}</span>
          <span>${v.min} min</span>
          <a href="https://youtu.be/${videoId}" target="_blank" rel="noopener">Open on YouTube ↗</a>
          ${topicLink}
        </div>
      </div>
      <button class="action-btn path-watch-btn" onclick="pathToggleEmbed('${videoId}', this)">▶ Watch</button>
      <div class="path-embed" id="embed-${videoId}" hidden></div>
    </div>`;
}

function renderPathGroup(group, opts = {}) {
  const ids = group.steps.map(([vid]) => vid);
  const c = pathCount(ids);
  const rows = group.steps.map(([vid, topic]) => renderPathStep(vid, topic, opts)).join("");
  const note = group.note ? `<p class="path-note">${escapeHtml(group.note)}</p>` : "";
  return `
    <div class="path-group" id="group-${group.id}">
      <div class="path-group-head">
        <h3>${escapeHtml(group.title)}</h3>
        <span class="path-group-count" data-group-count="${ids.join(",")}">${c.done}/${c.total}</span>
      </div>
      ${note}
      <div class="path-steps">${rows}</div>
    </div>`;
}

function renderPathCheckItem(id, text, suffixHtml = "") {
  if (!id) return `<li class="path-item nocheck"><span>${escapeHtml(text)}</span>${suffixHtml}</li>`;
  const done = pathProgress.isDone(id);
  return `
    <li class="path-item ${done ? "done" : ""}" data-step="${id}">
      <label><input type="checkbox" ${done ? "checked" : ""} onchange="pathSetDone('${id}', this.checked)"> <span>${escapeHtml(text)}</span>${suffixHtml}</label>
    </li>`;
}

function renderPathProgressStrip() {
  const all = pathCount(pathAllIds());
  const p1 = pathCount(pathPhase1Ids());
  const bars = [];
  const phaseBar = (label, c) => `
    <div class="path-mini">
      <div class="path-mini-label"><span>${label}</span><span>${c.done}/${c.total}</span></div>
      <div class="progress-bar"><div class="progress-fill" style="width:${c.pct}%"></div></div>
    </div>`;
  const byNum = {};
  for (const p of PATH_PHASES) byNum[p.num] = p;
  bars.push(phaseBar("0 Math", pathCount(pathPhaseIds(byNum[0]))));
  bars.push(phaseBar("1 Python", p1));
  bars.push(phaseBar("2 Project", pathCount(pathPhaseIds(byNum[2]))));
  bars.push(phaseBar("3 Skills", pathCount(pathPhaseIds(byNum[3]))));
  bars.push(phaseBar("4 Experience", pathCount(pathPhaseIds(byNum[4]))));
  bars.push(phaseBar("🎓 Certs", pathCount(pathCertIds())));
  return `
    <div class="path-progress-top">
      <strong>${all.done}/${all.total} steps done</strong>
      <span>${all.pct}%</span>
    </div>
    <div class="progress-bar"><div class="progress-fill" style="width:${all.pct}%"></div></div>
    <div class="path-minis">${bars.join("")}</div>`;
}

function renderPathPhaseCard(phase) {
  const c = pathCount(pathPhaseIds(phase));
  const items = phase.items.map(([id, text]) => renderPathCheckItem(id, text)).join("");
  return `
    <details class="phase-card">
      <summary>
        <span class="phase-num">${phase.num}</span>
        <span class="phase-title">${escapeHtml(phase.title)}</span>
        <span class="phase-cap">${escapeHtml(phase.cap)}</span>
        <span class="phase-count">${c.done}/${c.total}</span>
      </summary>
      <div class="phase-body">
        <p class="path-note">${escapeHtml(phase.intro)}</p>
        <ul class="path-items">${items}</ul>
      </div>
    </details>`;
}

function renderPathCertExam(ex) {
  const domainItems = ex.domains.map(([id, text, w]) =>
    renderPathCheckItem(id, text, `<span class="path-group-count cert-weight">${escapeHtml(w)} of the exam</span>`)
  ).join("");
  const stepItems = ex.steps.map(([id, text]) => renderPathCheckItem(id, text)).join("");
  let gapsHtml = "";
  if (ex.gaps) {
    const gapIds = ex.gaps.items.map(([id]) => id);
    const gc = pathCount(gapIds);
    gapsHtml = `
      <details class="path-group cert-gaps">
        <summary class="path-group-head">
          <h3>${escapeHtml(ex.gaps.title)}</h3>
          <span class="path-group-count" data-group-count="${gapIds.join(",")}">${gc.done}/${gc.total}</span>
        </summary>
        <p class="path-note">${escapeHtml(ex.gaps.note)}</p>
        <ul class="path-items">${ex.gaps.items.map(([id, text]) => renderPathCheckItem(id, text)).join("")}</ul>
      </details>`;
  }
  const allIds = [...ex.domains.map(([id]) => id), ...(ex.gaps ? ex.gaps.items.map(([id]) => id) : []), ...ex.steps.map(([id]) => id)];
  const c = pathCount(allIds);
  return `
    <div class="cert-block">
      <div class="path-group-head">
        <h3>${escapeHtml(ex.code)}: ${escapeHtml(ex.name)}</h3>
        <span class="path-group-count" data-group-count="${allIds.join(",")}">${c.done}/${c.total}</span>
      </div>
      <p class="path-note">${escapeHtml(ex.facts)}</p>
      <p class="path-sources cert-sources">
        <strong>Official first:</strong> <a href="${ex.official}" target="_blank" rel="noopener">Microsoft study guide, skills measured ↗</a><br>
        <strong>Then CertiAce:</strong> <a href="${ex.guide}" target="_blank" rel="noopener">study guide ↗</a> · <a href="${ex.practice}" target="_blank" rel="noopener">practice ↗</a> <span class="cert-note">(${escapeHtml(ex.practiceNote)})</span>
      </p>
      <h4 class="cert-sub">Domains (tick when you can teach it)</h4>
      <ul class="path-items">${domainItems}</ul>
      ${gapsHtml}
      <h4 class="cert-sub">Milestones</h4>
      <ul class="path-items">${stepItems}</ul>
    </div>`;
}

function renderPathCertsCard() {
  const c = pathCount(pathCertIds());
  return `
    <details class="phase-card phase-certs">
      <summary>
        <span class="phase-num">🎓</span>
        <span class="phase-title">${escapeHtml(PATH_CERTS.title)}</span>
        <span class="phase-cap">${escapeHtml(PATH_CERTS.cap)}</span>
        <span class="phase-count" data-group-count="${pathCertIds().join(",")}">${c.done}/${c.total}</span>
      </summary>
      <div class="phase-body">
        <p class="path-note">${escapeHtml(PATH_CERTS.intro)}</p>
        ${PATH_CERTS.exams.map(renderPathCertExam).join("")}
      </div>
    </details>`;
}

function renderPathDeepDivesCard() {
  const items = PATH_DEEPDIVES.items.map(it => {
    const link = it.internal
      ? `<a class="action-btn" href="${it.href}" onclick="navigate('${it.href.slice(1)}'); return false;">${escapeHtml(it.linkText)} \u2192</a>`
      : `<a class="action-btn" href="${it.href}" target="_blank" rel="noopener">${escapeHtml(it.linkText)} \u2197</a>`;
    const warn = it.warning ? `<p class="path-note dd-warning"><strong>Read this first:</strong> ${escapeHtml(it.warning)}</p>` : "";
    return `
      <div class="cert-block dd-block ${it.onPath ? "dd-on" : "dd-off"}">
        <div class="path-group-head">
          <h3>${escapeHtml(it.title)}</h3>
          <span class="path-group-count dd-badge">${escapeHtml(it.badge)}</span>
        </div>
        <p class="path-note dd-author">${escapeHtml(it.author)}</p>
        <p class="path-note"><strong>Where it fits:</strong> ${escapeHtml(it.where)}</p>
        <p class="path-note">${escapeHtml(it.blurb)}</p>
        ${warn}
        <p style="margin-top:10px">${link}</p>
      </div>`;
  }).join("");
  return `
    <details class="phase-card">
      <summary>
        <span class="phase-num">\u{1f4da}</span>
        <span class="phase-title">${escapeHtml(PATH_DEEPDIVES.title)}</span>
        <span class="phase-cap">${escapeHtml(PATH_DEEPDIVES.cap)}</span>
      </summary>
      <div class="phase-body">
        <p class="path-note">${escapeHtml(PATH_DEEPDIVES.intro)}</p>
        ${items}
      </div>
    </details>`;
}

function renderPath(app) {
  const phase0 = PATH_PHASES.find(p => p.num === 0);
  const later = PATH_PHASES.filter(p => p.num > 1);
  const p1 = pathCount(pathPhase1Ids());
  const groupsHtml = PATH_GROUPS.map(g => renderPathGroup(g)).join("");
  const extrasIds = PATH_EXTRAS.steps.map(([vid]) => vid);
  const extrasCount = pathCount(extrasIds);
  const gatesHtml = PATH_GATES.map(([id, text]) => renderPathCheckItem(id, text)).join("");

  app.innerHTML = `
    <button class="back-btn" onclick="navigate('/dashboard')">← All Topics</button>

    <div class="path-hero">
      <h1>🧭 The AI Engineer Path</h1>
      <p>The goal is to build applications on top of foundation models, not to train them. The method is Marina Wyss's five phases: a short math map, Python by hand, one project you keep escalating, the five skills production teams pay for, and real experience you manufacture yourself. A Microsoft certification track (AI-901, then AI-103) runs alongside the project.</p>
      <div class="path-rule"><strong>The one rule:</strong> You type every line. Pytor explains and quizzes. It never writes your code.</div>
    </div>

    <div id="path-progress" class="path-progress">${renderPathProgressStrip()}</div>

    ${renderPathPhaseCard(phase0)}

    <details class="phase-card phase-main" open>
      <summary>
        <span class="phase-num">1</span>
        <span class="phase-title">Python by hand</span>
        <span class="phase-cap">2-3 months, the main body of the path</span>
        <span class="phase-count">${p1.done}/${p1.total}</span>
      </summary>
      <div class="phase-body">
        <div class="tips-box path-loop">
          <h3>🔁 The study loop, per topic</h3>
          <ol>
            <li>Watch the <strong>concept</strong> video. No notes.</li>
            <li>Open the <strong>practice</strong> video and <strong>pause at each problem</strong>.</li>
            <li>Type your solution in a real file and run it. Not in your head.</li>
            <li>Only then play the solution and compare.</li>
            <li>Do the matching <strong>Pytor exercises</strong> for the topic.</li>
          </ol>
        </div>
        <p class="path-sources">
          <strong>Course spine:</strong> <a href="${SCRIMBA_URL}" target="_blank" rel="noopener">Scrimba Learn Python</a> (free, 58 parts, builds an expense-splitting app). You pause the screencast and type into it.<br>
          <strong>Explanations and practice problems:</strong> <a href="${VE_CHANNEL_URL}" target="_blank" rel="noopener">Visually Explained</a> on YouTube. Nearly every concept video has a matching practice video; that pair is the unit of work below.
        </p>

        ${groupsHtml}

        <details class="path-group path-extras">
          <summary class="path-group-head">
            <h3>${escapeHtml(PATH_EXTRAS.title)}</h3>
            <span class="path-group-count" data-group-count="${extrasIds.join(",")}">${extrasCount.done}/${extrasCount.total}</span>
          </summary>
          <p class="path-note">${escapeHtml(PATH_EXTRAS.note)}</p>
          <div class="path-steps">${PATH_EXTRAS.steps.map(([vid, topic]) => renderPathStep(vid, topic)).join("")}</div>
        </details>

        <div class="path-group path-gate">
          <div class="path-group-head"><h3>🚪 Exit gate (all three, judged honestly)</h3></div>
          <ul class="path-items">${gatesHtml}</ul>
        </div>
      </div>
    </details>

    ${renderPathCertsCard()}

    ${renderPathDeepDivesCard()}

    ${later.map(renderPathPhaseCard).join("")}

    <div style="text-align:center;margin-top:32px;padding-top:24px;border-top:1px solid var(--border)">
      <button class="action-btn" onclick="resetPathProgress()" style="color:var(--error)">🔄 Reset path progress</button>
      <p style="font-size:0.75rem;color:var(--text-light);margin-top:6px">Progress is saved in this browser only.</p>
    </div>
  `;
}

// Used by the per-topic Watch tab in app.js.
function renderWatchList(topicId) {
  const ids = PATH_VIDEOS_BY_TOPIC[topicId] || [];
  if (!ids.length) {
    return `
      <div class="lesson-content"><div class="lesson-section">
        <h3>No videos matched to this topic yet</h3>
        <p>See the full <a href="#/path">AI Engineer Path</a> for the video sequence.</p>
      </div></div>`;
  }
  const rows = ids.map(vid => renderPathStep(vid, null, { compact: true })).join("");
  const c = pathCount(ids);
  return `
    <div class="path-watch">
      <p class="path-note">Short videos from <a href="${VE_CHANNEL_URL}" target="_blank" rel="noopener">Visually Explained</a> that match this topic. Watch the concept, then pause the practice video at each problem and type your answer in the <a href="#/playground">Playground</a> or a local file before you see the solution.</p>
      <div class="path-group">
        <div class="path-group-head">
          <h3>▶ Watch</h3>
          <span class="path-group-count" data-group-count="${ids.join(",")}">${c.done}/${c.total}</span>
        </div>
        <div class="path-steps">${rows}</div>
      </div>
      <p style="text-align:center;margin-top:16px"><a class="action-btn" href="#/path">🧭 See the whole path →</a></p>
    </div>`;
}
