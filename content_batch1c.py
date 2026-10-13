#!/usr/bin/env python3
"""Batch 1c: wave-3 drills for the last 5 thin AQA maths foundation topics.
Run: python3 content_batch1c.py"""
from expand_topics import run_wave3

DR = lambda body: (
    '<section class="section">\n'
    '<h2>⚡ Targeted Drills</h2>\n'
    '<p>Thirty-second checks — cover the answers, work each one, then mark yourself. '
    'If any takes longer than a minute, revisit the matching section above.</p>\n' + body + '\n</section>')

BATCH = {}

BATCH["N7-integer-indices.html"] = dict(drills=DR('<ul>'
    '<li>Simplify: c⁵ × c⁴ &nbsp;→&nbsp; c⁹ &nbsp;·&nbsp; d⁸ ÷ d³ &nbsp;→&nbsp; d⁵ &nbsp;·&nbsp; (g²)⁴ &nbsp;→&nbsp; g⁸</li>'
    '<li>True or false: 2³ × 2⁴ = 4⁷? &nbsp;→&nbsp; FALSE — bases must be the same single base; 2³ × 2⁴ = 2⁷</li>'
    '<li>Write with a positive index: 3⁻² &nbsp;→&nbsp; 1/9 &nbsp;·&nbsp; 10⁻³ &nbsp;→&nbsp; 1/1000</li>'
    '<li>Simplify: 4p³ × 5p² &nbsp;→&nbsp; 20p⁵ (multiply coefficients, add indices)</li>'
    '<li>Spot the error: (a³)² = a⁵ &nbsp;→&nbsp; WRONG — multiply the indices: a⁶</li>'
    '</ul>'))

BATCH["N1-ordering-numbers.html"] = dict(drills=DR('<ul>'
    '<li>Order: −6, −6.5, 6, −0.6 &nbsp;→&nbsp; −6.5, −6, −0.6, 6</li>'
    '<li>Fill in the symbol: −3 __ −7 &nbsp;→&nbsp; > (−3 is closer to zero)</li>'
    '<li>Order: 3/4, 0.72, 7/10, 0.075 &nbsp;→&nbsp; 0.075, 7/10, 0.72, 3/4</li>'
    '<li>Which is smaller: −0.09 or −0.1? &nbsp;→&nbsp; −0.1 (further from zero)</li>'
    '<li>Convert then order: 2/5, 0.45, 9/20 &nbsp;→&nbsp; 0.4, 0.45, 0.45 = 9/20 — 2/5 < 0.45 = 9/20</li>'
    '</ul>'))

BATCH["A22-inequalities.html"] = dict(drills=DR('<ul>'
    '<li>Solve: x + 4 < 9 &nbsp;→&nbsp; x < 5</li>'
    '<li>Solve: 3x > 18 &nbsp;→&nbsp; x > 6</li>'
    '<li>Solve: −2x ≥ 10 &nbsp;→&nbsp; x ≤ −5 (flip!)</li>'
    '<li>Circle type for x ≥ 2: &nbsp;→&nbsp; filled (closed) circle at 2</li>'
    '<li>List integers in −4 < x < −1: &nbsp;→&nbsp; −3, −2</li>'
    '</ul>'))

BATCH["N6-powers-and-roots.html"] = dict(drills=DR('<ul>'
    '<li>12² &nbsp;→&nbsp; 144 &nbsp;·&nbsp; 13² &nbsp;→&nbsp; 169 &nbsp;·&nbsp; 4³ &nbsp;→&nbsp; 64</li>'
    '<li>√144 &nbsp;→&nbsp; 12 &nbsp;·&nbsp; ³√64 &nbsp;→&nbsp; 4 &nbsp;·&nbsp; √400 &nbsp;→&nbsp; 20</li>'
    '<li>Between which two square numbers does √70 sit? &nbsp;→&nbsp; 64 (8²) and 81 (9²), so ≈ 8.4</li>'
    '<li>10⁵ &nbsp;→&nbsp; 100,000 &nbsp;·&nbsp; 2⁶ &nbsp;→&nbsp; 64</li>'
    '<li>A square has area 196 cm². Perimeter? &nbsp;→&nbsp; side √196 = 14, perimeter 4 × 14 = 56 cm</li>'
    '</ul>'))

BATCH["G21-exact-trig-values.html"] = dict(drills=DR('<ul>'
    '<li>sin 30° &nbsp;→&nbsp; 1/2 &nbsp;·&nbsp; sin 45° &nbsp;→&nbsp; √2/2 &nbsp;·&nbsp; sin 90° &nbsp;→&nbsp; 1</li>'
    '<li>cos 60° &nbsp;→&nbsp; 1/2 &nbsp;·&nbsp; cos 45° &nbsp;→&nbsp; √2/2 &nbsp;·&nbsp; cos 90° &nbsp;→&nbsp; 0</li>'
    '<li>tan 30° &nbsp;→&nbsp; 1/√3 &nbsp;·&nbsp; tan 45° &nbsp;→&nbsp; 1 &nbsp;·&nbsp; tan 60° &nbsp;→&nbsp; √3</li>'
    '<li>sin 30° + cos 60° &nbsp;→&nbsp; 1/2 + 1/2 = 1</li>'
    '<li>Hypotenuse 4 cm, angle 60°: exact opposite side? &nbsp;→&nbsp; 4 × √3/2 = 2√3 cm</li>'
    '</ul>'))

if __name__ == "__main__":
    run_wave3(BATCH)
