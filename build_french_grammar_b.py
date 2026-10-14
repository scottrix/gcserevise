#!/usr/bin/env python3
"""French grammar bank pages 3-4 (FR27 pronouns/negation, FR28 prepositions/questions/modals)."""
import re
import sys
from build_french_grammar_a import build, SEC, END, TBL, Q

P3 = (
    SEC('📋 Key Concepts: Pronouns and Negation') +
    '<p>Pronouns replace nouns so you avoid repeating <em>mon frère</em> five times — and examiners award '
    'complex-structure marks for using them. Negation in French is a two-part wrapper around the VERB, '
    'not a single word like “not”.</p>' +
    TBL([
        ['Type','Forms','Example','Meaning'],
        ['Stress pronouns','moi, toi, lui, elle, nous, vous, eux, elles','Moi, j’adore le cine.','Me, I love the cinema.'],
        ['Direct object','me, te, le, la, nous, vous, les','Je le vois chaque jour.','I see him/it every day.'],
        ['Indirect object','me, te, lui, nous, vous, leur','Je lui parle souvent.','I speak to him/her often.'],
        ['y (there / about it)','y','J’y vais demain.','I’m going there tomorrow.'],
        ['en (of it / some)','en','J’en mange beaucoup.','I eat a lot of it.'],
    ]) +
    '<p>Pronouns go BEFORE the verb (after the subject): <em>Je <strong>le</strong> vois</em>, '
    '<em>Nous <strong>y</strong> allons</em>. In the passé composé they go before the AUXILIARY: '
    '<em>Je <strong>l’ai</strong> vu</em>. In infinitive constructions they attach before the INFINITIVE: '
    '<em>Je vais <strong>le</strong> faire</em>.</p>' + END +

    SEC('📝 Negation: The Two-Part Wrapper') +
    TBL([
        ['Negation','Wrapper','Example','Meaning'],
        ['not','ne … pas','Je ne mange pas de viande.','I don’t eat meat.'],
        ['no longer','ne … plus','Il ne joue plus au rugby.','He no longer plays rugby.'],
        ['never','ne … jamais','Nous ne sortons jamais le soir.','We never go out in the evening.'],
        ['nothing','ne … rien','Je ne fais rien le dimanche.','I do nothing on Sundays.'],
        ['nobody','ne … personne','Je ne connais personne ici.','I don’t know anybody here.'],
        ['only','ne … que','Je ne bois que de l’eau.','I only drink water.'],
    ]) +
    '<p>Word order rules that earn accuracy marks: <strong>personne</strong> comes AFTER the verb '
    '(<em>je ne vois personne</em>), <strong>rien</strong> after the verb (<em>je ne fais rien</em>), '
    'while <strong>pas/plus/jamais</strong> wrap around it. In the passé composé, ne + pas/plus/jamais '
    'wrap the AUXILIARY: <em>je n’ai jamais vu ce film</em>; but <em>je n’ai rien dit</em> and '
    '<em>je n’ai vu personne</em> keep rien/personne after the participle.</p>' + END +

    SEC('📝 y and en — The Two Pronouns English Lacks') +
    '<p><strong>y</strong> replaces a PLACE introduced by à/dans/chez (<em>tu vas au cinéma ? — j’y vais</em>) '
    'and the phrase <strong>il y a</strong> (there is/are) — the single most used structure in French.</p>' +
    '<p><strong>en</strong> replaces quantities and “of it”: <em>tu veux du pain ? — j’en veux bien</em>; '
    '<em>j’ai trois frères — j’en ai trois</em>. With numbers and quantities the article drops: '
    '<em>j’en mange deux</em> (not « j’en mange deux du »).</p>' + END +

    SEC('🧮 Worked Examples — Exam Style') +
    '<div class="example"><p><strong>Translate: “I never do my homework in the evening but I did it yesterday.”</strong></p>'
    '<p>« Je ne fais jamais mes devoirs le soir mais je les ai faits hier. »</p>'
    '<p><em>ne…jamais around the present verb; les before the auxiliary in the passé composé; '
    'fait + agreement (faits). Three accuracy marks in one sentence.</em></p></div>'
    '<div class="example"><p><strong>Rewrite with pronouns: « Je donne le livre à ma sœur. »</strong></p>'
    '<p>« Je <strong>le lui</strong> donne. » — direct object (le) BEFORE indirect (lui).</p>'
    '<p><em>When both pronouns appear, the order me/te/nous/vous → le/la/les → lui/leur is fixed. '
    'This order is a classic Higher-tier trap.</em></p></div>' + END +

    SEC('❓ Practice Questions') +
    '<div class="practice-questions">' +
    Q(1,'Negate: « Je regarde la télévision. » (not)') +
    Q(2,'Negate in the passé composé: « Il a mangé du poulet. » (not)') +
    Q(3,'Replace with a pronoun: « Tu vas au parc ? — Oui, je vais au parc. »') +
    Q(4,'Replace with en: « Vous buvez du café ? — Oui, nous buvons du café. »') +
    Q(5,'Two pronouns: « Je parle à mes parents. » (I speak to them)') +
    Q(6,'Translate: I no longer play video games.') +
    '</div>' + END +

    SEC('✅ Answers') +
    '<ol>'
    '<li>Je ne regarde pas la télévision.</li>'
    '<li>Il n’a pas mangé de poulet. (du → de after negation)</li>'
    '<li>Oui, j’y vais.</li>'
    '<li>Oui, nous en buvons.</li>'
    '<li>Je leur parle.</li>'
    '<li>Je ne joue plus aux jeux vidéo.</li>'
    '</ol>' + END +

    SEC('📌 Key Facts to Memorise') +
    '<ul>'
    '<li>Pronouns sit BEFORE the verb; before the auxiliary in PC; before the infinitive after aller/vouloir</li>'
    '<li>Two pronouns together: me/te/nous/vous → le/la/les → lui/leur</li>'
    '<li>ne … pas / plus / jamais wrap the (auxiliary) verb; rien and personne go AFTER it</li>'
    '<li>du/de la/des → de under negation; le/la/les survive</li>'
    '<li>il y a = there is/there are · y = there · en = of it/some</li>'
    '</ul>' + END +

    SEC('🗺️ In the Exam') +
    '<p>Using <strong>two pronouns correctly</strong> (e.g. « je les y ai vus » is extreme — but « je lui en parle ») '
    'is a top-band structure in the 150-word task. In speaking, <strong>en</strong> answers quantity questions '
    'naturally: « Est-ce que tu manges beaucoup de légumes ? — Oui, j’en mange tous les jours. » '
    'If a negation question appears (« Est-ce que tu fumes ? »), answer with the full wrapper '
    '(« Non, je ne fume pas ») — the two-part negation is itself an accuracy mark.</p>' + END +

    SEC('⚠️ Common Errors') +
    '<ul>'
    '<li><span class="wrong">Wrong: je regarde pas la télé</span> <span class="right">Correct: je ne regarde pas la télé (both halves of the wrapper)</span></li>'
    '<li><span class="wrong">Wrong: je vais le à faire</span> <span class="right">Correct: je vais le faire (pronoun directly before the infinitive)</span></li>'
    '<li><span class="wrong">Wrong: je ne mange pas du pain</span> <span class="right">Correct: je ne mange pas de pain</span></li>'
    '<li><span class="wrong">Wrong: j’en veux deux du croissants</span> <span class="right">Correct: j’en veux deux (article drops after en + number)</span></li>'
    '<li><span class="wrong">Wrong: je ne fais personne</span> <span class="right">Correct: je ne vois personne (personne pairs with the right verb and follows it)</span></li>'
    '</ul>' + END +

    SEC('🎯 Exam Tips') +
    '<ul>'
    '<li>Drop in one y or en per speaking answer — cheap complex-structure marks</li>'
    '<li>Never split the negation wrapper: write ne first, then the verb, then pas</li>'
    '<li>In the 150-word task, one « ce qui est important, c’est que… » style pronoun structure lifts the register</li>'
    '<li>Check PC negatives: wrapper around the auxiliary, du → de</li>'
    '</ul>' + END
)

P4 = (
    SEC('📋 Key Concepts: Prepositions, Questions and Modal Verbs') +
    '<p>Three small toolkits unlock fluent questions and opinions: prepositions (especially with countries '
    'and places), the three ways to form questions, and the modal verbs that turn simple verbs into plans, '
    'possibilities and obligations.</p>' +
    TBL([
        ['Destination','Preposition','Example'],
        ['Cities','à','Je vais à Paris.'],
        ['Feminine countries/regions','en','en France, en Espagne, en Écosse'],
        ['Masculine countries','au','au Pays de Galles, au Portugal'],
        ['Plural countries','aux','aux États-Unis, aux Pays-Bas'],
        ['Coming from','de / du / de la / des','je viens de Londres, du Japon, des Pays-Bas'],
    ]) + END +

    SEC('📝 Three Ways to Ask a Question') +
    TBL([
        ['Method','Example','Register'],
        ['Intonation','Tu viens ?','Spoken, informal'],
        ['Est-ce que + statement','Est-ce que tu viens ?','Neutral — always safe in writing'],
        ['Inversion','Venez-vous ?','Formal; adds -t- after il/elle (a-t-il ?)'],
    ]) +
    '<p>Question words: <strong>qui</strong> (who), <strong>que/quoi</strong> (what), <strong>quand</strong> (when), '
    '<strong>où</strong> (where), <strong>pourquoi</strong> (why), <strong>comment</strong> (how), '
    '<strong>combien (de)</strong> (how many/much), <strong>quel/quelle/quels/quelles</strong> (which — agrees '
    'with the noun: <em>quelle matière</em>). Photo-card questions are almost always '
    '<em>qu’est-ce qu’il y a… / que fait… / où…</em> — recognise them instantly.</p>' + END +

    SEC('📝 Modal Verbs: pouvoir, devoir, vouloir, il faut') +
    TBL([
        ['Modal','Present forms','Meaning','Example'],
        ['pouvoir','peux, peux, peut, pouvons, pouvez, peuvent','can / to be able','Je peux venir samedi.'],
        ['devoir','dois, dois, doit, devons, devez, doivent','must / to have to','Je dois réviser ce soir.'],
        ['vouloir','veux, veux, veut, voulons, voulez, veulent','to want','Je veux travailler à l’étranger.'],
        ['il faut','il faut (invariable)','it is necessary','Il faut apprendre les verbes.'],
    ]) +
    '<p>Modals are followed by an INFINITIVE — no preposition: <em>je peux <strong>jouer</strong></em> '
    '(never « je peux de jouer »). Conditional forms soften opinions: <em>je voudrais</em> (I would like), '
    '<em>je devrais</em> (I should), <em>on pourrait</em> (we could) — three conditional modals that lift '
    'a photo-card or writing answer instantly.</p>' + END +

    SEC('📝 depuis vs pendant') +
    '<p><strong>depuis</strong> + present tense for an action still ongoing: '
    '<em>j’apprends le français depuis trois ans</em> (I have been learning… for three years). '
    '<strong>pendant</strong> for a completed duration: <em>j’ai habité à Lyon pendant deux ans</em>. '
    'Using depuis + present where English uses the present perfect is a hallmark of a strong candidate.</p>' + END +

    SEC('🧮 Worked Examples — Exam Style') +
    '<div class="example"><p><strong>Translate: “We have lived in Wales for five years and we want to move to the United States.”</strong></p>'
    '<p>« Nous habitons au Pays de Galles depuis cinq ans et nous voulons déménager aux États-Unis. »</p>'
    '<p><em>au + masculine country, depuis + PRESENT (not “we have lived”), aux + plural country, '
    'vouloir + infinitive. Four marks, all structural.</em></p></div>'
    '<div class="example"><p><strong>Photo card: say what the people must/could do and what you would like to do.</strong></p>'
    '<p>« À mon avis, ils doivent faire attention parce que la mer est dangereuse. On pourrait nager plus près '
    'de la plage. Moi, je voudrais essayer le surf un jour. »</p>'
    '<p><em>devoir + inf, pouvoir + inf, vouloir conditional — three modals, three justifications: '
    'the exact shape examiners want in speaking follow-ups.</em></p></div>' + END +

    SEC('❓ Practice Questions') +
    '<div class="practice-questions">' +
    Q(1,'Preposition: « Je vais ___ Espagne cet été. »') +
    Q(2,'Preposition: « Il travaille ___ États-Unis. »') +
    Q(3,'Ask formally: « You (vous) come tomorrow? » using inversion.') +
    Q(4,'Which question word: « ___ matière préfères-tu ? » (which subject)') +
    Q(5,'Modal + infinitive: « I must do my homework. »') +
    Q(6,'depuis or pendant: « J’étudie le français ___ deux ans. »') +
    '</div>' + END +

    SEC('✅ Answers') +
    '<ol>'
    '<li>en Espagne (feminine country)</li>'
    '<li>aux États-Unis (plural)</li>'
    '<li>Venez-vous demain ?</li>'
    '<li>Quelle matière…</li>'
    '<li>Je dois faire mes devoirs.</li>'
    '<li>depuis (still studying → depuis + present)</li>'
    '</ol>' + END +

    SEC('📌 Key Facts to Memorise') +
    '<ul>'
    '<li>en + feminine country · au + masculine · aux + plural · à + city</li>'
    '<li>Question trio: intonation (spoken) · est-ce que (safe) · inversion (formal, -t- after il/elle)</li>'
    '<li>Modals + INFINITIVE with no preposition; il faut is invariable</li>'
    '<li>Conditional softeners: je voudrais / je devrais / on pourrait</li>'
    '<li>depuis + present (ongoing) · pendant + past (completed duration)</li>'
    '<li>quel/quelle/quels/quelles agree with the following noun</li>'
    '</ul>' + END +

    SEC('🗺️ In the Exam') +
    '<p>Role-plays and photo cards are MODAL-verb territory: justify with '
    '« il faut + inf » and hypothesise with « on pourrait + inf ». In the 90/150-word tasks, a '
    '« je voudrais… parce que » plan sentence for the future plus a « depuis + present » line for the past '
    'covers two assessment criteria in two sentences. Question formation matters for the conversation: '
    'asking the examiner one question (« Et vous ? ») is often required — never answer in monologue.</p>' + END +

    SEC('⚠️ Common Errors') +
    '<ul>'
    '<li><span class="wrong">Wrong: je vais à la France</span> <span class="right">Correct: je vais en France (feminine country)</span></li>'
    '<li><span class="wrong">Wrong: je peux de jouer</span> <span class="right">Correct: je peux jouer (no preposition after modals)</span></li>'
    '<li><span class="wrong">Wrong: j’habite ici pendant trois ans (still living there)</span> <span class="right">Correct: j’habite ici depuis trois ans</span></li>'
    '<li><span class="wrong">Wrong: quel est ton matières préférée?</span> <span class="right">Correct: quelle est ta matière préférée (agreement + possessive)</span></li>'
    '<li><span class="wrong">Wrong: a-il un parc ?</span> <span class="right">Correct: y a-t-il un parc ? (the -t- bridges vowels)</span></li>'
    '</ul>' + END +

    SEC('🎯 Exam Tips') +
    '<ul>'
    '<li>Memorise the country-preposition grid — it appears in every travel/holiday answer</li>'
    '<li>One conditional modal per speaking answer: je voudrais / on pourrait</li>'
    '<li>Il faut + infinitive is the safest justification structure in French — use it for opinions</li>'
    '<li>In role-plays, if you do not understand, ask: « Pouvez-vous répéter, s’il vous plaît ? » — it is credited communication</li>'
    '</ul>' + END
)

if __name__ == "__main__":
    PAGES = [
        ("FR27-pronouns-and-negation",
         "French Pronouns and Negation",
         "Stress, direct and indirect object pronouns, y and en, and the six French negation wrappers — with word order rules and exam technique for writing and speaking.",
         P3),
        ("FR28-prepositions-questions-and-modal-verbs",
         "French Prepositions, Questions and Modal Verbs",
         "Country prepositions (en, au, aux), question formation, pouvoir/devoir/vouloir/il faut, and depuis vs pendant — with photo-card and writing exam technique.",
         P4),
    ]
    out = sys.argv[1] if len(sys.argv) > 1 else 'topics/french/aqa'
    for slug, title, desc, body in PAGES:
        html = build(slug, title, desc, body)
        open(f'{out}/{slug}.html', 'w', encoding='utf-8').write(html)
        print('wrote', f'{out}/{slug}.html', len(html), 'bytes')
