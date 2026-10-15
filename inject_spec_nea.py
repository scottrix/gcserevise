#!/usr/bin/env python3
"""Inject spec-focus boxes (single-board subjects) and Coursework & NEA Guide sections."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expand_topics import insert_before_section
from spec_focus_single import SPEC
from nea_guides import NEA

ROOT = os.path.dirname(os.path.abspath(__file__))
BOARD_NAMES = {"aqa": "AQA", "edexcel": "Pearson Edexcel", "ocr": "OCR",
               "eduqas": "Eduqas", "ccea": "CCEA"}
NEA_TITLE = "🎯 Coursework & NEA Guide"


def inject_spec(subject, board, block):
    n = 0
    tdir = os.path.join(ROOT, "topics", subject, board)
    if not os.path.isdir(tdir):
        return 0
    section = (f'<section class="section"><h2>🧭 Spec Focus — {BOARD_NAMES[board]}</h2>'
               f'<div class="board-diff">{block}</div></section>')
    for fn in sorted(os.listdir(tdir)):
        if not fn.endswith(".html"):
            continue
        path = os.path.join(tdir, fn)
        h = open(path, encoding="utf-8", errors="replace").read()
        if "Spec Focus" in h or 'http-equiv="refresh"' in h[:600]:
            continue
        for anchor in ("🎯 Exam Tips", "🎬 Video Resources", "Related"):
            h2, ok = insert_before_section(h, anchor, section)
            if ok:
                open(path, "w", encoding="utf-8").write(h2)
                n += 1
                break
        else:
            i = h.rfind("</main>")
            if i != -1:
                open(path, "w", encoding="utf-8").write(h[:i] + section + "\n" + h[i:])
                n += 1
    # subject page
    spath = os.path.join(ROOT, f"{subject}.html")
    if os.path.exists(spath) and "Spec Focus" not in open(spath, encoding="utf-8").read():
        page = open(spath, encoding="utf-8").read()
        i = page.find("</main>")
        if i != -1:
            big = (f'<section id="{subject}-spec" class="section"><h2>🧭 Exam Board & Specification</h2>'
                   f'<div class="board-diff">{block}</div></section>')
            open(spath, "w", encoding="utf-8").write(page[:i] + big + "\n" + page[i:])
    return n


def inject_nea(subject, block):
    spath = os.path.join(ROOT, f"{subject}.html")
    if not os.path.exists(spath):
        return False
    page = open(spath, encoding="utf-8").read()
    if NEA_TITLE in page:
        return False
    section = (f'<section id="{subject}-nea" class="section"><h2>{NEA_TITLE}</h2>'
               f'<div class="board-diff">{block}</div></section>')
    i = page.find("</main>")
    if i == -1:
        return False
    open(spath, "w", encoding="utf-8").write(page[:i] + section + "\n" + page[i:])
    return True


def main():
    only = sys.argv[1:] or sorted(set(list(SPEC) + list(NEA)))
    boxes = 0
    nea = 0
    for subject in only:
        if subject in SPEC:
            for board, block in SPEC[subject].items():
                boxes += inject_spec(subject, board, block)
        if subject in NEA:
            if inject_nea(subject, NEA[subject]):
                nea += 1
    print(f"spec boxes: {boxes} topic pages | NEA guides: {nea} subject pages")


if __name__ == "__main__":
    main()
