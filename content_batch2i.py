#!/usr/bin/env python3
"""Batch 2i: S5, S6, G25, S4 (final four) + any straggler check."""
from content_waves import W_SEC, EX, SOL_HEAD, KF, CTX, W2, run, run2

B = {}

B["S5-describing-populations.html"] = dict(
    marker="Q6: Two delivery firms: A mean 32 min, range 18 min; B mean 34 min, range 8 min. Which firm is more CONSISTENT, and which is faster on average?",
    worked=W_SEC("Describing and comparing: report a suitable AVERAGE (mean/median/mode) AND a suitable SPREAD (range/IQR), then interpret both in context.",
        EX("Compare: Class A mean 62%, range 40; Class B mean 58%, range 12.",
            '<p>A scores higher on average (62 > 58); B is more consistent (range 12 vs 40 — results '
            'less spread out).</p>',
            "B1 for the average comparison, B1 for the spread comparison. BOTH sentences are needed — 'compare' always means two.")
        + EX("Should a report on house prices use the mean or median? Why?",
            '<p><strong>Median</strong> — a few very expensive houses pull the mean up, so the median '
            'better represents a typical price.</p>',
            "B1 with the reason (outliers skew the mean). Median for skewed data, mean for symmetric data."))
    + '<p><strong>Exam wording to expect:</strong> "compare the distributions", "which average is most appropriate?", "make two comparisons".</p>',
    questions=["Q6: Two delivery firms: A mean 32 min, range 18 min; B mean 34 min, range 8 min. Which is more consistent, and which is faster on average?", "Q7: Data has mean 20, median 12. Describe the skew and give a possible cause."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Mean 45 > median 38 → <strong>positive (right) skew</strong> — a few high values pull the mean up</p>'
        '<p><strong>Q2.</strong> <strong>2 pets is the most common</strong> — the modal household</p>'
        '<p><strong>Q3.</strong> <strong>Median</strong> — expensive outliers inflate the mean; the median resists them</p>'
        '<p><strong>Q4.</strong> B better on average (68 > 65) and more consistent (range 15 < 40) → '
        '<strong>B on both counts</strong></p>'
        '<p><strong>Q5.</strong> Sample may not represent the population; estimates carry sampling '
        'error; larger samples reduce but never remove it</p>'
        '<p><strong>Q6.</strong> <strong>B more consistent</strong> (8 < 18); <strong>B faster on average</strong> (34 < 32? '
        'no — A is faster: 32 < 34). Faster = A; consistent = B.</p>'
        '<p><strong>Q7.</strong> Mean > median → <strong>positive skew</strong>; likely cause: a few unusually '
        'large values (e.g. one very high spender)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Mean: use for symmetric data · Median: skewed data/outliers · Mode: categories</li>'
        '<li>Range: quick spread (one outlier inflates it) · IQR: resistant spread</li>'
        '<li>Comparisons need TWO sentences: one average, one spread, both in CONTEXT</li>'
        '<li>Mean > median → positive skew · mean < median → negative skew</li>'
        '<li>Sample conclusions: state they are estimates and depend on sample size</li>'
        '</ul>'),
    context=CTX('<p>Comparing distributions: 2–4 marks on Papers 1/2. Contextual sentences '
        '("Delivered faster on average") score; bare number comparisons do not.</p>'
        '<p>Links to: central tendency (S4), grouped data (S3), scatter (S6).</p>'))

B["S6-scatter-graphs.html"] = dict(
    marker="Q6: A best-fit line passes through (2, 10) and (6, 30). Write its equation and predict y at x = 10",
    worked=W_SEC("Scatter graphs: correlation direction/strength, line of best fit by eye, predictions INSIDE the data range (interpolation — reliable) vs outside (extrapolation — risky).",
        EX("Describe the correlation between hours of practice and errors made, and what it does NOT prove.",
            '<p><strong>Negative correlation</strong> (more practice → fewer errors). It does NOT prove '
            'practice CAUSES fewer errors — other factors may explain the pattern (correlation ≠ causation).</p>',
            "B1 correlation, B1 the causation caveat. The 'does not prove' clause is the examined AO3 line.") +
        EX("A best-fit line has equation y = 4x + 1 (x = hours, y = score). Predict the score for 6 hours, and comment on predicting for 50 hours.",
            '<p>y = 25 → <strong>25</strong> (interpolation, reliable). For 50 hours: y = 201 — '
            '<strong>extrapolation, unreliable</strong> (the trend need not continue that far).</p>',
            "M1 for the substitution, A1 for 25, B1 for the extrapolation caveat."))
    + '<p><strong>Exam wording to expect:</strong> "describe the correlation", "draw the line of best fit", "use it to estimate…", "comment on the reliability".</p>',
    questions=["Q6: A best-fit line passes through (2, 10) and (6, 30). Write its equation and predict y at x = 10", "Q7: A scatter graph shows an outlier far from the trend. What should you do before drawing the line of best fit?"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> <strong>Negative correlation</strong> — more sleep, less tiredness</p>'
        '<p><strong>Q2.</strong> y = 3(7) + 5 = <strong>26</strong></p>'
        '<p><strong>Q3.</strong> Interpolation: predicting <strong>within</strong> the data range (reliable); '
        'extrapolation: outside it (unreliable)</p>'
        '<p><strong>Q4.</strong> <strong>Extrapolation</strong> — 95% exceeds the 40–90% data range</p>'
        '<p><strong>Q5.</strong> Any two: ruler; follow the trend; balance points above/below; '
        'pass through the mean point if drawn; ignore outliers</p>'
        '<p><strong>Q6.</strong> Gradient = (30 − 10)/4 = 5 → y = 5x (through origin? check intercept: 10 = 5×2 ✓) → '
        '<strong>y = 5x</strong>; at x = 10: <strong>50</strong></p>'
        '<p><strong>Q7.</strong> <strong>Identify and check the outlier</strong> — if it is a data error, exclude it; '
        'otherwise keep it but note it — then draw the best fit ignoring it if spurious</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Correlation: positive/negative × strong/weak/none — describe DIRECTION and STRENGTH</li>'
        '<li>Best fit: single straight line, balanced points, drawn with a ruler</li>'
        '<li>Interpolation (inside range) reliable; extrapolation (outside) not</li>'
        '<li>Correlation ≠ causation — always the AO3 caveat</li>'
        '<li>Outliers: investigate before excluding; they drag the best-fit line</li>'
        '</ul>'),
    context=CTX('<p>Scatter graphs: 3–5 marks on Papers 2/3 — describing, fitting, estimating. '
        'The reliability commentary (interpolation/extrapolation, causation) is where top marks live.</p>'
        '<p>Links to: describing populations (S5), graphs (A9), proportion (R7).</p>'))

B["G25-vector-proofs.html"] = dict(
    marker="Q6: OA = a, OB = b. M divides AB in ratio 1 : 3. Find OM in terms of a and b",
    worked=W_SEC("Vector proofs: write every journey as a path sum (AB = AO + OB), then test parallel (scalar multiple) or collinear (parallel + shared point).",
        EX("OP = p, OQ = q. M is the midpoint of PQ. Find OM.",
            '<p>OM = OP + PM = p + ½(PQ) = p + ½(q − p) = <strong>½(p + q)</strong></p>',
            "M1 for the path, A1 for ½(p + q). The midpoint vector is the average of the position vectors.") +
        EX("XY = 4a and YZ = −6a. Show X, Y, Z are collinear.",
            '<p>XZ = XY + YZ = 4a − 6a = −2a = −½(4a) = −½ XY</p>'
            '<p>XZ is a scalar multiple of XY AND shares the point Y → <strong>collinear ∎</strong></p>',
            "M1 for the scalar multiple, A1 with the shared-point condition. Parallel alone is not collinearity — a common point is required."))
    + '<p><strong>Exam wording to expect:</strong> "prove that … are collinear", "find OM in terms of a and b", Higher-tier topic in this folder.</p>',
    questions=["Q6: OA = a, OB = b. M divides AB in ratio 1 : 3. Find OM in terms of a and b", "Q7: ABCD: AB = p, BC = q, CD = p, DA = q. What shape is ABCD? Prove it."],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> AC = AB + BC = 3a + 3a = 6a = 2(AB) → AC parallel to AB and sharing A → '
        '<strong>collinear ∎</strong></p>'
        '<p><strong>Q2.</strong> OM = ½(a + b) — midpoint of OA and OB endpoints</p>'
        '<p><strong>Q3.</strong> AB = 2CD → parallel (scalar multiple) ∎</p>'
        '<p><strong>Q4.</strong> OP = OA + (2/5)AB = a + (2/5)(b − a) = <strong>(3/5)a + (2/5)b</strong></p>'
        '<p><strong>Q5.</strong> AB = DC → one pair of opposite sides equal AND parallel → '
        '<strong>parallelogram ∎</strong></p>'
        '<p><strong>Q6.</strong> OM = OA + (1/4)AB = a + ¼(b − a) = <strong>¾a + ¼b</strong></p>'
        '<p><strong>Q7.</strong> Opposite sides equal and parallel (AB = DC, BC = AD) → '
        '<strong>parallelogram ∎</strong></p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Path rule: AB = AO + OB (any route between the points)</li>'
        '<li>Midpoint: OM = ½(OA + OB) · ratio division: OP = OA + fraction × AB</li>'
        '<li>Parallel: one vector = scalar multiple of the other</li>'
        '<li>Collinear: parallel + a shared point</li>'
        '<li>Parallelogram proof: one pair of opposite sides equal AND parallel</li>'
        '</ul>'),
    context=CTX('<p>Vector proofs: Higher-tier content in this folder — 4–6 marks on Higher papers. '
        'Expressing everything in terms of a and b, then FACTORING to reveal scalar multiples, is the method.</p>'
        '<p>Links to: vectors (G24), congruence/proof (G5/G6), coordinate geometry (G11).</p>'))

B["S4-central-tendency.html"] = dict(
    marker="Q6: Five numbers have mean 14. Four of them are 10, 12, 15, 17. Find the fifth",
    worked=W_SEC("Averages: mean (total ÷ count), median (middle of ORDERED data), mode (most frequent), range (spread). Reverse questions use total = mean × n.",
        EX("Find the mean of 3, 7, 8, 10, 12.",
            '<p>Total 40 → mean = 40 ÷ 5 = <strong>8</strong></p>',
            "B1 for 8. The total-first habit (sum, then divide) prevents lost values.") +
        EX("The mean of 6 numbers is 11. One number is removed and the mean becomes 10. What was removed?",
            '<p>Original total 66; new total 60 → removed number = <strong>6</strong></p>',
            "M1 for both totals, A1 for 6. Mean-reversal questions always run through the TOTAL."))
    + '<p><strong>Exam wording to expect:</strong> "calculate the mean/median/mode/range", reverse-mean problems, comparing averages.</p>',
    questions=["Q6: Five numbers have mean 14. Four of them are 10, 12, 15, 17. Find the fifth", "Q7: Find the median of: 9, 3, 7, 11, 3, 8, 5"],
    solutions=SOL_HEAD +
        '<p><strong>Q1.</strong> Sum 44 ÷ 7 ≈ <strong>6.29</strong>; ordered: 4,5,6,6,6,8,9 → median <strong>6</strong>; mode <strong>6</strong></p>'
        '<p><strong>Q2.</strong> Total 60 − 47 = <strong>13</strong></p>'
        '<p><strong>Q3.</strong> 89 − 12 = <strong>77</strong></p>'
        '<p><strong>Q4.</strong> 42 − 15 = <strong>27</strong></p>'
        '<p><strong>Q5.</strong> <strong>Mode</strong> — colours are categorical; no numerical mean/median exists</p>'
        '<p><strong>Q6.</strong> Total = 70; sum given = 54 → fifth = <strong>16</strong></p>'
        '<p><strong>Q7.</strong> Ordered: 3, 3, 5, 7, 8, 9, 11 → median = <strong>7</strong> (4th of 7)</p>\n</div>\n</section>',
    keyfacts=KF('<ul>'
        '<li>Mean = total ÷ n → TOTAL = mean × n (the reverse-question engine)</li>'
        '<li>Median: ORDER first; odd n → middle; even n → mean of the middle two</li>'
        '<li>Mode: most frequent (can be none, or more than one)</li>'
        '<li>Range = largest − smallest (a SPREAD, not an average)</li>'
        '<li>Mean uses every value; the median ignores extremes; the mode needs repeats</li>'
        '</ul>'),
    context=CTX('<p>Averages and range: 3–5 marks per paper, and the foundation of every comparison '
        'question (S5). Reverse-mean questions are the reliable 3-marker.</p>'
        '<p>Links to: comparing populations (S5), grouped data (S3), charts (S2).</p>'))

if __name__ == "__main__":
    run(B)
    run2(B)
