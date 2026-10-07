"""Run every Python Block Bench solution and compare its stdout with the puzzle's expected output.

The puzzles live as a JS array in docs/blocks/index.html. Node extracts them as JSON,
this test assembles each solution exactly the way the page's step-through does, runs it
with python3 in a temp dir (with any `files` the puzzle provides), and checks the output.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

HTML = Path(__file__).resolve().parent.parent / "docs" / "blocks" / "index.html"
NO_RUN_IMPORTS = ("requests", "openai", "pandas")

EXTRACT_JS = r"""
const fs = require('fs');
const src = fs.readFileSync(process.argv[1], 'utf8');
const start = src.indexOf('const SECTIONS = [');
const end = src.indexOf('\n];', start);
const SECTIONS = eval(src.slice(start + 'const SECTIONS = '.length, end + 2));
process.stdout.write(JSON.stringify(SECTIONS));
"""


def load_sections():
    out = subprocess.run(
        ["node", "-e", EXTRACT_JS, str(HTML)], capture_output=True, text=True, check=True
    )
    return json.loads(out.stdout)


def solution_source(ex):
    if ex["t"] == "fill":
        answers = iter(a[0] for a in ex["ans"])
        lines = []
        for line in ex["code"]:
            parts = line.split("___")
            built = parts[0]
            for p in parts[1:]:
                built += next(answers) + p
            lines.append(built)
        return "\n".join(lines)
    if ex["t"] == "order":
        return "\n".join("    " * ind + code for code, ind in ex["lines"])
    if ex["t"] == "label":
        import re

        return re.sub(r"\[\[\w+\|([^\]]+)\]\]", r"\1", ex["code"])
    raise ValueError(ex["t"])


def runnable(ex, src):
    if ex.get("norun") or "out" not in ex:
        return False
    if src.lstrip().startswith("pip "):
        return False
    return not any(
        f"import {m}" in src or f"from {m} " in src or f"{m}." in src for m in NO_RUN_IMPORTS
    )


CASES = [
    pytest.param(sec["id"], i, ex, id=f"{sec['id']}-{i}")
    for sec in load_sections()
    for i, ex in enumerate(sec["ex"])
]


def run(src, files):
    with tempfile.TemporaryDirectory() as tmp:
        for name, text in (files or {}).items():
            Path(tmp, name).write_text(text, encoding="utf-8")
        res = subprocess.run(
            [sys.executable, "-I", "-c", src],
            cwd=tmp,
            capture_output=True,
            text=True,
            timeout=10,
        )
    return res


@pytest.mark.parametrize("sec_id,idx,ex", CASES)
def test_solution_prints_expected_output(sec_id, idx, ex):
    src = solution_source(ex)
    if not runnable(ex, src):
        pytest.skip("needs network, a third-party package or the terminal")
    res = run(src, ex.get("files"))
    assert res.returncode == 0, res.stderr
    assert res.stdout.rstrip("\n") == ex["out"], src


@pytest.mark.parametrize("sec_id,idx,ex", CASES)
def test_worked_example_prints_its_output(sec_id, idx, ex):
    if not ex.get("ex") or not ex["ex"][1]:
        pytest.skip("no worked example output")
    src, want = ex["ex"]
    if not runnable(ex, src):
        pytest.skip("needs network, a third-party package or the terminal")
    res = run(src, ex.get("files"))
    assert res.returncode == 0, res.stderr
    assert res.stdout.rstrip("\n") == want, src


@pytest.mark.parametrize("sec_id,idx,ex", CASES)
def test_fill_has_distinct_answer_and_extra_blocks(sec_id, idx, ex):
    if ex["t"] != "fill":
        pytest.skip("not a fill puzzle")
    gaps = sum(line.count("___") for line in ex["code"])
    assert gaps == len(ex["ans"])
    firsts = [a[0] for a in ex["ans"]]
    assert not set(firsts) & set(ex["extra"]), "an extra block equals a correct answer"


WORKER = HTML.parent / "trace-worker.js"


def load_tracer():
    js = WORKER.read_text(encoding="utf-8")
    start = js.index("const TRACER = `") + len("const TRACER = `")
    end = js.index("`;", start)
    ns = {}
    exec(js[start:end], ns)
    return ns["_run"]


@pytest.mark.parametrize("sec_id,idx,ex", CASES)
def test_step_through_reaches_expected_output(sec_id, idx, ex):
    src = solution_source(ex)
    if not runnable(ex, src):
        pytest.skip("needs network, a third-party package or the terminal")
    import os

    here = os.getcwd()
    try:
        res = json.loads(load_tracer()(src, json.dumps(ex.get("files") or {})))
    finally:
        os.chdir(here)
    assert res["error"] is None, res["error"]
    assert res["out"].rstrip("\n") == ex["out"]
    assert res["steps"], "no steps recorded"
    assert all(s["line"] >= 1 for s in res["steps"])
