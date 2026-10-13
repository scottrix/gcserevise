#!/usr/bin/env python3
"""Merge authored expansion content into maths topic pages (additive only).

Per-topic payload keys:
  worked:      str  — HTML of a "Worked Examples — Exam Style" section,
                    inserted immediately BEFORE the Practice Questions section.
  questions:   list — extra question HTML strings (inner HTML of a
                    <div class="question">), appended inside .practice-questions.
  solutions:   str  — HTML of a "Model Answers — Full Working" section,
                    inserted immediately AFTER the Answers section.

Idempotent: skips topics whose content is already present (marker check).
"""
import re
import sys


def insert_worked(html, worked_html):
    m = re.search(r'<section class="section">\s*<h2>❓ Practice Questions</h2>', html)
    if not m:
        return html, False
    return html[:m.start()] + worked_html + "\n\n" + html[m.start():], True


def append_questions(html, questions):
    m = re.search(r'(<h2>❓ Practice Questions</h2>\s*<div class="practice-questions">)(.*?)(\n</div>\s*</section>)', html, re.DOTALL)
    if not m:
        return html, False
    extra = "".join(f'\n<div class="question">\n<p>{q}</p>\n</div>' for q in questions)
    return html[:m.end(2)] + extra + html[m.end(2):], True


def insert_solutions(html, solutions_html):
    m = re.search(r'<h2>✅ Answers</h2>.*?</section>', html, re.DOTALL)
    if not m:
        return html, False
    return html[:m.end()] + "\n\n" + solutions_html + html[m.end():], True


def apply(path, payload):
    html = open(path, encoding="utf-8").read()
    changed = []
    for old, new in payload.get("corrections", []):
        if new in html and old not in html:
            continue
        if old not in html:
            print(f"  WARN correction target missing: {old[:40]}")
            continue
        html = html.replace(old, new, 1)
        changed.append("correct")
    if payload.get("worked") and 'Worked Examples — Exam Style' not in html:
        html, ok = insert_worked(html, payload["worked"])
        changed += ["worked"] if ok else []
    if payload.get("questions") and payload.get("marker") and payload["marker"] not in html:
        html, ok = append_questions(html, payload["questions"])
        changed += ["questions"] if ok else []
    if payload.get("solutions") and 'Model Answers — Full Working' not in html:
        html, ok = insert_solutions(html, payload["solutions"])
        changed += ["solutions"] if ok else []
    if changed:
        open(path, "w", encoding="utf-8").write(html)
    return changed


def run(batch, root="topics/mathematics/aqa/foundation"):
    for fname, payload in batch.items():
        path = f"{root}/{fname}"
        did = apply(path, payload)
        print(f"{fname}: {'+'.join(did) if did else 'SKIP (already applied)'}")


def insert_before_section(html, h2_text, new_html):
    """Insert new_html before the <section> whose <h2> starts with h2_text."""
    m = re.search(r'<section class="section">\s*<h2>[^<]*' + re.escape(h2_text), html)
    if not m:
        return html, False
    return html[:m.start()] + new_html + "\n\n" + html[m.start():], True


def insert_after_marker_section(html, h2_text, new_html):
    m = re.search(r'<h2>[^<]*' + re.escape(h2_text) + r'</h2>.*?</section>', html, re.DOTALL)
    if not m:
        return html, False
    return html[:m.end()] + "\n\n" + new_html + html[m.end():], True


def apply_wave2(path, payload):
    html = open(path, encoding="utf-8").read()
    changed = []
    kf = payload.get("keyfacts")
    if kf and '📌 Key Facts to Memorise' not in html:
        html, ok = insert_before_section(html, "🎯 Exam Tips", kf)
        changed += ["keyfacts"] if ok else ["keyfacts-NOANCHOR"]
    ctx = payload.get("context")
    if ctx and '🗺️ In the Exam' not in html:
        html, ok = insert_before_section(html, "🎯 Exam Tips", ctx)
        changed += ["context"] if ok else ["context-NOANCHOR"]
    w2 = payload.get("worked2")
    if w2 and 'Worked Examples — Harder Exam Style' not in html:
        html, ok = insert_after_marker_section(html, "✅ Answers", w2)
        changed += ["worked2"] if ok else ["worked2-NOANCHOR"]
    if changed:
        open(path, "w", encoding="utf-8").write(html)
    return changed


def run_wave2(batch, root="topics/mathematics/aqa/foundation"):
    for fname, payload in batch.items():
        path = f"{root}/{fname}"
        did = apply_wave2(path, payload)
        print(f"{fname}: {','.join(did) if did else 'SKIP'}")


def insert_before_section(html, h2_text, new_html):
    m = re.search(r'<section class="section">\s*<h2>[^<]*' + re.escape(h2_text), html)
    if not m:
        return html, False
    return html[:m.start()] + new_html + "\n\n" + html[m.start():], True


def apply_wave3(path, payload):
    html = open(path, encoding="utf-8").read()
    changed = []
    dr = payload.get("drills")
    if dr and '⚡ Targeted Drills' not in html:
        html, ok = insert_before_section(html, "🎯 Exam Tips", dr)
        changed += ["drills"] if ok else ["drills-NOANCHOR"]
    if changed:
        open(path, "w", encoding="utf-8").write(html)
    return changed


def run_wave3(batch, root="topics/mathematics/aqa/foundation"):
    for fname, payload in batch.items():
        path = f"{root}/{fname}"
        did = apply_wave3(path, payload)
        print(f"{fname}: {','.join(did) if did else 'SKIP'}")
