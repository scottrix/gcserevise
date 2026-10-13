#!/usr/bin/env python3
"""Inject per-board 'Board Focus' boxes into topic pages of multi-board subjects,
and a composed 'Board Differences' section into the subject landing pages."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expand_topics import insert_before_section
from board_focus_subjects import SUB

ROOT = os.path.dirname(os.path.abspath(__file__))
BOARD_NAMES = {"aqa": "AQA", "edexcel": "Pearson Edexcel", "ocr": "OCR",
               "eduqas": "Eduqas", "ccea": "CCEA"}
MARKER = "🧭 Board Focus"


def box(board, html):
    return (f'<section class="section"><h2>{MARKER} — {BOARD_NAMES[board]}</h2>'
            f'<div class="board-diff">{html}'
            '<p class="key-point"><strong>Always check:</strong> specification details change — '
            'confirm paper structure and set texts against the current specification for your exam year.</p>'
            '</div></section>')


def insert_topic(subject, board, path, html_block):
    page = open(path, encoding="utf-8").read()
    if MARKER in page:
        return False
    b = box(board, html_block)
    for anchor in ("🎯 Exam Tips", "🎬 Video Resources", "Related"):
        page, ok = insert_before_section(page, anchor, b)
        if ok:
            open(path, "w", encoding="utf-8").write(page)
            return True
    # fallback: before </main>
    i = page.rfind("</main>")
    if i != -1:
        page = page[:i] + b + "\n" + page[i:]
        open(path, "w", encoding="utf-8").write(page)
        return True
    return False


def main():
    only = sys.argv[1:] or sorted(SUB)
    topics_done = 0
    subjects_done = 0
    for subject in only:
        boards = SUB.get(subject)
        if not boards:
            print(f"no data for {subject}")
            continue
        # topic pages
        for board, block in boards.items():
            tdir = os.path.join(ROOT, "topics", subject, board)
            if not os.path.isdir(tdir):
                continue
            for fn in sorted(os.listdir(tdir)):
                if not fn.endswith(".html"):
                    continue
                path = os.path.join(tdir, fn)
                try:
                    if "http-equiv=\"refresh\"" in open(path, encoding="utf-8", errors="replace").read(600):
                        continue
                except OSError:
                    continue
                if insert_topic(subject, board, path, block):
                    topics_done += 1
        # subject landing page
        spath = os.path.join(ROOT, f"{subject}.html")
        if os.path.exists(spath) and MARKER not in open(spath, encoding="utf-8").read():
            page = open(spath, encoding="utf-8").read()
            blocks = "".join(
                f'<h3>{BOARD_NAMES[b]}</h3>{block}'
                for b in ["aqa", "edexcel", "ocr", "eduqas", "ccea"] if b in boards)
            section = (f'<section id="{subject}-board-differences" class="section">'
                       f'<h2>🧭 Board Differences</h2><div class="board-diff">{blocks}</div></section>')
            i = page.find("</main>")
            if i != -1:
                page = page[:i] + section + "\n" + page[i:]
                open(spath, "w", encoding="utf-8").write(page)
                subjects_done += 1
    print(f"injected: {topics_done} topic boxes, {subjects_done} subject sections")


if __name__ == "__main__":
    main()
