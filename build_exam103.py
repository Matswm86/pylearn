#!/usr/bin/env python3
"""Regenerate docs/exam103.js, the Pytor site's AI-103 drill, from PyQuest tier 10.

The tier file is the single source of truth for the questions:

    pyquest/app/src/main/assets/curriculum/tier_10.json

Edit that file (and run pyquest/tools/validate_curriculum.py), then run this script.
Never hand-edit docs/exam103.js.

Levels 1 to 5 were written for this project. Questions tagged notes-rk were written for this
project from Rishab Kumar's AI-103 notes, used with permission. Every other later question is
adapted from the MIT-licensed open-source AI-103 practice exam (see THIRD_PARTY_NOTICES.md).
The page credits each source in the hero, in each section note, and in the Learn link on each
question.

Usage:
    python3 build_exam103.py [--tier path/to/tier_10.json] [--out path/to/exam103.js]
"""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TIER = ROOT / "pyquest/app/src/main/assets/curriculum/tier_10.json"
OUT = ROOT / "docs/exam103.js"

# Levels 1-5 are the questions written for this site. Later levels are adapted.
ORIGINAL_LEVELS = 5
SOURCE_REPO = "https://github.com/sefstratiou-ai/ai-103-practice-exam"
NOTICES_URL = "https://github.com/Matswm86/pylearn/blob/main/THIRD_PARTY_NOTICES.md"
STUDY_GUIDE = [
    "AI-103 study guide (skills measured)",
    "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103",
]
ORIGINAL_NOTE = "Written for this site from the official skills list."
ADAPTED_NOTE = f"Adapted from the MIT-licensed AI-103 practice exam at {SOURCE_REPO}."
NOTES_TAG = "notes-rk"
NOTES_URL = "https://rishabkumar.com/notes/azure-ai-apps-and-agents-developer-associate/"
NOTES_NOTE = (
    f"Written for this site from Rishab Kumar's AI-103 notes, used with permission: {NOTES_URL}"
)
LEARN_LINE = re.compile(r"Microsoft Learn: (?P<label>.+?), (?P<url>https://\S+)$")
CASE_NAME = re.compile(r"^Case study, ([^.(]+?)[.(]")


def site_item(q: dict, n: int, ref: int) -> dict:
    item = {"n": n, "q": q["prompt"], "explain": q["explain"], "ref": ref}
    if q.get("code"):
        item["code"] = q["code"]
    kind = q["type"]
    if kind == "mcq":
        opts = list(q["options"])
        random.Random(q["id"]).shuffle(opts)
        item.update(type="single", options=opts, correct=opts.index(q["answer"][0]))
    elif kind == "multi":
        opts = list(q["options"])
        item.update(
            type="multi",
            options=opts,
            pick=len(q["answer"]),
            correct=[opts.index(a) for a in q["answer"]],
        )
    elif kind == "order":
        item.update(type="order", steps=q["answer"])
        if q.get("accept"):
            item["accept"] = q["accept"]
    elif kind == "match":
        item.update(
            type="match",
            choices=q["options"],
            rows=[[row, answer] for row, answer in zip(q["rows"], q["answer"])],
        )
        if q.get("mono"):
            item["mono"] = True
    else:
        raise ValueError(f"{q['id']}: type {kind!r} has no site format")
    return item


def split_into_sections(
    level: int, title: str, questions: list[dict]
) -> list[tuple[str, str, list[dict]]]:
    """One section per level, or one per case study when a level groups several."""
    cases = list(dict.fromkeys(q.get("case") for q in questions))
    if len(cases) <= 1:
        return [(f"a{level}", title, questions)]
    sections = []
    for index, case in enumerate(cases):
        group = [q for q in questions if q.get("case") == case]
        match = CASE_NAME.match(group[0]["prompt"])
        name = match.group(1) if match else f"part {index + 1}"
        sections.append((f"a{level}{chr(ord('a') + index)}", f"Case study: {name}", group))
    return sections


def source_of(q: dict) -> str:
    """original, notes or adapted: who the question's content comes from."""
    if NOTES_TAG in q.get("tags", []):
        return "notes"
    return "original" if q["level"] <= ORIGINAL_LEVELS else "adapted"


def section_note(source: str, case: str | None) -> str:
    credit = {"original": ORIGINAL_NOTE, "notes": NOTES_NOTE, "adapted": ADAPTED_NOTE}[source]
    if case:
        text = f"Case study. {case}"
        return text if source == "original" else f"{text}\n\n{credit}"
    return credit


def build(tier_path: Path) -> tuple[str, int]:
    tier = json.loads(tier_path.read_text(encoding="utf-8"))
    by_level: dict[int, list[dict]] = {}
    for q in tier["questions"]:
        by_level.setdefault(q["level"], []).append(q)

    refs = [STUDY_GUIDE]
    ref_index = {STUDY_GUIDE[1]: 1}
    sections, n = [], 0
    for level in sorted(by_level):
        lesson = (
            tier["lessons"][level - 1] if level - 1 < len(tier["lessons"]) else f"Level {level}"
        )
        title = lesson[:1].upper() + lesson[1:]
        for section_id, section_title, group in split_into_sections(level, title, by_level[level]):
            items = []
            for q in group:
                n += 1
                ref = 1
                learn = LEARN_LINE.search(q.get("deep", "")) if level > ORIGINAL_LEVELS else None
                if learn:
                    url = learn.group("url")
                    if url not in ref_index:
                        refs.append([learn.group("label"), url])
                        ref_index[url] = len(refs)
                    ref = ref_index[url]
                items.append(site_item(q, n, ref))
            case = next((q["case"] for q in group if q.get("case")), None)
            sections.append(
                {
                    "id": section_id,
                    "title": section_title,
                    "weight": f"{len(items)} questions",
                    "note": section_note(source_of(group[0]), case),
                    "questions": items,
                }
            )

    sources = [source_of(q) for q in tier["questions"]]
    original, from_notes = sources.count("original"), sources.count("notes")
    adapted = sources.count("adapted")
    case_studies = len({q["case"] for q in tier["questions"] if q.get("case")})
    js = f"""/* ===== AI-103 exam drill: {n} questions =====
 *
 * Generated from the PyQuest tier 10 bank (pyquest/app/src/main/assets/curriculum/tier_10.json)
 * by build_exam103.py at the repository root; edit the tier file and regenerate rather than
 * editing here. Scope follows the official AI-103 study guide. Answers live in localStorage
 * under pylearn_exam103, separate from the AI-901 drill.
 *
 * Credit: {original} questions were written for this site, {from_notes} were written for this site
 * from Rishab Kumar's AI-103 notes ({NOTES_URL}, used with permission), and {adapted} are adapted
 * from {SOURCE_REPO} (MIT licence, see THIRD_PARTY_NOTICES.md).
 */

const EXAM103_REFS = {json.dumps(refs, indent=2, ensure_ascii=False)};

const EXAM103_SECTIONS = {json.dumps(sections, indent=2, ensure_ascii=False)};

function renderExam103Hero() {{
  return `
    <div class="path-hero">
      <h1>&#127891; AI-103 drill</h1>
      <p>{n} questions for the Azure AI Apps and Agents Developer Associate exam: single answer, select-N, matching and ordering, with Python SDK code to read and {case_studies} case studies. The weight follows the official skills list, with extra depth where people who sat the exam report Microsoft goes deep: Azure AI Search and RAG, Foundry agents and tools, keyless security, content safety, and Content Understanding against Document Intelligence.</p>
      <p class="path-note">Credit: the first {original} questions were written for this site from the official skills list. The last {from_notes}, the stem-to-answer and traps drills, were written for this site from <a href="{NOTES_URL}" target="_blank" rel="noopener">Rishab Kumar's AI-103 notes</a>, used with permission. The other {adapted} are adapted from the open-source <a href="{SOURCE_REPO}" target="_blank" rel="noopener">AI-103 practice exam by sefstratiou-ai</a> (MIT licence), whose authors describe their questions as original and based on public Microsoft documentation. We regrouped them into sections and reshuffled the answer options. The copyright notice and licence text are in <a href="{NOTICES_URL}" target="_blank" rel="noopener">THIRD_PARTY_NOTICES.md</a>. Treat this as a drill, not a mock exam: the official Practice Assessment is still the bar before you book.</p>
    </div>
  `;
}}

EXAM_BANKS["103"] = {{
  key: "pylearn_exam103", prefix: "y", sections: EXAM103_SECTIONS, refs: EXAM103_REFS,
  name: "AI-103", hero: renderExam103Hero,
}};
"""
    return js, n


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tier", type=Path, default=TIER)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()
    js, total = build(args.tier)
    args.out.write_text(js, encoding="utf-8")
    print(f"wrote {args.out} with {total} questions")


if __name__ == "__main__":
    main()
