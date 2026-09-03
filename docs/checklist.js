/* ===== AI Engineering Skills Checklist =====
 *
 * Marina Wyss's checklist (https://marinawyss.com), rebuilt here so the
 * boxes can be ticked and remembered. The item text is hers, verbatim.
 * The "where this lives" line under each section is the only thing added:
 * it ties her sections to the phases on the Path page.
 *
 * Progress is stored per browser in localStorage under CHECKLIST_STORAGE_KEY.
 */

const CHECKLIST_AUTHOR_URL = "https://marinawyss.com";
const AIE_RESOURCES_URL = "https://github.com/chiphuyen/aie-book/blob/main/resources.md";
const CHECKLIST_STORAGE_KEY = "pylearn_checklist";

// Section titles and items: transcribed verbatim, in the original order.
// `phase` and `reading` are the additions that tie this to the Path page.
const CHECKLIST_SECTIONS = [
  {
    title: "Technical Foundation",
    phase: "Phase 0, the three-week math map",
    items: [
      "Basic statistics and probability",
      "Probability distributions",
      "Averages and variance",
      "Basic linear algebra: vectors and matrices",
      "Basic calculus: derivatives and gradients",
      "Understanding of numerical precision formats",
      "Data structures and algorithms fundamentals",
      "Intuition for the concepts, rather than doing the math by hand",
    ],
  },
  {
    title: "Python",
    phase: "Phase 1, Python by hand",
    items: [
      "Functions and classes",
      "Core data structures, and when to use each",
      "Error handling",
      "Reading a traceback to find the real problem",
      "Working with APIs",
      "Using third-party libraries",
      "Writing Python without an AI finishing your lines",
    ],
  },
  {
    title: "Software Engineering",
    phase: "Phase 1 and the project in Phase 2",
    items: [
      "Structuring a project",
      "Git and version control",
      "Virtual environments",
      "Config files instead of hardcoded settings",
      "Writing tests",
      "Linux and command-line tools",
      "Enough backend to ship, without being a backend expert",
    ],
  },
  {
    title: "ML Basics",
    phase: "Phase 0",
    items: [
      "Supervised vs. unsupervised learning",
      "Common algorithms at a high level",
      "Training/validation/test splits",
      "Overfitting and underfitting",
      "Model evaluation metrics: precision, recall",
      "Neural networks at a high level",
      "Strong deep learning knowledge",
    ],
  },
  {
    title: "Foundation Models & Model Selection",
    phase: "Phase 2, level 1",
    reading: `${AIE_RESOURCES_URL}#chapter-2-understanding-foundation-models`,
    items: [
      "Transformer architecture",
      "Attention mechanism",
      "Tokenization",
      "Post-training techniques: SFT, RLHF, DPO",
      "Tradeoffs: performance vs. cost vs. speed vs. licensing",
      "Open-weight vs. open-source vs. API models",
      "Tooling for model benchmarking",
    ],
  },
  {
    title: "Prompt Engineering",
    phase: "Phase 2, level 1",
    reading: `${AIE_RESOURCES_URL}#chapter-5-prompt-engineering`,
    items: [
      "Structuring effective prompts",
      "Few-shot and in-context learning",
      "Structured outputs",
      "Defensive prompt engineering against attacks",
      "Prompt experimentation and tracking",
      "Testing changes systematically instead of eyeballing them",
    ],
  },
  {
    title: "Context Engineering",
    phase: "Phase 3, skill 2",
    items: [
      "Deciding what the model sees, and in what order",
      "Deciding what gets cut when there's too much",
      "Context construction patterns",
      "Conversation history and memory management",
      "Token budgeting",
    ],
  },
  {
    title: "Retrieval-Augmented Generation",
    phase: "Phase 2, level 2",
    reading: `${AIE_RESOURCES_URL}#chapter-6-rag-and-agents`,
    items: [
      "Vector database implementation",
      "Document chunking strategies",
      "Embedding techniques",
      "Term-based vs. embedding-based retrieval",
      "Retrieval optimization techniques",
    ],
  },
  {
    title: "Evaluation and Testing",
    phase: "Phase 3, skill 1, the one that comes first",
    reading: `${AIE_RESOURCES_URL}#chapters-3--4-evaluation-methodology`,
    items: [
      "Model evaluation pipelines",
      "Building test sets",
      "Metrics: perplexity, BLEU, ROUGE, semantic similarity, functional correctness",
      "AI judges and human evals",
      "Measuring hallucinations, toxicity, bias",
    ],
  },
  {
    title: "Agent Systems",
    phase: "Phase 2, levels 3 and 4",
    reading: `${AIE_RESOURCES_URL}#chapter-6-rag-and-agents`,
    items: [
      "Tool calling and integration",
      "Planning and reflection techniques",
      "Memory systems implementation",
      "Working with MCP",
      "Agent security and safety guardrails",
      "Agent evaluation methodologies",
      "Multi-agent system design",
    ],
  },
  {
    title: "Finetuning",
    phase: "Beyond this path. An AI engineer builds on pretrained models; learn it when a job asks.",
    reading: `${AIE_RESOURCES_URL}#chapter-7-finetuning`,
    items: [
      "Parameter-efficient fine-tuning (PEFT)",
      "LoRA and similar approaches",
      "Model distillation",
      "Model merging",
      "Multi-task fine-tuning",
    ],
  },
  {
    title: "Dataset Engineering",
    phase: "Beyond this path, same reason as finetuning.",
    reading: `${AIE_RESOURCES_URL}#chapter-8-dataset-engineering`,
    items: [
      "Data acquisition strategies",
      "Data quality assessment",
      "Data processing",
      "Annotation guidelines creation",
      "Data augmentation and synthesis",
    ],
  },
  {
    title: "Inference Optimization",
    phase: "Phase 3, skill 4, LLMOps",
    reading: `${AIE_RESOURCES_URL}#chapter-9-inference-optimization`,
    items: [
      "Compute vs. memory-bound inference",
      "Latency metrics: TTFT, TPOT",
      "Model compression: quantization, pruning, distillation",
      "Batch vs. online inference strategies",
      "Hardware (GPU, TPU, memory specs)",
      "Batching techniques",
      "Parallel inference strategies",
      "Caching implementations",
    ],
  },
  {
    title: "Application Architecture",
    phase: "Phase 3",
    reading: `${AIE_RESOURCES_URL}#chapter-10-ai-engineering-architecture-and-user-feedback`,
    items: [
      "Input/output guardrails",
      "Model routing and gateways",
      "Caching architectures",
      "Orchestration patterns",
    ],
  },
  {
    title: "Production Engineering",
    phase: "Phase 3, skills 3 and 4",
    items: [
      "Building APIs",
      "Cloud platforms",
      "Docker and containers",
      "Basic CI/CD",
      "Monitoring and logging",
      "Debugging what went wrong in production",
      "Cost, speed, and security under real traffic",
    ],
  },
  {
    title: "Security / Privacy / Ethics",
    phase: "Phase 3, and the AI-103 certificate's content-safety domain",
    items: [
      "Prompt injection detection and mitigation",
      "Adversarial input handling",
      "PII detection and redaction",
      "Secure sandboxing for agents and code execution",
      "Model privacy risks: memorization attacks, data leakage",
      "Legal compliance: GDPR, copyright implications",
      "AI ethics considerations",
    ],
  },
];

// ===== Persistence =====
const checklistProgress = {
  _data: null,
  load() {
    try { this._data = JSON.parse(localStorage.getItem(CHECKLIST_STORAGE_KEY)) || {}; }
    catch { this._data = {}; }
  },
  save() {
    try { localStorage.setItem(CHECKLIST_STORAGE_KEY, JSON.stringify(this._data)); }
    catch { /* storage unavailable: progress lives for this page view only */ }
  },
  isDone(id) { if (!this._data) this.load(); return !!this._data[id]; },
  set(id, done) {
    if (!this._data) this.load();
    if (done) this._data[id] = true; else delete this._data[id];
    this.save();
  },
  reset() {
    this._data = {};
    try { localStorage.removeItem(CHECKLIST_STORAGE_KEY); } catch { /* ignore */ }
  },
};
checklistProgress.load();

// Ids are positional on purpose: rewording an item must not orphan a tick.
function checklistItemId(sectionIndex, itemIndex) {
  return `sk_${sectionIndex}_${itemIndex}`;
}

function checklistSectionIds(sectionIndex) {
  return CHECKLIST_SECTIONS[sectionIndex].items.map((_, i) => checklistItemId(sectionIndex, i));
}

function checklistAllIds() {
  const ids = [];
  CHECKLIST_SECTIONS.forEach((_, si) => ids.push(...checklistSectionIds(si)));
  return ids;
}

function checklistCount(ids) {
  const done = ids.filter(id => checklistProgress.isDone(id)).length;
  return { done, total: ids.length, pct: ids.length ? Math.round(done / ids.length * 100) : 0 };
}

// ===== Event handlers (global, called from inline handlers) =====
function checklistSetDone(id, done) {
  checklistProgress.set(id, done);
  document.querySelectorAll(`[data-skill="${id}"]`).forEach(el => el.classList.toggle("done", done));
  const strip = document.getElementById("checklist-progress");
  if (strip) strip.innerHTML = renderChecklistProgressStrip();
  document.querySelectorAll("[data-skill-count]").forEach(el => {
    const c = checklistCount(el.getAttribute("data-skill-count").split(","));
    el.textContent = `${c.done}/${c.total}`;
  });
}

function resetChecklistProgress() {
  if (!confirm("Reset the skills checklist? This clears all 100 boxes. Nothing else on the site is affected.")) return;
  checklistProgress.reset();
  render();
}

// ===== Rendering =====
function renderChecklistProgressStrip() {
  const c = checklistCount(checklistAllIds());
  return `
    <div class="path-progress-top">
      <strong>${c.done}/${c.total} complete</strong>
      <span>${c.pct}%</span>
    </div>
    <div class="progress-bar"><div class="progress-fill" style="width:${c.pct}%"></div></div>`;
}

function renderChecklistSection(section, si) {
  const ids = checklistSectionIds(si);
  const c = checklistCount(ids);
  const beyond = section.phase.startsWith("Beyond this path");
  const items = section.items.map((text, ii) => {
    const id = checklistItemId(si, ii);
    const done = checklistProgress.isDone(id);
    return `
      <li class="path-item ${done ? "done" : ""}" data-skill="${id}">
        <label><input type="checkbox" ${done ? "checked" : ""} onchange="checklistSetDone('${id}', this.checked)"> <span>${escapeHtml(text)}</span></label>
      </li>`;
  }).join("");
  const reading = section.reading
    ? `<a href="${section.reading}" target="_blank" rel="noopener">Further reading: curated resource list ↗</a>`
    : "";
  return `
    <details class="phase-card skill-card ${beyond ? "skill-beyond" : ""}" ${beyond ? "" : "open"}>
      <summary>
        <span class="phase-title">${escapeHtml(section.title)}</span>
        <span class="phase-count" data-skill-count="${ids.join(",")}">${c.done}/${c.total}</span>
      </summary>
      <div class="phase-body">
        <p class="path-note skill-where">
          <span class="skill-phase">${escapeHtml(section.phase)}</span>
          ${reading}
        </p>
        <ul class="path-items">${items}</ul>
      </div>
    </details>`;
}

function renderChecklist(app) {
  const sections = CHECKLIST_SECTIONS.map(renderChecklistSection).join("");

  app.innerHTML = `
    <button class="back-btn" onclick="navigate('/dashboard')">← All Topics</button>

    <div class="path-hero">
      <h1>📋 AI Engineering Skills Checklist</h1>
      <p>The checklist is <a href="${CHECKLIST_AUTHOR_URL}" target="_blank" rel="noopener">Marina Wyss</a>'s, rebuilt here so you can tick the boxes and have them remembered. The full skill set, from fundamentals through to shipping: work through it in any order, and you do not need all of it to start.</p>
      <p class="path-note">The further-reading links point at Chip Huyen's free resource list on GitHub, roughly 166 links arranged by the chapters of the book <em>AI Engineering</em>.</p>
      <p class="path-note">The five phases and the certificate track live on the <a href="#/path" onclick="navigate('/path'); return false;">Path page</a>.</p>
      <div class="path-rule"><strong>The one thing to take away:</strong> the biggest mistake is waiting until you've learned all of this to build anything.</div>
    </div>

    <div id="checklist-progress" class="path-progress">${renderChecklistProgressStrip()}</div>

    ${sections}

    <div style="text-align:center;margin-top:32px;padding-top:24px;border-top:1px solid var(--border)">
      <button class="action-btn" onclick="resetChecklistProgress()" style="color:var(--error)">🔄 Reset checklist</button>
      <p style="font-size:0.75rem;color:var(--text-light);margin-top:6px">Progress is saved in this browser only.</p>
    </div>
  `;
}
