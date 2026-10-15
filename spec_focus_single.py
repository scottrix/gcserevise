#!/usr/bin/env python3
"""Spec-focus blocks for single-board subjects (P3: verify against the single spec)."""

SPEC = {}

SPEC["astronomy"] = {
"edexcel": "<p><strong>Edexcel GCSE Astronomy (1AS0).</strong> Assessment: two written papers — Paper 1 "
    "<em>Naked-eye Astronomy</em> and Paper 2 <em>Telescopic Astronomy</em> (each around 1h45), plus a "
    "requirement to complete observational tasks (unaided and aided) during the course — check the current "
    "specification for how observations are evidenced. These pages follow the 1AS0 topic split: Earth, Moon "
    "and Sun phenomena under naked-eye; instruments, stars, galaxies and cosmology under telescopic.</p>",
}

SPEC["geology"] = {
"eduqas": "<p><strong>Eduqas GCSE Geology.</strong> Assessment runs through written papers examining "
    "geological principles (minerals, rocks, fossils, structures) and geological Britain/processes, with "
    "map- and fieldwork-style questions inside the papers rather than separate coursework. These pages "
    "cover the rock cycle, plate tectonics, geological time, applied and economic geology topics — check "
    "the current paper structure and fieldwork expectations for your exam year.</p>",
}

SPEC["ancient-history"] = {
"ocr": "<p><strong>OCR GCSE Ancient History (J198).</strong> Two written papers, no coursework: one covering "
    "the Greek world (Persia and Greece, Alexander) and one covering Rome (kings to emperors, Britain). "
    "These pages map onto that split: ah-persian-wars, ah-greece and ah-alexander-style period topics for "
    "the Greek paper; ah-rome-republic, ah-rome-emperors and ah-britain for the Roman paper. Source-analysis "
    "skill is the assessed differentiator — every answer should cite the ancient evidence by author.</p>",
}

SPEC["classical-civilisation"] = {
"ocr": "<p><strong>OCR GCSE Classical Civilisation (J199).</strong> Two written papers, no coursework: "
    "<em>Myth and Religion</em> (gods, Hercules, the Underworld, Temples, festivals) and <em>Roman City "
    "Life</em> (housing, entertainment, citizenship). These pages follow that topic structure with the "
    "prescribed literary and visual sources — learn the named sources precisely, as the papers examine "
    "them by name.</p>",
}

SPEC["law"] = {
"aqa": "<p><strong>AQA GCSE Law (4160) — status check.</strong> AQA withdrew its GCSE Law specification "
    "and no awarding body currently offers GCSE Law in England; final awards were taken a number of years "
    "ago (confirm the exact position with your centre). These pages remain valuable as a foundation for "
    "A-Level Law and for citizenship/legal-literacy study: the English legal system, courts and personnel, "
    "and law in action (criminal, tort and family topics). Do not enter for a GCSE Law exam without "
    "first confirming availability with an awarding body.</p>",
}

SPEC["dance"] = {
"aqa": "<p><strong>AQA GCSE Dance (8236).</strong> Assessment: written paper (~40%) on the six anthology "
    "set works and dance theory; performance NEA (~30%, including the set phrases and a duo/trio "
    "performance); choreography NEA (~30%, with a choreographic log). Coursework is substantial — see the "
    "Coursework & NEA Guide on the Dance page for the log structure and recording requirements.</p>",
}

SPEC["film-studies"] = {
"eduqas": "<p><strong>Eduqas GCSE Film Studies.</strong> Assessment: two written papers covering "
    "comparative US/UK film, global English-language film, film history and key genres, plus a film-"
    "production NEA (an extract plus evaluation) worth around 30% — confirm the current weighting. These "
    "pages cover the set films, genre conventions and the micro-features (cinematography, editing, sound, "
    "mise-en-scène) that both the papers and the NEA evaluation examine.</p>",
}

SPEC["electronics"] = {
"eduqas": "<p><strong>Eduqas GCSE Electronics.</strong> Assessment: written papers on electronic "
    "principles and systems (components, analogue and digital circuits, logic, programming of "
    "microcontrollers) plus a substantial design-and-build NEA — confirm the current weighting in the "
    "specification. These pages cover the theory papers' content; the NEA needs circuit simulation and "
    "prototype evidence on top.</p>",
}

SPEC["engineering"] = {
"aqa": "<p><strong>AQA GCSE Engineering (8852).</strong> Written paper (~50%) plus a design-and-engineering "
    "NEA (~50%) from an AQA-set context. Edexcel (1EG0) and CCEA run similar splits. These pages cover the "
    "examined theory — materials, processes, maths-for-engineering, health and safety; the NEA needs a "
    "documented design-and-make portfolio on top (see the Coursework & NEA Guide).</p>",
}

SPEC["statistics"] = {
"aqa": "<p><strong>AQA GCSE Statistics (8382).</strong> Two written papers with Foundation/Higher tiers; "
    "confirm the calculator arrangement for your exam year. Edexcel (1ST0) runs two calculator papers. "
    "These pages follow the statistical enquiry cycle — planning, collecting, processing, presenting and "
    "interpreting — with AQA's Petersen capture-recapture and Edexcel's standard deviation both included "
    "where relevant.</p>",
}

if __name__ == "__main__":
    print(len(SPEC), "single-board subjects")
