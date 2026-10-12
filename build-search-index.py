#!/usr/bin/env python3
"""Build search-index.json by walking topics/{subject}/{board}/ HTML files.

Entry shape (consumed by app.js client-side search):
  id          filename stem, e.g. "ah1-greek-city-states"
  name        <h1> text, falling back to <title> minus the site suffix
  strandId    ""  (reserved; per-strand grouping not in the path)
  strandName  ""
  url         repo-relative path, e.g. "topics/ancient-history/ocr/ah1-....html"
  subject     subject dir name, e.g. "ancient-history"
  subjectName display name from subjects.json
  category    from subjects.json
  board       board dir name (aqa/edexcel/ocr/eduqas/ccea) or ""
  tier        foundation/higher when present in the path, else ""

Idempotent output; sorted by url for stable diffs.
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TOPICS = os.path.join(ROOT, "topics")

H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
BOARDS = {"aqa", "edexcel", "ocr", "eduqas", "ccea", "wjec", "ocra", "ocrb"}
TIERS = {"foundation", "higher"}


def page_name(path):
    src = open(path, encoding="utf-8", errors="replace").read()
    m = H1_RE.search(src)
    if m:
        text = TAG_RE.sub("", m.group(1))
        text = html.unescape(text).strip()
        if text:
            return re.sub(r"\s+", " ", text)
    t = re.search(r"<title>(.*?)</title>", src, re.DOTALL)
    if t:
        title = html.unescape(t.group(1)).strip()
        title = re.sub(r"\s*-\s*GCSE Revise\s*$", "", title)
        return title
    return ""


def main():
    subjects = {s["id"]: s for s in json.load(
        open(os.path.join(ROOT, "subjects.json"), encoding="utf-8"))["subjects"]}

    topics = []
    for dirpath, _dirnames, filenames in os.walk(TOPICS):
        rel_dir = os.path.relpath(dirpath, TOPICS)
        parts = rel_dir.split(os.sep)
        subject = parts[0] if parts[0] != "." else ""
        board = parts[1] if len(parts) > 1 and parts[1] in BOARDS else ""
        tier = parts[2] if len(parts) > 2 and parts[2] in TIERS else (
            parts[1] if len(parts) > 1 and parts[1] in TIERS else "")
        meta = subjects.get(subject, {})
        for fn in sorted(filenames):
            if not fn.endswith(".html") or fn == "index.html":
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), ROOT).replace(os.sep, "/")
            stem = fn[:-5]
            name = page_name(os.path.join(dirpath, fn))
            search = " ".join(p for p in [
                stem, name, meta.get("name", ""), board, tier] if p).lower()
            topics.append({
                "id": stem,
                "name": name,
                "strandId": "",
                "strandName": "",
                "url": rel,
                "subject": subject,
                "subjectName": meta.get("name", ""),
                "category": meta.get("category", ""),
                "board": board,
                "tier": tier,
                "searchText": search,
            })

    topics.sort(key=lambda t: t["url"])
    subjects_out = []
    for sid, s in subjects.items():
        subjects_out.append({
            "id": sid,
            "name": s["name"],
            "category": s.get("category", ""),
            "papers": s.get("papers", 0),
            "boards": s.get("boards", []),
            "aliases": s.get("aliases", []),
            "url": f"{sid}.html",
        })
    subjects_out.sort(key=lambda s: s["id"])

    out = os.path.join(ROOT, "search-index.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"subjects": subjects_out, "topics": topics},
                  f, ensure_ascii=False, separators=(",", ":"))
    print(f"Wrote {out}: {len(subjects_out)} subjects, {len(topics)} topics "
          f"({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
