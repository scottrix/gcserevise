#!/usr/bin/env python3
"""Shared section builders for topic expansion batches."""
from expand_topics import (apply, apply_wave2, apply_wave3, insert_before_section,
                           insert_after_marker_section)

W_SEC = lambda title, body: (
    '<section class="section">\n'
    '<h2>🧮 Worked Examples — Exam Style</h2>\n'
    f'<p>{title}</p>\n{body}\n</section>')
EX = lambda q, steps, marks: (
    '<div class="example">\n'
    f'<p><strong>{q}</strong></p>\n{steps}\n'
    f'<p><em>{marks}</em></p>\n</div>')
SOL_HEAD = (
    '<section class="section">\n'
    '<h2>📋 Model Answers — Full Working</h2>\n'
    '<p>Every mark comes from the working, not just the answer. '
    'These model answers show the lines a mark scheme expects to see.</p>\n'
    '<div class="example">')
KF = lambda body: (
    '<section class="section">\n'
    '<h2>📌 Key Facts to Memorise</h2>\n' + body + '\n</section>')
CTX = lambda body: (
    '<section class="section">\n'
    '<h2>🗺️ In the Exam</h2>\n' + body + '\n</section>')
W2 = lambda q, steps, marks: (
    '<section class="section">\n'
    '<h2>🧮 Worked Examples — Harder Exam Style</h2>\n'
    '<div class="example">\n'
    f'<p><strong>{q}</strong></p>\n{steps}\n'
    f'<p><em>{marks}</em></p>\n</div>\n</section>')
DR = lambda body: (
    '<section class="section">\n'
    '<h2>⚡ Targeted Drills</h2>\n'
    '<p>Cover the answers, work each one, then mark yourself. '
    'If any takes over a minute, revisit the matching section above.</p>\n' + body + '\n</section>')

ROOT = "topics/mathematics/aqa/foundation"


def run(batch, root=ROOT):
    for fname, payload in batch.items():
        path = f"{root}/{fname}"
        did = apply(path, payload)
        print(f"{fname}: {'+'.join(did) if did else 'SKIP'}")


def run2(batch, root=ROOT):
    for fname, payload in batch.items():
        path = f"{root}/{fname}"
        did = apply_wave2(path, payload)
        print(f"{fname}: {','.join(did) if did else 'SKIP'}")
