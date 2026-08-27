/* ===== PyLearn Playground worker =====
   Runs user code in a Web Worker so an infinite loop can be killed
   (worker.terminate()) without freezing the page. */

const PYODIDE_VERSION = "0.26.4";
let pyodide = null;

function post(type, payload) { self.postMessage({ type, ...payload }); }

const RUNNER = `
import sys, io, builtins, traceback

def __pg_run(src, stdin_text):
    sys.stdin = io.StringIO(stdin_text)
    _lines = iter(stdin_text.split("\\n")) if stdin_text else iter(())
    _real_input = builtins.input
    def _input(prompt=""):
        if prompt:
            print(prompt, end="")
        try:
            line = next(_lines)
        except StopIteration:
            raise EOFError("no more input - add a line to the Input (stdin) box")
        print(line)
        return line
    builtins.input = _input
    g = {"__name__": "__main__", "__file__": "main.py", "__builtins__": builtins}
    try:
        exec(compile(src, "main.py", "exec"), g)
        return 0
    except SystemExit as e:
        return int(e.code or 0)
    except BaseException as e:
        tb = e.__traceback__.tb_next          # hide the __pg_run frame
        traceback.print_exception(type(e), e, tb)
        return 1
    finally:
        builtins.input = _real_input
`;

async function ensurePyodide() {
  if (pyodide) return pyodide;
  post("status", { text: "Loading Python engine (first run ~10s)..." });
  self.importScripts(`https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js`);
  pyodide = await loadPyodide({
    indexURL: `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`,
  });
  pyodide.setStdout({ batched: (t) => post("stdout", { text: t + "\n" }) });
  pyodide.setStderr({ batched: (t) => post("stderr", { text: t + "\n" }) });
  pyodide.runPython(RUNNER);
  pyodide.runPython("import sys\nsys.path.insert(0, '/home/pyodide')");
  post("status", { text: "" });
  return pyodide;
}

// Names that are import-able but whose PyPI/package name differs
const IMPORT_ALIASES = { PIL: "pillow", cv2: "opencv-python", sklearn: "scikit-learn", yaml: "pyyaml", bs4: "beautifulsoup4" };

function topLevelImports(src) {
  const names = new Set();
  const re = /^\s*(?:import\s+([A-Za-z_][\w.]*)|from\s+([A-Za-z_][\w.]*)\s+import)/gm;
  let m;
  while ((m = re.exec(src)) !== null) {
    const mod = (m[1] || m[2]).split(".")[0];
    if (mod) names.add(mod);
  }
  return [...names];
}

async function ensurePackages(py, src) {
  // 1. Packages bundled with Pyodide (numpy, pandas, matplotlib, ...)
  try {
    await py.loadPackagesFromImports(src, {
      messageCallback: (t) => post("status", { text: t }),
      errorCallback: () => {},
    });
  } catch (e) { /* unknown modules are handled below */ }

  // 2. Anything still missing -> try micropip (pure-Python wheels on PyPI)
  const missing = topLevelImports(src).filter((n) => {
    try { return !py.runPython(`import importlib.util as _u\n_u.find_spec(${JSON.stringify(n)}) is not None`); }
    catch { return true; }
  });
  if (!missing.length) return;
  await py.loadPackage("micropip");
  const micropip = py.pyimport("micropip");
  for (const name of missing) {
    const pkg = IMPORT_ALIASES[name] || name;
    post("status", { text: `Installing ${pkg} from PyPI...` });
    try { await micropip.install(pkg); }
    catch (e) { post("stderr", { text: `Could not install "${pkg}": ${e.message || e}\n` }); }
  }
  post("status", { text: "" });
}

self.onmessage = async (ev) => {
  const msg = ev.data;
  if (msg.type === "init") {
    try { await ensurePyodide(); post("ready", {}); }
    catch (e) { post("fatal", { text: String(e && e.message || e) }); }
    return;
  }
  if (msg.type !== "run") return;

  try {
    const py = await ensurePyodide();

    // Write every project file to the virtual FS so `import helper` works
    for (const [name, content] of Object.entries(msg.files || {})) {
      py.FS.writeFile(`/home/pyodide/${name}`, content, { encoding: "utf8" });
    }

    await ensurePackages(py, msg.code);

    const t0 = performance.now();
    const rc = await py.runPythonAsync(
      `__pg_run(${JSON.stringify(msg.code)}, ${JSON.stringify(msg.stdin || "")})`
    );
    post("done", { rc, ms: Math.round(performance.now() - t0) });
  } catch (e) {
    post("stderr", { text: String(e && e.message || e) + "\n" });
    post("done", { rc: 1, ms: 0 });
  }
};
