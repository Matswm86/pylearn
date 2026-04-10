/* ===== PyLearn AI Tutor (Pytor) =====
 *
 * Default endpoint: https://pytor.mwmai.no/api/tutor
 *   - Caddy strips the /api/tutor prefix via handle_path
 *   - Upstream is a stdlib-only HTTP server at 127.0.0.1:8100
 *   - Groq-primary (llama-3.3-70b-versatile), Ollama fallback
 *
 * Override for local dev: localStorage.setItem("pylearn_tutor_url",
 *   "http://127.0.0.1:8100") — note: unprefixed, no /api/tutor for local.
 */

const TUTOR_API_URL =
  localStorage.getItem("pylearn_tutor_url") ||
  "https://pytor.mwmai.no/api/tutor";

// ===== API Client =====
class TutorAPI {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }

  async _post(endpoint, body) {
    const resp = await fetch(`${this.baseUrl}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(120000),
    });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    return resp.json();
  }

  async health() {
    const resp = await fetch(`${this.baseUrl}/health`, {
      signal: AbortSignal.timeout(5000),
    });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    return resp.json();
  }

  async chat(question, context = "", history = "") {
    return this._post("/chat", { question, context, history });
  }

  async hint(exerciseId, attempt = "") {
    return this._post("/hint", { exercise_id: exerciseId, attempt });
  }

  async designLesson(topic) {
    return this._post("/design-lesson", { topic });
  }

  async generatePage(title, summary, difficulty = "intermediate") {
    return this._post("/generate-page", { title, summary, difficulty });
  }
}

// ===== UI Controller =====
class TutorUI {
  constructor() {
    this.api = new TutorAPI(TUTOR_API_URL);
    this.available = false;
    this.sidebarOpen = false;
    this.history = this._loadHistory();
    this.currentContext = null; // { type: "exercise"|"topic", data: ... }
    this.loading = false;
  }

  // --- Init ---
  async init() {
    try {
      const h = await this.api.health();
      // Pytor is available whenever the bridge reports ok — either Groq
      // (primary) or Ollama (fallback) is enough.
      this.available = h.status === "ok";
    } catch {
      this.available = false;
    }

    const toggle = document.getElementById("tutor-toggle");
    const mascot = document.getElementById("pytor-mascot");
    if (toggle) toggle.style.display = this.available ? "" : "none";
    if (mascot) mascot.style.display = this.available ? "" : "none";

    // First-visit greeting bubble: show once, then stop pestering.
    if (this.available && mascot && !localStorage.getItem("pylearn_pytor_greeted")) {
      setTimeout(() => {
        mascot.classList.add("greet");
        localStorage.setItem("pylearn_pytor_greeted", "1");
        setTimeout(() => mascot.classList.remove("greet"), 6000);
      }, 1500);
    }

    // Restore sidebar state
    if (this.available && localStorage.getItem("pylearn_tutor_sidebar") === "open") {
      this.openSidebar();
    }

    this._renderMessages();
  }

  // --- Sidebar ---
  toggleSidebar() {
    if (this.sidebarOpen) this.closeSidebar();
    else this.openSidebar();
  }

  openSidebar() {
    this.sidebarOpen = true;
    const el = document.getElementById("tutor-sidebar");
    if (el) el.classList.add("open");
    document.getElementById("app").classList.add("tutor-shifted");
    document.getElementById("tutor-toggle")?.classList.add("active");
    localStorage.setItem("pylearn_tutor_sidebar", "open");
    this._scrollToBottom();
  }

  closeSidebar() {
    this.sidebarOpen = false;
    const el = document.getElementById("tutor-sidebar");
    if (el) el.classList.remove("open");
    document.getElementById("app").classList.remove("tutor-shifted");
    document.getElementById("tutor-toggle")?.classList.remove("active");
    localStorage.setItem("pylearn_tutor_sidebar", "closed");
  }

  // --- Context ---
  updateContext(route) {
    if (route.view === "exercise") {
      const app = document.getElementById("app");
      const ex = app?._exercise;
      if (ex) {
        this.currentContext = {
          type: "exercise",
          id: ex.id,
          title: ex.title,
          description: ex.description,
          concepts: ex.concepts,
          difficulty: ex.difficulty,
        };
      }
    } else if (route.view === "topic") {
      this.currentContext = { type: "topic", id: route.topicId };
    } else {
      this.currentContext = null;
    }
  }

  // --- Chat ---
  async sendMessage() {
    const input = document.getElementById("tutor-input");
    if (!input) return;
    const question = input.value.trim();
    if (!question || this.loading) return;

    input.value = "";
    this._addMessage("user", question);

    // Build context string
    let context = "";
    const useContext = document.getElementById("tutor-context-toggle")?.checked;
    if (useContext && this.currentContext) {
      if (this.currentContext.type === "exercise") {
        context = `Currently on exercise: ${this.currentContext.title}. ` +
          `Description: ${this.currentContext.description}. ` +
          `Concepts: ${(this.currentContext.concepts || []).join(", ")}`;
      } else if (this.currentContext.type === "topic") {
        context = `Currently studying topic: ${this.currentContext.id}`;
      }
    }

    // Build history string for API
    const historyForApi = JSON.stringify(
      this.history.slice(-6).map(m => ({ role: m.role, content: m.content }))
    );

    this._showLoading(true);
    try {
      const result = await this.api.chat(question, context, historyForApi);
      const response = result.response || result.error || "No response received.";
      this._addMessage("assistant", response);
    } catch (e) {
      this._addMessage("assistant", `Pytor is having trouble reaching the server (${e.message}). Try again in a moment?`);
    }
    this._showLoading(false);
  }

  async askAboutExercise() {
    if (!this.available) return;
    if (!this.sidebarOpen) this.openSidebar();

    const app = document.getElementById("app");
    const ex = app?._exercise;
    if (!ex) return;

    const question = `Help me understand this exercise: "${ex.title}". ${ex.description}`;
    const input = document.getElementById("tutor-input");
    if (input) {
      input.value = question;
      input.focus();
    }
  }

  async getAIHint() {
    if (!this.available) return;
    if (!this.sidebarOpen) this.openSidebar();

    const app = document.getElementById("app");
    const ex = app?._exercise;
    if (!ex) return;

    // Get current code from editor
    const attempt = window.currentEditor ? window.currentEditor.getValue() : "";

    this._addMessage("user", `Get a hint for: ${ex.title}`);
    this._showLoading(true);

    try {
      const result = await this.api.hint(ex.id, attempt);
      const response = result.response || result.error || "Could not generate hint.";
      this._addMessage("assistant", response);
    } catch (e) {
      this._addMessage("assistant", `Connection error: ${e.message}`);
    }
    this._showLoading(false);
  }

  // --- Generate Lesson ---
  openLessonModal() {
    const modal = document.getElementById("lesson-modal");
    if (modal) modal.classList.add("open");
    document.getElementById("lesson-topic")?.focus();
  }

  closeLessonModal() {
    const modal = document.getElementById("lesson-modal");
    if (modal) modal.classList.remove("open");
    const container = document.getElementById("lesson-iframe-container");
    if (container) container.style.display = "none";
  }

  async generateLesson() {
    const input = document.getElementById("lesson-topic");
    const topic = input?.value.trim();
    if (!topic) return;

    const btn = document.getElementById("lesson-generate-btn");
    const container = document.getElementById("lesson-iframe-container");
    const iframe = document.getElementById("lesson-iframe");
    const status = document.getElementById("lesson-status");

    if (btn) { btn.disabled = true; btn.textContent = "Generating..."; }
    if (status) { status.textContent = "Designing lesson structure..."; status.style.display = "block"; }
    if (container) container.style.display = "none";

    try {
      // Step 1: Design lesson
      const lesson = await this.api.designLesson(topic);
      const lessonData = lesson.response;

      // Step 2: Generate HTML page
      let title = topic;
      let summary = `Learn about ${topic} in Python`;
      let difficulty = "intermediate";

      if (lessonData && typeof lessonData === "object" && lessonData.knowledge_points) {
        const kp = lessonData.knowledge_points[0];
        if (kp) {
          title = kp.title || title;
          summary = kp.summary || summary;
          difficulty = kp.difficulty || difficulty;
        }
      }

      if (status) status.textContent = "Generating interactive page...";
      const page = await this.api.generatePage(title, summary, difficulty);
      const html = page.response;

      if (html && iframe) {
        iframe.srcdoc = html;
        if (container) container.style.display = "block";
        if (status) status.style.display = "none";
      }
    } catch (e) {
      if (status) { status.textContent = `Error: ${e.message}`; status.style.display = "block"; }
    }

    if (btn) { btn.disabled = false; btn.textContent = "Generate"; }
  }

  // --- History ---
  clearHistory() {
    this.history = [];
    this._saveHistory();
    this._renderMessages();
  }

  _addMessage(role, content) {
    this.history.push({ role, content, ts: Date.now() });
    // Cap at 50 messages
    if (this.history.length > 50) this.history = this.history.slice(-50);
    this._saveHistory();
    this._renderMessages();
    this._scrollToBottom();
  }

  _loadHistory() {
    try {
      return JSON.parse(localStorage.getItem("pylearn_tutor_history")) || [];
    } catch {
      return [];
    }
  }

  _saveHistory() {
    localStorage.setItem("pylearn_tutor_history", JSON.stringify(this.history));
  }

  // --- Rendering ---
  _renderMessages() {
    const area = document.getElementById("tutor-chat-area");
    if (!area) return;

    if (this.history.length === 0) {
      area.innerHTML = `<div class="tutor-empty">Hi, I'm <strong>Pytor</strong> 🐍<br>Ask me anything about Python — I'll guide you with questions rather than just hand you the answer.</div>`;
      return;
    }

    area.innerHTML = this.history.map(m =>
      `<div class="tutor-msg ${m.role}">${this._escapeHtml(m.content)}</div>`
    ).join("");
  }

  _showLoading(show) {
    this.loading = show;
    const area = document.getElementById("tutor-chat-area");
    const existing = area?.querySelector(".tutor-loading");
    if (show && area && !existing) {
      area.insertAdjacentHTML("beforeend",
        `<div class="tutor-loading"><span></span><span></span><span></span></div>`
      );
      this._scrollToBottom();
    } else if (!show && existing) {
      existing.remove();
    }
    // Disable/enable send button
    const sendBtn = document.getElementById("tutor-send-btn");
    if (sendBtn) sendBtn.disabled = show;
  }

  _scrollToBottom() {
    const area = document.getElementById("tutor-chat-area");
    if (area) requestAnimationFrame(() => { area.scrollTop = area.scrollHeight; });
  }

  _escapeHtml(s) {
    const div = document.createElement("div");
    div.textContent = s;
    return div.innerHTML;
  }
}

// ===== Init =====
window.tutorUI = new TutorUI();

// Handle Enter key in chat input
document.addEventListener("keydown", (e) => {
  if (e.target.id === "tutor-input" && e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    window.tutorUI.sendMessage();
  }
  // Handle Enter in lesson topic input
  if (e.target.id === "lesson-topic" && e.key === "Enter") {
    e.preventDefault();
    window.tutorUI.generateLesson();
  }
});

// Init after DOM ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => window.tutorUI.init());
} else {
  window.tutorUI.init();
}
