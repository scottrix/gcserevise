#!/usr/bin/env python3
"""Board-focus data: sciences + mathematics. subject -> board -> html block."""

SCI = {}

_bio = {
"aqa": "<p><strong>Spec 8461.</strong> Two 1h45 written papers (100 marks each), Foundation/Higher tiers. Ten required practicals are examined inside the papers — learn the method, variables and graph work for each. Paper 1 covers Cell biology, Organisation, Infection and response, Bioenergetics; Paper 2 covers Homeostasis, Inheritance, Variation and evolution, Ecology.</p>",
"edexcel": "<p><strong>Spec 1BI0.</strong> Two written papers with Foundation/Higher tiers. Edexcel's Topic 1, Key Concepts in Biology (cells, enzymes, transport, microscopy), underpins every later topic — revise it first and revisit it often. Core practicals are assessed within the written papers, so practical methods earn exam marks, not coursework marks.</p>",
"ocr": "<p><strong>Spec J247 (Gateway).</strong> Two written papers with Foundation/Higher tiers, organised into chapters B1–B6: the first paper draws on the earlier chapters (cells, respiration, photosynthesis) and the second on the later ones (nervous/hormones, inheritance, ecology). Practical skills (PAGs) are examined within the written papers.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland), A*–G grading.</strong> Content is split across units rather than two big papers, and practical skills are tested through booklet-style practical papers alongside the written units. Check which units your exam year covers and whether your route includes the practical booklets.</p>",
}
SCI["biology"] = _bio

_chem = {
"aqa": "<p><strong>Spec 8462.</strong> Two 1h45 written papers (100 marks each), Foundation/Higher tiers. Eight required practicals examined in the papers. Paper 1 covers Atomic structure, Bonding, Quantitative chemistry, Chemical changes and Energy changes; Paper 2 covers Rates, Organic chemistry, Analysis, Atmosphere and Using resources.</p>",
"edexcel": "<p><strong>Spec 1CH0.</strong> Two written papers with Foundation/Higher tiers across nine topic areas, from States of matter through to Fuels and Earth science. Chemical changes (Topic 3, including making salts and titration calculations) is Edexcel's heaviest early topic — master ionic equations and salt preparation early. Core practicals are assessed within the papers.</p>",
"ocr": "<p><strong>Spec J248 (Gateway).</strong> Two written papers with Foundation/Higher tiers, organised into chapters C1–C8 covering particles, reactions, quantitative chemistry, electrolysis, organic and analysis. The chapter split between the two papers differs by tier — check the current paper structure for your entry. Practical skills (PAGs) are examined within the written papers.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland), A*–G grading.</strong> Content is split across units, with practical skills assessed through booklet-style practical papers alongside the written units. Check your exam year's unit list and practical route.</p>",
}
SCI["chemistry"] = _chem

_phys = {
"aqa": "<p><strong>Spec 8463.</strong> Two 1h45 written papers (100 marks each), Foundation/Higher tiers. Ten required practicals examined in the papers. Paper 1 covers Energy, Electricity, the Particle model and Atomic structure; Paper 2 covers Forces, Waves, Magnetism and electromagnetism, and Space physics (triple only). Know which equations you must memorise for your tier and which appear on the data sheet.</p>",
"edexcel": "<p><strong>Spec 1PH0.</strong> Two written papers with Foundation/Higher tiers across eight topics, from Forces and motion through Electricity, Waves and Energy to Magnetism and the particle model. Edexcel expects equations to be selected and rearranged fluently — the equation list is given, but choosing and transforming is the examined skill. Core practicals are assessed within the papers.</p>",
"ocr": "<p><strong>Spec J249 (Gateway).</strong> Two written papers with Foundation/Higher tiers, organised into chapters P1–P6 covering matter, forces, electricity and magnetism, waves, radioactivity and energy, with practical skills (PAGs) embedded in the written papers.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland), A*–G grading.</strong> Content is split across units with practical-style booklet papers alongside the written units. Check your exam year's unit list.</p>",
}
SCI["physics"] = _phys

_comb = {
"aqa": "<p><strong>Spec 8464 (Trilogy).</strong> Six shorter written papers — two per science — rather than the triple award's longer papers, all at Foundation/Higher tiers. Required practicals are a reduced set drawn from the three disciplines; the same practicals can appear in any of the six papers, so keep biology, chemistry and physics practical knowledge separate in your head.</p>",
"edexcel": "<p><strong>Spec 1SC0.</strong> Six written papers (two per science) at Foundation/Higher tiers. Edexcel's combined award mirrors the triple topics in condensed form, with core practicals assessed inside the written papers — a combined-science practical can be examined in any of the six papers.</p>",
"ocr": "<p><strong>Spec J250 (Gateway Combined).</strong> Papers span all three sciences using the same B/C/P chapter structure as the separate sciences, at Foundation/Higher tiers. Because each paper mixes disciplines, revise by science (all biology chapters, then all chemistry) rather than by paper.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland), A*–G grading.</strong> Units separate the sciences, with practical skills assessed through booklet-style papers. Check your exam year's unit structure.</p>",
}
SCI["combined-science"] = _comb

MATHS = {
"aqa": "<p><strong>Spec 8300.</strong> Three papers, each 80 marks and 1h30: Paper 1 non-calculator, Papers 2 and 3 calculator. Foundation/Higher tiers. Roughly a third of the marks sit under AO2 (reasoning) and AO3 (problem-solving), so show every line of working — method marks survive arithmetic slips.</p>",
"ocr": "<p><strong>Spec J560.</strong> Three papers of 100 marks each: Paper 1 non-calculator, Papers 2 and 3 calculator, at Foundation/Higher tiers. OCR marks problem-solving explicitly, and its papers tend to front-load multi-step worded contexts — practise extracting the mathematics from prose before calculating.</p>",
}

if __name__ == "__main__":
    print(len(SCI), "science subjects +", len(MATHS), "maths")
