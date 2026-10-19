import re
#!/usr/bin/env python3
"""Deep-dive expansion for the compact history option topics (additive sections)."""
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from expand_topics import insert_before_section

SEC = lambda h2, body: f'<section class="section">\n<h2>{h2}</h2>\n' + body + '\n</section>'
UL = lambda items: '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

D = {}

D["N41-establishing-control-castles-and-harrying"] = [
    SEC('📖 Detailed Notes: The Rebellions, Rebellion by Rebellion', UL([
        '<strong>Exeter (1068):</strong> Gytha (Harold\u2019s mother) held the city; William besieged it 18 days, '
        'letting the garrison go but confiscating the city\u2019s tax revenue. First proof that family ties to '
        'Harold still mattered.',
        '<strong>Stafford and Chester (1068–69):</strong> risings in the Midlands and north-west; William built '
        'castles AT Stafford and Chester as he suppressed them — suppression and castle-building were the same '
        'campaign.',
        '<strong>The northern rising (1069):</strong> Robert de Comines\u2019 700-man garrison at Durham was '
        'massacred; Edgar Aetheling, Waltheof and Gospatric joined; a Danish fleet took York — the closest the '
        'conquest came to failure.',
        '<strong>Ely and Hereward the Wake (1070–71):</strong> the Isle of Ely\u2019s fenland resistance, linked to '
        'Morcar and Siward Barn; the monastery\u2019s wealth (the "Camp of Refuge") made it a magnet. Hereward\u2019s '
        'survival in legend shows how the English remembered resistance.',
        '<strong>The Danes (1070, 1075):</strong> bought off in 1070 with 72,000 pounds — cheaper than war; in 1075 '
        'Cnut\u2019s fleet arrived too late. William also took the fleet\u2019s retreat as licence for the harrying.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        '1068 rising at Exeter — led by Gytha, Harold\u2019s mother.',
        'Durham massacre Jan 1069 — Robert de Comines\u2019 700 men.',
        'Danish fleet paid off 1070 — £72,000.',
        'Ely 1070–71 — Hereward the Wake, Morcar.',
        'Revolt of the Earls 1075 — Ralph, Roger, Waltheof; Waltheof beheaded 1076.',
    ])),
]

D["N42-feudalism-government-and-law"] = [
    SEC('📖 Detailed Notes: Oath, Land and the King\u2019s Peace', UL([
        '<strong>The Salisbury Oath (1086):</strong> William summoned ALL major landholders to Salisbury and made '
        'them swear loyalty DIRECTLY to him — even sub-tenants to their lords\u2019 lords. It broke the risk of '
        'barons becoming independent princes (as in Normandy) and is the single clearest sign that English feudalism '
        'was designed for royal power.',
        '<strong>Knight\u2019s fees in practice:</strong> a baron with 60 fees owed 60 knights; he kept some lands '
        '(demesne), distributed the rest to knights. Knights also owed castle guard (e.g. 3 months a year at a '
        'royal castle), suit at the lord\u2019s court, and aids (money for the lord\u2019s knighting of his son, '
        'his daughter\u2019s marriage, his ransom).',
        '<strong>Anglo-Norman law in action:</strong> the sworn inquest (jury-like enquiry) was Norman administrative '
        'genius — used for Domesday and, later, for theAssizes. William I also kept the geld (tax) and the wergild '
        'idea, while adding his own punishments (blinding, mutilation replaced many death sentences — as political '
        'theatre of mercy).',
        '<strong>Royal forest:</strong> by 1087 the Chronicle complains the law covered half of England — the '
        'New Forest alone displaced villages; Rufus extended it and died in it (1100).',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Salisbury Oath 1086 — all landholders swear DIRECTLY to the king.',
        'Knight\u2019s fee = 40 days\u2019 service/year + castle guard + aids.',
        'Murdrum fine = 46 marks on the hundred for an unexplained dead Norman.',
        'Writ = sealed royal order; the basis of later chancery government.',
        'Trial by combat = Norman import; Anglo-Saxon oath-helpers and ordeals continued.',
    ])),
]

D["N43-domesday-economy-and-towns"] = [
    SEC('📖 Detailed Notes: Reading Domesday as Evidence', UL([
        '<strong>What a Domesday entry looks like:</strong> "In Earl Tochi\u2019s manor of [X] stood 12 villani, '
        '6 bordarii, 4 slaves; ploughs: 8 in lordship, 12 men\u2019s; woodland for 500 pigs; 2 mills; value before '
        '1066 £12, now 100 shillings." Every number is a fiscal unit — the survey\u2019s genius was standardising '
        'the whole kingdom into comparable values.',
        '<strong>The "waste" entries:</strong> Yorkshire\u2019s wapentakes record value falling from £12 to 4 '
        'shillings — quantitative proof of the harrying, 16 years later. Historians still argue how far "waste" '
        'means destruction versus tax exemption, but the human evidence (Orderic, the Chronicle) backs devastation.',
        '<strong>Tenurial revolution in numbers:</strong> of £73,000 of recorded lay revenue in 1086, roughly '
        'half belonged to 11 barons; the king kept ~17% directly; the Church held ~26%. Two hundred years of '
        'English land law was rewritten in one reign.',
        '<strong>Towns in Domesday:</strong> boroughs listed by houses, rents and mints — York\u2019s houses '
        'destroyed in 1069 counted and taxed; London omitted (its power was too great to survey).',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Great Domesday = condensed; Little Domesday = East Anglia (unfinished).',
        'Inquest juries = sworn local panels — the "sworn inquest" method.',
        'Values compared 1066 vs 1086 — "waste" = harrying evidence.',
        'Boroughs: castle + market + mint + Jewish house.',
        'London NOT surveyed — royal power already there.',
    ])),
]

D["N44-village-life-and-peasants"] = [
    SEC('📖 Detailed Notes: A Year on the Manor', UL([
        '<strong>Autumn:</strong> ploughing and sowing winter wheat; boon-work at peak; harvest bonus meals at '
        'the lord\u2019s table (fattened goose). <strong>Winter:</strong> threshing, hedging, killing and salting '
        'meat; Christmas "misrule" inversion. <strong>Spring:</strong> oat/barley sowing, lambing. <strong>Summer:</strong> '
        'haymaking, sheepshearing, weeding; the fight against weeds and birds with children\u2019s help.',
        '<strong>The manor court:</strong> the lord\u2019s steward presided; villeins judged neighbours on custom '
        '("the memory of man"); fines recorded in court rolls — our best evidence for village life. Cases: stray '
        'pigs in the lord\u2019s wood, unfixed fences, overdue week-work, brewing without licence (ale-tasters).',
        '<strong>Women:</strong> brewed ale (the main drink), spun wool, managed poultry and dairy; widows held '
        'land (dower) and could trade in boroughs; but merchet and fines targeted their marriages.',
        '<strong>The three-field system</strong> spread under the Normans: winter wheat, spring barley/oats, '
        'fallow — more food, more population, more plough teams (and Domesday\u2019s plough counts show it).',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Villein week-work 2–3 days + boon-work at harvest.',
        'Dues: merchet (marriage), heriot (death), tallage (random), chevage (leaving).',
        'Manor court: steward presides, custom is law, fines recorded on rolls.',
        'Slaves ~10% in 1086 → extinct by c1120 (Church influence + economics).',
        'Three-field rotation spread — population and plough counts rise.',
    ])),
]

D["N45-town-life-trade-and-jews"] = [
    SEC('📖 Detailed Notes: A Borough\u2019s Anatomy', UL([
        '<strong>The castle end:</strong> motte/keep + bailey, sited over the river crossing or road junction — '
        'taxing every cart. <strong>The market place</strong> beside the castle gate: charter days, tolls, '
        'stalls; <strong>the mint</strong> nearby (moneyers under bond). <strong>Parish churches</strong> for '
        'English townsfolk; a synagogue near the Jewish quarter; the French borough\u2019s separate streets '
        '(Nottingham, Norwich).',
        '<strong>Trade goods:</strong> wool and woollen cloth to Flanders; Danzig/Norwegian furs and fish; '
        'Rouen wine; Lincolnshire\u2019s wool; Stamford\u2019s pottery. Fairs (Winchester\u2019s St Giles) '
        'drew international merchants.',
        '<strong>Jewish life:</strong> a stone house (Moses\u2019 house in Lincoln survives) signalled permanence; '
        'loans to abbeys (Bury St Edmunds) and to the crown; <strong>archa</strong> — the official chest recording '
        'every debt, enforced in royal courts. The protection-exploitation duality: Henry I\u2019s charter (c1130) '
        'guaranteed safety and free movement; Rufus demanded cash from the same community.',
        '<strong>Urban self-government begins:</strong> burgage tenure (rent-paying instead of labour), borough '
        'customs, merchant guilds — Norman towns taught England commerce.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Castle over the crossing = toll power; French borough = separate merchant streets.',
        'Jews from Rouen c1070; archa = royal debt-chest; Rufus extorted, Henry I chartered.',
        'Wool to Flanders; mints under royal bond; burgage tenure = rent not labour.',
        'Guilds: mutual aid + trade control; fairs drew foreigners.',
        'Expulsion came 1290 (Edward I) — 200 years AFTER the conquest.',
    ])),
]

D["N46-church-monasticism-and-lanfranc"] = [
    SEC('📖 Detailed Notes: Monasticism and the Monastic Constitution', UL([
        '<strong>New houses:</strong> Lewes (Cluniac, 1077 — first priory of a French mother house), Battle Abbey '
        '(on Hastings field itself — William\u2019s penance-vow, 1070s), Durham\u2019s monastic cathedral. Monks '
        'became bishops (Walkelin at Winchester, Gundulf at Rochester) — the "monastic bishop" was a Norman '
        'signature.',
        '<strong>Lanfranc\u2019s Constitutions (c1077):</strong> a handbook for Christ Church, Canterbury — '
        'claustral discipline, obediencies, schooling for boys in the cloister. It spread across English '
        'monasteries and is our best window into monastic daily life (prayers, work, reading in strict rotation).',
        '<strong>Parish revolution:</strong> tithe enforced as a compulsory tenth of produce; parish boundaries '
        'fixed (many still trace them); baptism/marriage/burial regulated — the Church penetrated village life '
        'more deeply after 1066 than before.',
        '<strong>William vs the Pope:</strong> Gregory VII demanded fealty (1080); William refused but promised '
        'payment of Peter\u2019s Pence and no papal letters in England without royal permission — '
        '"I consented to be his liege man for my salvation; fealty for my kingdom I never promised". Royal '
        'control of the Church, unusually strong in Europe.',
        '<strong>Anselm:</strong> a scholar-saint (Proslogion, Cur Deus Homo) forced on Canterbury in 1093; his '
        'quarrel with Rufus over investiture and the schismatic popes (Urban vs Clement) sent him into exile — '
        'the template for Becket\u2019s later conflict.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Lewes 1077 = first Cluniac priory; Battle Abbey = penance on the battlefield.',
        'Lanfranc\u2019s Constitutions c1077 = monastic rulebook for Christ Church.',
        'Tithe compulsory; parish boundaries fixed (still traceable).',
        'William 1080: no fealty to the pope — payment and permission only.',
        'Anselm vs Rufus = the First Quarrel; exile 1097–1100.',
    ])),
]

D["N47-norman-architecture-historic-environment-castles"] = [
    SEC('📖 Detailed Notes: Reading a Castle in the Exam', UL([
        '<strong>Site choice:</strong> castles sit on high ground, river crossings, Roman roads and OLD Anglo-Saxon '
        'burhs — controlling trade and old power, not just views. Pevensey: inside a Roman Saxon Shore fort '
        '(recycled walls — Norman pragmatism). Durham: peninsula defended by river on three sides, cathedral '
        'beside castle.',
        '<strong>The motte:</strong> up to 10m high, using dumped earth (sometimes a demolished Anglo-Saxon '
        'church or Roman rubble); the wooden tower on top = look-out, last refuge, lord\u2019s hall. '
        '<strong>The bailey:</strong> stables, granary, smithy, barracks, chapel; palisade + ditch. '
        '<strong>Ringworks</strong> (bailey-only with motte-less design) appear where bedrock prevented motting.',
        '<strong>Stone phases:</strong> tower keeps (Colchester c1076, White Tower c1078, Rochester 1127) — walls '
        'up to 4m thick at the base; entrance at FIRST-FLOOR level (defensive); chapel inside; well shafts '
        'through the core. Shell keeps (Arundel, Carisbrooke) convert palisades to stone circles. Gatehouses '
        'grow towers by the 12th century.',
        '<strong>Symbolism:</strong> sited opposite an English minster (Norwich cathedral vs castle); bay-windowed '
        'halls in the bailey; the mound\u2019s very shape = a permanent statement that the world had changed. '
        'Chroniclers called castles "the bones of the conquest" — today\u2019s phrase "fossils of feudalism".',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'MotTE 5–10m; timber tower + palisade; built in DAYS with forced labour.',
        'White Tower c1078 (Gundulf): 27m+ corners, Caen stone, first-floor entrance.',
        'Durham 1072 castle / 1093 cathedral — peninsula site; monastic cathedral.',
        'Shell keeps (Arundel, Carisbrooke) = stone palisades on old mottes.',
        'Phase-reading: timber (1066–70s) → stone keep (1080s–90s) → gatehouse/tower upgrades (12th century).',
    ])),
]

D["A40-plains-indians-way-of-life"] = [
    SEC('📖 Detailed Notes: Bands, Beliefs and the Horse', UL([
        '<strong>Bands:</strong> named after a leader\u2019s quality (e.g. "Sore Back Band"); members could leave — '
        'consent ran both ways; band chiefs chosen for generosity, bravery and wisdom; a council of elders and '
        'societies (e.g. fox soldiers) kept order on the summer camp. <strong>Tribal councils</strong> (the Seven '
        'Council Fires of the Lakota) met rarely — usually for war or the Sun Dance.',
        '<strong>Women\u2019s power:</strong> the tipi AND its contents were the woman\u2019s property; women '
        'decamped the band if they lost faith in the chief; they tanned hides, butchered, raised children, ran the '
        'home — and traded (pemmican). Marriages arranged with bride-wealth in horses.',
        '<strong>War as institution:</strong> war societies (Badgers, Foxes) policed the hunt; coups counted '
        'higher than kills; prisoners often adopted (losing a son meant gaining one). War was about HONOUR, '
        'not territory — the fatal cultural mismatch with US total war.',
        '<strong>The Sun Dance:</strong> annual renewal — dancing around the sacred pole, sometimes self-torture '
        '(Sun Dance Piercing) for visions; banned by Washington in the 1880s as part of assimilation.',
        '<strong>The horse (Spanish origin, spread 1600s–1750):</strong> a warrior\u2019s wealth counted in horses '
        '(stolen from other bands = double honour); hunting radius exploded; the Comanche became a horse empire.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Band 10–30 tipis; tribe = summer alliance (Seven Council Fires).',
        'Women owned the tipi; could veto a chief by decamping.',
        'Counting coup = touch, not kill; war societies policed hunts.',
        'Wakan Tanka; the circle; visions sought at the Sun Dance.',
        'Horses = wealth; bride-wealth paid in horses.',
    ])),
]

D["A41-homesteaders-and-the-railroads"] = [
    SEC('📖 Detailed Notes: Homesteader Problems and Solutions, Paired', UL([
        '<strong>Drought and low rainfall:</strong> the 100th meridian (roughly the Dakotas–Texas line) marked '
        'dry country; 160 acres (chosen for WETTER eastern land) could not support a family in the west. '
        'Solutions: dry farming (dust-mulch), deep-well windmills (self-regulating pumps), drought-resistant '
        'Turkey Red wheat brought by Mennonites from Russia.',
        '<strong>Building materials:</strong> no trees on the prairie → <strong>sod houses</strong> ("soddies" — '
        'warm in winter, cool in summer, roofed leaks); rail-borne lumber once lines arrived. '
        '<strong>Fuel:</strong> buffalo and cow chips burned.',
        '<strong>Fencing:</strong> wood was scarce and crops/animals wandered — <strong>barbed wire (Glidden '
        '1874)</strong> ended open-range grazing and protected crops; fence-cutting wars followed.',
        '<strong>Isolation:</strong> 20+ miles to town; women\u2019s loneliness documented in diaries; rural '
        'churches and schools (one-room, all-ages) built community; mail-order catalogues (Montgomery Ward 1872) '
        'transformed consumption.',
        '<strong>Debt and panic:</strong> machinery on credit; the Panic of 1873 and falling prices squeezed '
        'farmers → Granger movement and (later) Populism.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Homestead Act 1862: 160 acres, 5 years, $18 fee, 21+/head of household.',
        'Sod houses; buffalo-chip fuel; Turkey Red wheat; dry farming.',
        'Barbed wire 1874 (Glidden); windmills (deep wells).',
        'Exodusters 1879 → Kansas; railroad land sales $2–10/acre.',
        'Panic of 1873 → Grange; loneliness documented by women\u2019s diaries.',
    ])),
]

D["A42-cattle-industry-and-open-range"] = [
    SEC('📖 Detailed Notes: The Drive, Season by Season', UL([
        '<strong>Spring round-up:</strong> cowboys from neighbouring ranches swept the range, branding calves; '
        'herds assembled at trailheads (Seymour, Texas). <strong>The drive:</strong> 3–4 months to Abilene/Dodge; '
        'two men per 250 head; night shifts singing to calm stampedes; rivers (Red, Arkansas) the danger points; '
        'storm and stampede losses ~3–5%. <strong>Sale and return:</strong> paid off at the railhead; gambling, '
        'whiskey, the legendary (short) visit to town; back to Texas with wages.',
        '<strong>Cow towns:</strong> Abilene (1867–71), Ellsworth, Wichita, <strong>Dodge City (1872–85)</strong> — '
        'mayors and marshals (Bat Masterson, Wyatt Earp) imposed ordinance zones (gun-free north side). '
        '<strong>Ranching move north:</strong> open-range empires (the XIT, the Swan) with line camps and '
        'romantic-sounding brands.',
        '<strong>The collapse:</strong> overstocking (2m head on the range by 1885), the drought of 1886 and '
        '<strong>the Big Die-Up (1886–87)</strong> — cattle frozen/starved in blizzards; absentee investors ruined '
        '(the Edinburgh-backed Swan lost everything). Aftermath: hay farms, fenced pastures, winter feed, purebred '
        'breeding — the rancher replaced the drover.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'McCoy 1867 Abilene; $4 Texas / $40 northern head.',
        'Drive: 3–4 months, 10–15 miles/day, ~1,500–3,000 head, 8–12 crew.',
        'Dodge City 1872–85; Bat Masterson/Wyatt Earp as marshals.',
        'Big Die-Up 1886–87: up to 90% losses; overstocking + drought + blizzard.',
        'After 1890: fenced ranches, hay, purebreds — and the Johnson County War (1892).',
    ])),
]

D["A43-conflict-reservations-and-wounded-knee"] = [
    SEC('📖 Detailed Notes: Policy Timeline in Detail', UL([
        '<strong>1851 Fort Laramie:</strong> first great council — tribes assigned territories, US promised '
        'annuities; the "concentration" policy begins.',
        '<strong>1864 Sand Creek:</strong> Colorado volunteers under <strong>Colonel John Chivington</strong> '
        'attacked Black Kettle\u2019s peaceful Cheyenne (~150 dead, mostly women/children, scalps displayed in '
        'Denver) — northern outrage, but the pattern repeated.',
        '<strong>1866–68 Red Cloud\u2019s War:</strong> the Bozeman Trail through Lakota land; Fetterman\u2019s '
        '81 men ambushed and wiped out; the US <strong>abandoned the forts</strong> and signed the 1868 Treaty '
        '(the Great Sioux Reservation — "as long as the grass grows").',
        '<strong>1874 Custer\u2019s Black Hills expedition found gold</strong> → miners flooded in → government '
        'bought-or-took the Hills (1876) → Sitting Bull and Crazy Horse\u2019s victories (Rosebud, Little Bighorn '
        '25 June 1876 — Custer\u2019s 210+ dead) → the army\u2019s winter campaign broke the tribes (Crazy Horse '
        'killed 1877; Sitting Bull fled to Canada, returned 1881).',
        '<strong>Assimilation:</strong> boarding schools ("kill the Indian, save the man" — Carlisle 1879), '
        'Christian missions, the <strong>Dawes Act 1887</strong> (allotment: 160-acre family plots, "surplus" '
        'sold — 2/3 of reservation land lost by 1934). <strong>Ghost Dance 1890</strong> (Wovoka\u2019s vision: '
        'the buffalo return, the whites vanish) → panic → Sitting Bull killed (15 Dec 1890) → '
        '<strong>Wounded Knee (29 Dec 1890)</strong>: Hotchkiss guns fired on fleeing Lakota — ~250–300 dead; '
        'the last armed resistance.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        '1851 → 1868 treaties; both broken by gold and railroads.',
        'Sand Creek 1864 (Chivington); Fetterman 1866; Red Cloud won his war.',
        'Black Hills gold 1874 → Custer 1876 → winter campaigns 1876–77.',
        'Dawes 1887 = allotment; boarding schools = cultural war.',
        'Ghost Dance → Sitting Bull killed → Wounded Knee 29 Dec 1890.',
    ])),
]

D["R40-tsarist-russia-and-the-1905-revolution"] = [
    SEC('📖 Detailed Notes: Opposition Parties and Stolypin\u2019s Gamble', UL([
        '<strong>Kadets (1905):</strong> constitutional democrats — lawyers, zemstvo gentry; wanted a British-style '
        'parliament; led the first Duma. <strong>Socialist Revolutionaries:</strong> peasants\u2019 party, land '
        'socialisation, the Combat Organisation\u2019s terror (killed Plehve 1904, Grand Duke Sergei 1905). '
        '<strong>Social Democrats:</strong> Marxist factory party; the 1903 split — <strong>Bolsheviks</strong> '
        '(Lenin: disciplined cadre party) vs <strong>Mensheviks</strong> (mass party, two-stage revolution).',
        '<strong>Bloody Sunday in detail:</strong> ~150,000 marched with portraits of the Tsar and Gapon\u2019s '
        'petition (an 8-hour day, a constituent assembly); troops fired at the Winter Palace square; official '
        'figure 96 dead, contemporary claims 200–1,000. "We have no Tsar" — the loyalty myth broken.',
        '<strong>The 1905 sweep:</strong> the Potemkin mutiny (June), the All-Russian railway strike (October), '
        'the St Petersburg Soviet (Trotsky\u2019s platform), peasant seizure of estates; Witte negotiated the '
        'Manifesto while returning from Portsmouth (the peace treaty with Japan).',
        '<strong>Stolypin (PM 1906–11):</strong> field courts-martial (3,800 hanged — "Stolypin\u2019s necktie"); '
        'dissolved the 1st and 2nd Dumas; changed the electoral law (1907) to favour landowners — '
        '<strong>the "coup of June 1907"</strong>; his land reform let peasants leave the mir and consolidate '
        '(khutors) — 2m used it by 1914; assassinated in Kiev (1911).',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Parties: Kadets (liberals) · SRs (peasants/terror) · SDs (Marxists; Bolshevik/Menshevik split 1903).',
        'Bloody Sunday 22 Jan 1905 — Gapon; "we have no Tsar".',
        'October Manifesto: liberties + Duma; Fundamental Laws took it back (Apr 1906).',
        'Stolypin: necktie, wager on the strong, 1907 coup; assassinated 1911.',
        'Russo-Japanese defeat (Portsmouth treaty, Sep 1905) weakened the regime.',
    ])),
]

D["R41-1917-february-october-and-dual-power"] = [
    SEC('📖 Detailed Notes: Eight Months Between Revolutions', UL([
        '<strong>February in detail:</strong> International Women\u2019s Day (23 Feb) bread protests joined by '
        'Putilov strikers; 25 Feb general strike; 26 Feb troops fire; 27 Feb the Volhynia regiment mutinies — '
        'the capital falls; the Duma\u2019s Provisional Committee + the Petrograd Soviet form (Order No. 1: '
        'soldiers obey the Soviet, not officers); Nicholas\u2019s train halted; abdication for himself and Alexei '
        '(2 March); Michael refuses the throne.',
        '<strong>The PG\u2019s fatal eight:</strong> stayed in the war (Milyukov\u2019s note promising victory '
        'provoked the April Crisis); postponed land reform to the Constituent Assembly; delayed elections; '
        'amnesty but no real change; food rationing worsened; Lenin\u2019s return (sealed train, April); '
        'July Days (Kerensky blamed Lenin — German-agent smear); Kornilov (August) — Kerensky panicked, '
        'asked the Bolsheviks to defend Petrograd, then branded Kornilov a counter-revolutionary; the Red '
        'Guard kept its rifles.',
        '<strong>October in detail:</strong> Trotsky\u2019s MRC under the Petrograd Soviet banner; 24–25 October: '
        'bridges, telegraph, stations, Winter Palace (Aurora\u2019s blank shot); Second Congress of Soviets '
        'ratifies; Sovnarkom: Lenin (chair), Trotsky (foreign), Stalin (nationalities).',
    ])),
    SEC('⚡ Targeted Drills', UL([
        '23 Feb women\u2019s day protests → 27 Feb garrison mutiny → 2 Mar abdication.',
        'Order No. 1 = soldiers obey the Soviet.',
        'April Theses: peace, bread, land; all power to the Soviets.',
        'July Days crushed; Kornilov armed the Bolsheviks.',
        '24–25 Oct: MRC seizure; Sovnarkom (Lenin, Trotsky, Stalin).',
    ])),
]

D["R42-civil-war-war-communism-and-nep"] = [
    SEC('📖 Detailed Notes: Why the Reds Won — Factor by Factor', UL([
        '<strong>Geography:</strong> the Red core held Petrograd, Moscow and the railway spoke — interior lines; '
        'the Whites fought on four peripheral fronts (Kolchak from Siberia, Denikin from the south, Yudenich from '
        'Estonia, Miller from the north) that never linked.',
        '<strong>Organisation:</strong> Trotsky\u2019s armoured-train command tour; 50,000 ex-Tsarist officers '
        '(military specialists) watched by commissars; hostages and decimation enforced discipline; the Red Army '
        'grew from ~100,000 to 5,000,000.',
        '<strong>Politics:</strong> the Whites stood for restoring a broken past (landowners would return land); '
        'the Reds defended the peasants\u2019 land seizure — even peasants who hated requisitioning feared White '
        'victory more; national minorities feared White "Russia One and Indivisible".',
        '<strong>Terror as policy:</strong> the Cheka (Dzerzhinsky); Red Terror declared Sept 1918 (after Uritsky '
        'and the Lenin shooting); 50,000+ shot; class-hostage system. <strong>War Communism</strong> fed cities '
        'by starving villages (prodrazvyorstka took "surplus", really seed grain).',
        '<strong>Aftermath:</strong> ~10m dead (war + famine + terror); Kronstadt (March 1921) — the sailors of '
        '1917 rose for "Soviets without Bolsheviks"; Tukhachevsky stormed the ice fortress; the NEP followed '
        'within days of the final suppression.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'White fronts: Kolchak (E), Denikin (S), Yudenich (NW), Miller (N) — never linked.',
        'Trotsky: ex-officers + commissars; decimation; armoured trains.',
        'War Communism: prodrazvyorstka; ban on private trade; nationalisation.',
        'Famine 1921–22 (~5m); American Relief Administration fed millions.',
        'Kronstadt Mar 1921 → NEP 10th Party Congress (same month).',
    ])),
]

D["R43-stalin-collectivisation-plans-and-terror"] = [
    SEC('📖 Detailed Notes: The Machine of Transformation', UL([
        '<strong>Five-Year Plans in detail:</strong> 1st Plan (1928–32) heavy industry; Magnitogorsk built on the '
        'steppe (25,000 a month arrived); Dnieper dam (Dneprostroi); white-coal electricity; workers\u2019 rationing '
        'and barracks; <strong>Stakhanov (1935)</strong> — 102 tons of coal in a shift, the Stakhanovite movement '
        'raising norms. 2nd/3rd Plans: chemicals, machine tools, armaments (the 3rd cut short by Barbarossa).',
        '<strong>Collectivisation mechanics:</strong> 25,000ers (urban volunteers) sent to enforce; kolkhoz '
        'chairmen elected by quota; <strong>de-kulakisation</strong> — "liquidation as a class": transport in '
        'cattle trucks to Siberia (~2m deported); grain targets took seed corn → the 1932–33 famine (Ukraine '
        'hardest — the Holodomor; ~3.5–5m Ukrainian dead); internal passports (1932) chained peasants to land '
        'the serfs\u2019 way.',
        '<strong>Terror mechanics:</strong> Kirov shot (1 Dec 1934) — likely with Stalin\u2019s knowledge; '
        '"terror railway" legislation; <strong>show trials</strong> (Zinoviev/Kamenev Aug 1936; Pyatakov Jan 1937; '
        'Bukharin/Rykov Mar 1938) — rehearsed confessions, families threatened; the Tukhachevsky case (June 1937) '
        'gutted the army (3/5 marshals, 13/15 army commanders); <strong>Yezhovshchina</strong>: ~750,000 shot '
        '(1937–38), gulag population ~2m; Yezhov himself purged (1939), replaced by Beria.',
        '<strong>Culture of control:</strong> Socialist Realism (the only permitted art); history rewritten; '
        'children informed (Pavlik Morozov myth); churches dynamited or closed.',
    ])),
    SEC('⚡ Targeted Drills', UL([
        '25,000ers enforced collectivisation; kolkhoz quotas; machine tractor stations.',
        'Famine 1932–33: Ukraine (Holodomor) ~3.5–5m; internal passports 1932.',
        'Magnitogorsk; Dnieper dam; Stakhanov 1935 (102 tons).',
        'Show trials 1936/37/38; Tukhachevsky June 1937; Yezhov → Beria.',
        'Cult: Corypheus; Socialist Realism; Pavlik Morozov myth.',
    ])),
]

D["C40-origins-of-the-cold-war-1945-49"] = [
    SEC('📖 Detailed Notes: Conferences and Crises, Line by Line', UL([
        '<strong>Yalta (4–11 Feb 1945):</strong> Germany into four zones; free elections PROMISED in Poland; '
        'the Lublin (Soviet) Poles to be "broadened"; the UN agreed (USSR a permanent Security Council member). '
        'Stalin kept his word on nothing Poland-related — the Katyn truth was already known in London.',
        '<strong>Potsdam (17 Jul–2 Aug 1945):</strong> Truman had the bomb (tested 16 Jul); Attlee replaced '
        'Churchill mid-conference; the Oder-Neisse line de facto; reparations taken by each occupier from their '
        'own zone (the USSR stripped its zone — and East Germany — bare); Nazis demilitarised/denazified.',
        '<strong>The Iron Curtain in detail:</strong> 1945–48 coups and rigged votes: Romania (Feb 1947), Poland '
        '(Jan 1947 referendum fraud), Hungary (1947 "salami tactics" against Smallholders), Czechoslovakia (Feb '
        '1948 — the only genuine democracy, lost last); Tito\u2019s Yugoslavia expelled from Cominform (1948) — '
        'proof communism was not monolithic.',
        '<strong>Berlin blockade mechanics:</strong> 23 June 1948 the Deutschmark introduced in the western zones; '
        'Stalin closed road/rail/canal on 24 June; 2.2m West Berliners needed 4,000 tonnes/day; the airlift '
        'peaked at 1,500 flights/day (Operation Vittles); Stalin lifted it 12 May 1949 — the Allies kept their '
        'zone and founded the FRG (May 1949); the GDR answered (October 1949); NATO (4 April 1949).',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Yalta: zones + UN + promised elections; Potsdam: Truman/Attlee + reparations rows.',
        'Fulton Mar 1946 ("From Stettin in the Baltic to Trieste in the Adriatic").',
        'Truman Doctrine Mar 1947 ($400m Greece/Turkey); Marshall $13bn; Czech coup Feb 1948.',
        'Blockade 24 Jun 1948–12 May 1949; 1,500 flights/day peak; NATO 4 Apr 1949.',
        'FRG May 1949 / GDR Oct 1949 — two Germanies.',
    ])),
]

D["C41-hungary-1956-and-the-berlin-wall-1961"] = [
    SEC('📖 Detailed Notes: Two Crises in Detail', UL([
        '<strong>Hungary timeline:</strong> Riots in Poland (Poznañ, June) emboldened Budapest; 23 Oct students '
        'demonstrated (statue of Stalin pulled down — only his boots remained); Nagy returned as PM; 28 Oct '
        'Soviet troops withdrew; 1 Nov Nagy announced NEUTRALITY and Warsaw Pact withdrawal; 4 Nov 60,000 Soviet '
        'troops + tanks (Operation Whirlwind, Konev) crushed the resistance (Coravin Cinema, Kilian Barracks); '
        'Cardinal Mindszenty sheltered in the US embassy (15 years); ~200,000 refugees; Nagy kidnapped from '
        'Yugoslav embassy, tried secretly, hanged June 1958.',
        '<strong>The West\u2019s dilemma:</strong> Eisenhower refused "rollback" that meant world war; Radio Free '
        'Europe had ENCOURAGED the rising — moral responsibility without capability; Suez (31 Oct–6 Nov) split '
        'the alliance precisely when Hungary burned.',
        '<strong>Berlin in detail:</strong> Khrushchev\u2019s Nov 1958 ultimatum (six months to a free city) — '
        'expired, bluffed, repeated; the "brain drain": doctors, engineers, teachers (the GDR trained them); '
        '13 Aug 1961 bars barbed wire overnight; two days later concrete; Ulbricht\u2019s phrase "no one intends '
        'to build a wall" (June 1961); Peter Fechter bled to death at the wall (17 Aug 1962) — the image of the '
        'era; Checkpoint Charlie tank stand-off (Oct 1961 — 16 hours, tanks 100m apart).',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Poznañ June 1956 → Budapest 23 Oct → neutrality 1 Nov → invasion 4 Nov.',
        'Mindszenty in the US embassy 15 years; Nagy hanged Jun 1958.',
        'Ultimatum Nov 1958 failed; ~3m fled; Wall 13 Aug 1961.',
        'Peter Fechter Aug 1962; Checkpoint Charlie tank stand-off Oct 1961.',
        "Kennedy: 'Ich bin ein Berliner' Jun 1963.",
    ])),
]

D["C42-cuban-missile-crisis-1962"] = [
    SEC('📖 Detailed Notes: Thirteen Days, Hour by Hour', UL([
        '<strong>Background chain:</strong> Castro\u2019s victory (Jan 1959) → US embargo (1960) → Bay of Pigs '
        '(17 Apr 1961) → Operation Anadyr (Soviet deployment, Sep 1962 — R-12s with 1-megaton warheads, 42,000 '
        'troops). <strong>14 Oct:</strong> Major Heyser\u2019s U-2 photographs San Cristóbal; 16 Oct Kennedy '
        'briefed ("we have some photographs").',
        '<strong>ExComm options:</strong> (1) do nothing; (2) diplomatic pressure; (3) secret approach to Castro; '
        '(4) invasion; (5) surgical air strike; (6) blockade — chosen as the middle option (legally "quarantine" '
        '— blockade is an act of war); OAS endorsement obtained.',
        '<strong>The 13 days:</strong> 22 Oct TV address; 24 Oct Soviet ships stop/turn at the line; 25 Oct '
        'Stevenson at the UN ("until hell freezes over"); 26 Oct Khrushchev\u2019s first letter (withdrawal for '
        'a pledge); 27 Oct the second letter (Turkish missiles) + <strong>Black Saturday</strong> — U-2 downed '
        '(Major Anderson killed), B-59 submarine depth-charged (considered a nuclear torpedo), U-2 strayed into '
        'Siberian airspace; Kennedy answered the FIRST letter and ignored the second; the Trollope ploy; RFK-'
        'Dobrynin night meeting sealed the Jupiter trade.',
        '<strong>Aftermath:</strong> missiles crated and shipped; UN inspection refused; the hotline (30 Aug 1963); '
        'Test Ban Treaty (Moscow, Aug 1963); Khrushchev celebrated quietly then fell (Oct 1964 — blamed for '
        'Cuba among other things); Castro felt betrayed ("the missiles were ours to decide").',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'U-2 photos 14 Oct; Kennedy briefed 16 Oct; TV address 22 Oct.',
        'Quarantine line 24 Oct; ships stop 25 Oct.',
        'Two letters 26/27 Oct; Trollope ploy; RFK-Dobrynin deal.',
        'Black Saturday: Anderson\u2019s U-2; B-59 depth charges.',
        'Hotline 30 Aug 1963; Test Ban Aug 1963; Khrushchev out Oct 1964.',
    ])),
]

D["C43-vietnam-detente-and-the-collapse"] = [
    SEC('📖 Detailed Notes: From Escalation to Collapse', UL([
        '<strong>Vietnam mechanics:</strong> Diem\u2019s assassination (Nov 1963); Gulf of Tonkin (2/4 Aug 1964) '
        'resolution = blank cheque; Rolling Thunder (1965); ground troops from Da Nang (Mar 1965); search-and-'
        'destroy, hammers and anvils; the Ho Chi Minh Trail through Laos/Cambodia; <strong>Tet (Jan 1968)</strong> '
        '— 80,000 NVA/VC attacked 100+ towns: military defeat, propaganda victory (Walter Cronkite: "we are "'
        'mired in stalemate"); LBJ declines re-election; Nixon\u2019s Vietnamisation + Cambodia incursion (1970); '
        'Paris Accords (Jan 1973); Saigon falls 30 Apr 1975 (helicopters off the embassy roof).',
        '<strong>Détente mechanics:</strong> SALT I (May 1972): ABM treaty + interim freeze; trade deals (US grain '
        'to USSR); <strong>Helsinki (Aug 1975)</strong>: three baskets — borders recognised (irony: dissidents '
        'used the human-rights basket), exchanges, human rights; Angola/Ethiopia proxy wars strained it; SALT II '
        'signed (Jun 1979) but shelved after Afghanistan.',
        '<strong>The end-game:</strong> Polish Solidarity (1980, martial law 1981); Reagan: build-up, SDI (Mar '
        '1983), Able Archer scare (Nov 1983); Gorbachev (1985): Geneva, Reykjavik (Oct 1986 — SDI blocked total '
        'disarmament), INF (Dec 1987 — 2,692 missiles destroyed with inspections); unilaterals; Afghanistan '
        'withdrawal (1988–89); Eastern Europe 1989 (Hungary opens the border May; Poland\u2019s June elections; '
        'Leipzig Monday demonstrations; Honecker out Oct; <strong>Schabowski\u2019s press-conference mistake, '
        'Wall opened 9 Nov</strong>); Bulgaria/Romania (Ceausescu shot 25 Dec); Baltic way; August coup (Yanayev) '
        'defeated by Yeltsin on the tank; Ukraine referendum (1 Dec); USSR dissolved (8/25 Dec 1991).',
    ])),
    SEC('⚡ Targeted Drills', UL([
        'Gulf of Tonkin Aug 1964; Tet Jan 1968; Saigon 30 Apr 1975.',
        'SALT I May 1972; Helsinki Aug 1975; Afghanistan Dec 1979; SDI Mar 1983.',
        'INF Dec 1987 — first deletion treaty; unilateral cuts 1988.',
        'Wall 9 Nov 1989 — Schabowski\u2019s live-TV mistake.',
        'Coup Aug 1991 (Yeltsin on the tank); dissolution 25 Dec 1991.',
    ])),
]

if __name__ == "__main__":
    only = None
    if len(sys.argv) > 2:
        only = set(sys.argv[2].split(','))
    n = 0
    for f in glob.glob('topics/history/*/*.html'):
        base = os.path.basename(f)[:-5]
        if base not in D or (only and base not in only):
            continue
        h = open(f, encoding='utf-8').read()
        for sec_html in D[base]:
            m = re.search(r'<h2>([^<]+)</h2>', sec_html)
            t = m.group(1).split(':')[0].split(' — ')[0].strip()
            if t in h:
                continue
            for anchor in ('⚠️ Common Errors', '🎯 Exam Tips', '🗺️ In the Exam'):
                h2, ok = insert_before_section(h, anchor, sec_html)
                if ok:
                    open(f, 'w', encoding='utf-8').write(h2)
                    n += 1
                    break
    print(f'sections injected: {n}')
