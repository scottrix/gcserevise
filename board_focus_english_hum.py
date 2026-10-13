#!/usr/bin/env python3
"""Board-focus data: English, humanities, MFL."""

ENG_LANG = {
"aqa": "<p><strong>Spec 8700.</strong> Paper 1 (1h45): fiction reading plus descriptive or narrative writing. Paper 2 (1h45): viewpoints paper — two non-fiction extracts, comparison and writing to present a viewpoint. Questions follow a fixed order (Q1 select, Q2 language, Q3 structure, Q4 evaluation, Q5 writing) — learn the question types by heart so timing is automatic.</p>",
"edexcel": "<p><strong>Spec 1EN0.</strong> Paper 1: fiction reading plus imaginative writing. Paper 2: non-fiction and literary non-fiction reading plus transactional writing (letters, articles, speeches). Edexcel's reading questions blend retrieval and language analysis, so label each answer clearly with the skill being assessed.</p>",
"ocr": "<p><strong>Spec J351.</strong> Paper 1: Communicating information and ideas — non-fiction reading plus writing to inform, argue or persuade. Paper 2: Exploring effects and creative writing — a literary extract plus imaginative writing. OCR rewards reading the SOURCE line references carefully: its questions pin you to specific lines.</p>",
"eduqas": "<p><strong>Spec C700.</strong> Component 1: a 20th-century literary extract with reading questions plus prose writing. Component 2: 19th- and 21st-century non-fiction reading plus transactional/persuasive writing. Eduqas reading questions build cumulatively — the later (higher-mark) questions reuse evidence you found earlier.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland).</strong> Content is split across units covering reading and writing, with speaking and listening endorsed separately. Unit wording and weighting vary by exam year — map your units before you plan revision.</p>",
}

ENG_LIT = {
"aqa": "<p><strong>Spec 8702 — CLOSED BOOK: no texts in the exam.</strong> Paper 1: Shakespeare and a 19th-century novel. Paper 2: modern prose or drama, the Power and Conflict poetry anthology, and unseen poetry. Memorise short, versatile quotations — closed-book questions reward precise, integrated quotes over long ones.</p>",
"edexcel": "<p><strong>Spec 1ET0.</strong> Paper 1: Shakespeare plus a post-1914 British play or novel. Paper 2: a 19th-century novel, a poetry collection, and unseen poetry. Edexcel set-text routes differ between centres — revise the exact texts your class studies, and note Edexcel's literature questions often specify an extract plus 'the whole text'.</p>",
"ocr": "<p><strong>Spec J352.</strong> Paper 1: a modern prose or drama text plus a literary-heritage text (Shakespeare or a 19th-century novel). Paper 2: the Towards a World Unknown poetry anthology plus unseen poems. OCR's comparison questions ask you to LINK poems by idea first, then method — lead with the connection, not the devices.</p>",
"eduqas": "<p><strong>Component 1: Shakespeare and the poetry anthology. Component 2: post-1914 prose/drama plus unseen poetry comparison.</strong> Eduqas unseen poetry asks about TWO poems with explicit comparison marks — plan a shared idea before writing. Set-text options vary by centre; revise your exact route.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland).</strong> Set texts are examined across units covering poetry, prose and drama, with study options varying by unit. Check your unit list and set texts against the current CCEA specification before planning quotation learning.</p>",
}

MATHS_NOTE = {}

HIST = {
"aqa": "<p><strong>Spec 8145.</strong> Paper 1: Understanding the modern world (one period study + one wider-world depth study). Paper 2: Shaping the nation (one thematic study with historic environment + one British depth study including the historic environment). AQA's AO4 historic-environment questions reward site-specific knowledge, not general period knowledge.</p>",
"edexcel": "<p><strong>Spec 1HI0.</strong> Paper 1: Thematic study with historic environment. Paper 2: Period study + British depth study. Paper 3: Modern depth study. Three papers means three distinct revision plans — Edexcel's source/interpretation marks differ per paper, so practise each paper's question stems separately.</p>",
"ocr": "<p><strong>Spec J410 — two routes:</strong> History A (Explaining the Modern World) and History B (Schools History Project). Your route decides the topics; check which route your centre takes. OCR's depth-study questions reward precise narrative chains — cause, event, consequence in order.</p>",
"eduqas": "<p><strong>Routes A and B.</strong> Both routes combine a period study, depth studies and a thematic study with non-British elements. Eduqas papers use structured (part-labelled) questions — answer every lettered part, as later parts build on earlier ones.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland).</strong> Units cover local, national and international studies with source-based elements. Check your unit options — CCEA's Northern Ireland elements appear in questions that other boards never ask.</p>",
}

GEOG = {
"aqa": "<p><strong>Spec 8035.</strong> Paper 1: Physical geography (natural hazards, the living world, UK physical landscapes). Paper 2: Human geography (urban issues, the economic world, resource management). Paper 3: Issue evaluation (pre-released booklet) + fieldwork + skills. AQA's Paper 3 is unique — study the pre-release BEFORE the exam and know your two fieldwork enquiries cold.</p>",
"edexcel": "<p><strong>Spec B (1GB0).</strong> Paper 1: Global geographical issues. Paper 2: UK geographical issues (including fieldwork). Paper 3: People and environment issues — making geographical decisions. Edexcel B is case-study led with named, specific examples; its Paper 3 decision-making exercise rewards weighing options, not describing them.</p>",
"ocr": "<p><strong>Spec B (J384, Our Natural World / People and Society).</strong> Three papers including a geographical-decisions element and fieldwork questions. OCR rewards precise command-word response: 'describe' earns description marks that 'explain' phrasing will not, and vice versa.</p>",
"eduqas": "<p><strong>Routes A and B.</strong> Components split physical, human and fieldwork/issues content. Eduqas fieldwork questions ask about YOUR enquiry process (hypothesis, data collection, evaluation) — write up your methods in detail after each fieldtrip while it is fresh.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland).</strong> Units split physical and human themes with fieldwork elements. Check your unit list; CCEA case-study expectations name specific local examples.</p>",
}

RS = {
"aqa": "<p><strong>Spec A (8062).</strong> Paper 1: The study of religions (beliefs and practices). Paper 2: Thematic studies (relationships, crime and punishment, peace and conflict, etc.). AQA's 12-mark questions require a justified conclusion — 'some agree… however… therefore' structure scores, bare description does not.</p>",
"edexcel": "<p><strong>Spec B.</strong> Areas of study split religion and ethics (Area 1) from religion, peace and conflict (Area 2), with philosophy-style questions inside religion papers for some routes. Edexcel rewards quoting scripture precisely — learn short citations with references.</p>",
"ocr": "<p><strong>Spec J625.</strong> Christianity plus one other religion, and thematic units. OCR's beliefs-and-teachings vs practices split per religion means two parallel revision lists — revise each religion in the same order both times.</p>",
"eduqas": "<p><strong>Routes A and B.</strong> Route A pairs two religions with thematic units; Route B has a different balance. Eduqas's part-structured questions build from 'give two' to evaluation — always answer every lettered part.</p>",
"ccea": "<p><strong>Unitised assessment (Northern Ireland).</strong> Units cover Matthew's Gospel and/or ethics themes depending on route. CCEA's Gospel-paper questions reward textual knowledge of specific passages — learn the named stories with details.</p>",
}

MFL_NOTE = {}

def _mfl(spec):
    return {
"aqa": f"<p><strong>Spec {spec}.</strong> Four separate papers: Listening, Speaking, Reading, Writing, each at Foundation or Higher tier (you sit the same tier across all four). AQA Speaking = role-play + photo card + general conversation; AQA Writing includes a structured translation task (English→target language). Learn answer-frame sentences you can reuse across papers.</p>",
"edexcel": f"<p><strong>Spec 1xx0 family.</strong> Four papers (listening, speaking, reading, writing) at Foundation/Higher. Edexcel's speaking = picture-based task + conversation; its reading paper includes a short translation INTO English. Edexcel rewards verb-tense variety — plan two tenses into every speaking and written answer.</p>",
"eduqas": f"<p><strong>Unitised components for the four skills</strong>, Foundation/Higher tiers. Eduqas writing includes translation both ways and structured short tasks; its listening uses longer, slower recordings than some boards — practise note-taking, not just gist.</p>",
"ccea": f"<p><strong>Unitised assessment (Northern Ireland).</strong> Listening, reading and writing are examined; the speaking test is teacher-conducted and externally moderated. CCEA writing tasks are shorter but more frequent — build accuracy in short pieces, especially present/past/future verb frames.</p>",
}

if __name__ == "__main__":
    print("ok")
