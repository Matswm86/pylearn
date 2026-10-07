/* ===== Block Bench step-through worker =====
   Runs a snippet under sys.settrace inside Pyodide and returns one snapshot per
   executed line: the line number, every frame's variables and the output so far.
   Runs in a Web Worker so the page can terminate a runaway loop. */

const PYODIDE_VERSION = "0.26.4";
let pyodide = null;

const TRACER = `
import sys, io, os, json, types, tempfile, traceback

MAX_STEPS = 400

def _fmt(v):
    if isinstance(v, types.ModuleType):
        return "module " + v.__name__, "module"
    if isinstance(v, type):
        return "class " + v.__name__, "class"
    if isinstance(v, types.FunctionType):
        if v.__name__ == "<lambda>":
            return "lambda", "function"
        n = v.__code__.co_argcount
        return "function " + v.__name__ + "(" + ", ".join(v.__code__.co_varnames[:n]) + ")", "function"
    if isinstance(v, io.IOBase):
        name = getattr(v, "name", "?")
        mode = getattr(v, "mode", "")
        state = "closed" if v.closed else "open"
        return f"file {name!r} mode {mode!r}, {state}", "file"
    cls = type(v)
    if cls.__module__ == "__main__" and hasattr(v, "__dict__"):
        inner = ", ".join(f"{k}={_short(x)}" for k, x in vars(v).items())
        return f"{cls.__name__}({inner})", cls.__name__
    return _short(v), cls.__name__

def _short(v):
    try:
        r = repr(v)
    except Exception:
        r = "<?>"
    return r if len(r) <= 90 else r[:87] + "..."

def _is_class_body(frame):
    loc = frame.f_locals
    return "__module__" in loc and "__qualname__" in loc


def _frames(frame):
    chain = []
    f = frame
    while f is not None and f.f_code.co_filename == "main.py":
        chain.append(f)
        f = f.f_back
    chain.reverse()
    out = []
    for fr in chain:
        name = fr.f_code.co_name
        if name == "<module>":
            title, src = "Global variables", fr.f_globals
        elif _is_class_body(fr):
            title, src = "class " + name + " (being built)", fr.f_locals
        else:
            title, src = name + "()", fr.f_locals
        rows = []
        for k, v in list(src.items()):
            if k.startswith("__") or k.startswith("_tb_"):
                continue
            val, typ = _fmt(v)
            rows.append([k, val, typ])
        out.append({"title": title, "vars": rows})
    return out

def _run(src, files_json):
    files = json.loads(files_json)
    work = tempfile.mkdtemp()
    os.chdir(work)
    for fname, text in files.items():
        with open(fname, "w", encoding="utf-8") as fh:
            fh.write(text)
    steps = []
    buf = io.StringIO()
    real_out = sys.stdout
    error = None

    class _Stop(Exception):
        pass

    def snap(frame, event, extra=None):
        steps.append({"line": frame.f_lineno, "event": event, "fn": frame.f_code.co_name,
                      "extra": extra, "frames": _frames(frame), "out": buf.getvalue()})

    def tracer(frame, event, arg):
        if frame.f_code.co_filename != "main.py":
            return None
        if len(steps) >= MAX_STEPS:
            raise _Stop()
        if event == "line":
            snap(frame, "line")
        elif event == "return" and frame.f_code.co_name != "<module>" and not _is_class_body(frame):
            snap(frame, "return", _fmt(arg)[0])
        return tracer

    g = {"__name__": "__main__", "__builtins__": __builtins__}
    try:
        code = compile(src, "main.py", "exec")
    except SyntaxError as e:
        return json.dumps({"steps": [], "error": f"{type(e).__name__} on line {e.lineno}: {e.msg}", "errline": e.lineno})
    sys.stdout = buf
    sys.settrace(tracer)
    errline = None
    try:
        exec(code, g)
    except _Stop:
        error = f"Stopped after {MAX_STEPS} steps. A loop that never ends looks like this."
    except BaseException as e:
        tb = e.__traceback__
        while tb is not None:
            if tb.tb_frame.f_code.co_filename == "main.py":
                errline = tb.tb_lineno
            tb = tb.tb_next
        error = f"{type(e).__name__}: {e}"
    finally:
        sys.settrace(None)
        sys.stdout = real_out
    return json.dumps({"steps": steps, "out": buf.getvalue(), "error": error, "errline": errline})
`;

async function ensure() {
  if (pyodide) return pyodide;
  self.postMessage({ type: "status", text: "Loading Python in your browser (first time takes about 10 seconds)..." });
  self.importScripts(`https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js`);
  pyodide = await loadPyodide({ indexURL: `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/` });
  pyodide.runPython(TRACER);
  return pyodide;
}

self.onmessage = async (e) => {
  const { src, files } = e.data;
  try {
    const py = await ensure();
    self.postMessage({ type: "status", text: "Running..." });
    py.globals.set("_src", src);
    py.globals.set("_files", JSON.stringify(files || {}));
    const res = py.runPython("_run(_src, _files)");
    self.postMessage({ type: "result", data: JSON.parse(res) });
  } catch (err) {
    self.postMessage({ type: "fail", text: String(err) });
  }
};
