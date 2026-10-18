from .core import gaps, meanings, explicit, LESSONS, question
from .actions import ACTIONS

voice_labels={
 'process':('A process in the present passive','Werden plus a past participle presents an action being carried out, with the patient as subject.'),
 'state':('A resulting state','Sein plus the participle describes the resulting condition, rather than the action of producing it.'),
 'future':('A future active event','Werden plus infinitive is Futur I; it does not turn the subject into the patient of an action.'),
 'activeperfect':('A completed active event','Haben/sein plus participle without passive worden can be an active Perfekt construction.'),
}
for action in ACTIONS[:10]:
    patient,plural,part,inf,present,past,obj,zu=action
    for unit,correct,wrong,tense in [
        (129,'werden' if plural=='1' else 'wird',['ist','sind','haben'],'present'),
        (130,'wurden' if plural=='1' else 'wurde',['wird','werden','hat'],'past'),
        (131,'worden',['geworden','werden','gewerden'],'perfect')]:
        prompt=f'{patient} '+('sind' if plural=='1' else 'ist')+f' {part} ___. (Perfekt des Vorgangspassivs)' if unit==131 else f'{patient} ___ {part}. (Vorgangspassiv, {"Präsens" if unit==129 else "Präteritum"})'
        LESSONS.setdefault(unit, []).append(question(prompt,correct,wrong,
            f"The {tense} event passive uses {'sein + participle + worden, never geworden' if unit==131 else 'the agreeing form of werden/wurden + past participle'}; the subject is '{patient}'.",'Complete the specifically requested event-passive form.'))

meanings(129,"""
Der Antrag wird geprüft.|process
Die Tür ist geschlossen. (Zustand)|state
Sie wird morgen kommen.|future
Er hat den Brief geschrieben.|activeperfect
Die Straße wird gesperrt.|process
Die Rechnung ist bezahlt. (Zustand)|state
Wir werden bald reisen.|future
Die Gäste sind angekommen.|activeperfect
Die Geräte werden repariert.|process
Die Fenster sind geöffnet. (Zustand)|state
""",voice_labels,'Identify the construction and its meaning.')

past_voice={
 'past':('A past event in the passive','Wurde/wurden plus participle marks an event passive in Präteritum.'),
 'present':('A present event in the passive','Wird/werden plus participle marks present event passive, not Präteritum.'),
 'active':('A past active event','The subject performs the lexical action; this is active Präteritum.'),
 'state':('A past resulting state','War/waren plus participle describes an existing past state rather than its creation.'),
}
meanings(130,"""
Die Straße wurde gestern gesperrt.|past
Der Antrag wird jetzt geprüft.|present
Anna schrieb gestern den Brief.|active
Die Tür war schon geschlossen. (Zustand)|state
Die Fenster wurden geöffnet.|past
Die Geräte werden repariert.|present
Der Fahrer bemerkte den Fehler.|active
Die Rechnungen waren bezahlt. (Zustand)|state
Der Vertrag wurde unterschrieben.|past
Das Zimmer war aufgeräumt. (Zustand)|state
""",past_voice,'Identify time and voice.')

perfect_voice={
 'passive':('A completed event in the passive','Sein + participle + worden is the Perfekt of the event passive.'),
 'become':('A change of state with lexical werden','Geworden belongs to lexical werden meaning become, not to the event-passive Perfekt.'),
 'active':('A completed active action','Haben plus participle identifies an active Perfekt action here.'),
 'state':('A present resulting state','Sein plus participle without worden describes the resulting state here.'),
}
meanings(131,"""
Der Termin ist verschoben worden.|passive
Sie ist Ärztin geworden.|become
Anna hat die Rechnung bezahlt.|active
Die Tür ist geschlossen. (Zustand)|state
Die Geräte sind repariert worden.|passive
Das Wetter ist besser geworden.|become
Er hat den Vertrag unterschrieben.|active
Die Rechnung ist bezahlt. (Zustand)|state
Die Briefe sind verschickt worden.|passive
Er ist sehr müde geworden.|become
""",perfect_voice,'Distinguish worden, geworden and other perfect/state forms.')

for action in ACTIONS[:10]:
    patient,plural,part,inf,present,past,obj,zu=action
    LESSONS.setdefault(132, []).append(question(f'{patient} '+('müssen' if plural=='1' else 'muss')+' ___.',f'{part} werden',
        [f'{inf} werden',f'werden {part}',f'{part} worden'],
        f"A modal passive ends with participle + werden: '{part} werden'. The subject receives rather than performs the action.",'Complete the modal event-passive construction.'))
passive_modals={
 'required':('The action is required','Muss/müssen … werden states a necessary action in the passive.'),
 'forbidden':('The action is forbidden','Darf/dürfen nicht … werden prohibits carrying out the passive action.'),
 'possible':('The action is possible','Kann/können … werden presents the action as possible.'),
 'noneed':('The action is unnecessary','Muss/müssen nicht … werden removes necessity; it does not prohibit the action.'),
}
meanings(132,"""
Der Antrag muss geprüft werden.|required
Die Datei darf nicht gelöscht werden.|forbidden
Das Gerät kann repariert werden.|possible
Die Rechnung muss nicht sofort bezahlt werden.|noneed
Die Unterlagen müssen eingereicht werden.|required
Hier darf nicht geparkt werden.|forbidden
Die Fragen können später beantwortet werden.|possible
Der Brief muss nicht verschickt werden.|noneed
Die Tür darf nicht geöffnet werden.|forbidden
Die Wohnung kann besichtigt werden.|possible
""",passive_modals,'What does the modal passive permit, require or prohibit?')

meanings(133,"""
Die Tür ist geschlossen. (Zustand)|state
Die Tür wird gerade geschlossen.|process
Anna hat die Tür geschlossen.|activeperfect
Anna wird die Tür schließen.|future
Das Zimmer ist aufgeräumt. (Zustand)|state
Das Zimmer wird gerade aufgeräumt.|process
Er hat das Zimmer aufgeräumt.|activeperfect
Er wird das Zimmer aufräumen.|future
Die Rechnung ist bezahlt. (Zustand)|state
Die Rechnung wird gerade bezahlt.|process
Sie hat die Rechnung bezahlt.|activeperfect
Sie wird die Rechnung bezahlen.|future
Das Fenster ist geöffnet. (Zustand)|state
Das Fenster wird geöffnet.|process
Er hat das Fenster geöffnet.|activeperfect
Er wird das Fenster öffnen.|future
Die Straße ist gesperrt. (Zustand)|state
Die Straße wird jetzt gesperrt.|process
Die Polizei hat die Straße gesperrt.|activeperfect
Die Polizei wird die Straße sperren.|future
""",voice_labels,'Distinguish state passive, event passive, future and active perfect.')

present_attributes=[('warten','wartend','die','Fahrgäste','en'),('spielen','spielend','das','Kind','e'),('lachen','lachend','die','Frau','e'),('arbeiten','arbeitend','der','Mann','e'),('laufen','laufend','die','Motoren','en'),('fehlen','fehlend','die','Unterschrift','e'),('reisen','reisend','die','Menschen','en'),('steigen','steigend','die','Preise','en'),('sinken','sinkend','die','Temperatur','e'),('schlafen','schlafend','das','Baby','e')]
for inf,stem,article,noun,ending in present_attributes:
    correct=stem+ending
    LESSONS.setdefault(134, []).append(question(f'{article.capitalize()} ___ {noun}. ({inf}; Partizip I als Attribut)',correct,
        [stem+'en' if ending=='e' else stem+'e',inf,stem+'em'],
        f"Partizip I is infinitive + d, then an adjective ending: '{correct}'. After the given definite article, use {'-en in plural' if ending=='en' else '-e in nominative singular'}.",'Complete the attributive present participle.'))
    LESSONS[134].append(question(f'Wie versteht man „{article} {correct} {noun}“?', 'The noun is performing the ongoing action.',
        ['The noun has necessarily finished the action.','The noun is necessarily the passive recipient of the action.','The action is explicitly denied.'],
        f"'{correct}' is an active present participle from '{inf}'; it describes an ongoing action associated with '{noun}'.",'Interpret the participial attribute.'))

past_attributes=[('das','repariert','e','Gerät','passive'),('die','geschlossen','e','Tür','passive'),('der','unterschrieben','e','Vertrag','passive'),('die','beschädigt','en','Autos','passive'),('das','gefunden','e','Buch','passive'),('die','angekommen','en','Gäste','active'),('der','eingeschlafen','e','Junge','active'),('die','verblüht','en','Blumen','active'),('das','geöffnet','e','Fenster','passive'),('die','abgereist','en','Teilnehmer','active')]
for article,stem,ending,noun,role in past_attributes:
    correct=stem+ending
    LESSONS.setdefault(135, []).append(question(f'{article.capitalize()} ___ {noun}. (Partizip II: {stem})',correct,
        [stem,stem+'en' if ending=='e' else stem+'e',stem+'em'],
        f"An attributive Partizip II takes adjective endings: '{correct}' agrees with the article and noun.",'Complete the past-participial attribute.'))
    active='The noun itself has undergone the intransitive change.'
    passive='The noun received the action and is described by its result.'
    LESSONS[135].append(question(f'Was bedeutet „{article} {correct} {noun}“?',active if role=='active' else passive,
        [passive if role=='active' else active,'The noun is currently starting the opposite action.','The attribute is a finite verb in the present tense.'],
        f"'{stem}' is {'an intransitive completed change' if role=='active' else 'a completed transitive action affecting the noun'}; not every Partizip II attribute has passive meaning.",'Interpret the noun’s role in the past-participial attribute.'))

long_attrs=[
 ('die gestern im Zug gefundenen Unterlagen','Unterlagen','die Unterlagen, die gestern im Zug gefunden wurden'),
 ('das vom Techniker reparierte Gerät','Gerät','das Gerät, das vom Techniker repariert wurde'),
 ('die vor einer Woche verschickten Briefe','Briefe','die Briefe, die vor einer Woche verschickt wurden'),
 ('der von beiden Seiten unterschriebene Vertrag','Vertrag','der Vertrag, der von beiden Seiten unterschrieben wurde'),
 ('die im Keller gelagerten Kisten','Kisten','die Kisten, die im Keller gelagert werden'),
 ('das an der Ecke neu eröffnete Geschäft','Geschäft','das Geschäft, das an der Ecke neu eröffnet wurde'),
 ('die seit einer Stunde wartenden Fahrgäste','Fahrgäste','die Fahrgäste, die seit einer Stunde warten'),
 ('der im Garten spielende Junge','Junge','der Junge, der im Garten spielt'),
 ('die bereits gestern angekommenen Gäste','Gäste','die Gäste, die bereits gestern angekommen sind'),
 ('das wegen der Baustelle geschlossene Schwimmbad','Schwimmbad','das Schwimmbad, das wegen der Baustelle geschlossen ist'),
]
for phrase,head,paraphrase in long_attrs:
    LESSONS.setdefault(136, []).append(question(f'Was ist das Kernnomen in „{phrase}“?',head,
        ['the first preposition','the participle itself','the time expression'],
        f"'{head}' is the head noun; all preceding modifiers describe it, even when a different noun occurs inside the attribute.",'Find the head noun.'))
    LESSONS[136].append(question(f'Welche Auflösung passt zu „{phrase}“?',paraphrase,
        ['The attribute refers to a different, unnamed head noun.','The phrase denies the action of the participle.','The phrase necessarily describes only a future plan.'],
        'The relative-clause paraphrase keeps the head noun, the participial action and all time/place/agent complements.','Unpack the compressed attribute.'))

gaps(137,'sei|habe|komme|wohne|arbeite|könne|ist|hat|kommt|wohnt|arbeitet|kann',"""
Die Zeitung berichtet, der Fahrer ___ unverletzt. (Konjunktiv I von sein)|sei
Anna sagt, sie ___ Zeit. (Konjunktiv I von haben)|habe
Paul erklärt, er ___ später. (Konjunktiv I von kommen)|komme
Sie berichtet, er ___ in Bonn. (Konjunktiv I von wohnen)|wohne
Er sagt, sie ___ im Büro. (Konjunktiv I von arbeiten)|arbeite
Der Arzt erklärt, er ___ helfen. (Konjunktiv I von können)|könne
Die Leiterin sagt, der Kurs ___ voll. (Konjunktiv I von sein)|sei
Er behauptet, er ___ keine Angst. (Konjunktiv I von haben)|habe
Sie meint, der Bus ___ bald. (Konjunktiv I von kommen)|komme
Die Zeitung schreibt, der Mann ___ allein. (Konjunktiv I von wohnen)|wohne
""", "The explicitly requested Konjunktiv I form '{answer}' marks someone else's reported statement rather than the reporter's own assertion.")

report_labels={
 'report':('A claim attributed to another speaker','The reporting context plus Konjunktiv I marks an attributed claim; the writer does not thereby guarantee it.'),
 'assert':('The speaker’s own indicative statement','The indicative sentence presents the information directly rather than marking it as reported with Konjunktiv I.'),
 'wish':('An unreal wish','Konjunktiv II with doch/gern presents a wished-for or hypothetical state, not Konjunktiv I reported speech.'),
 'question':('A direct request for information','The sentence asks a genuine direct question in this context rather than reporting a claim.'),
}
meanings(137,"""
Die Zeitung berichtet, er sei unverletzt.|report
Ich bin heute zu Hause.|assert
Wenn ich doch mehr Zeit hätte!|wish
Hast du heute Zeit? (echte Frage)|question
Sie erklärt, der Termin sei bestätigt.|report
Der Kurs beginnt um neun. (eigene Mitteilung)|assert
Ich wäre gern am Meer.|wish
Wo wohnst du? (echte Frage)|question
Er sagt, sie habe genug Geld.|report
Die Zeugin erklärt, sie kenne den Fahrer.|report
""",report_labels,'What kind of utterance is this?')

gaps(138,'habe|sei|hat|ist|war|hätte',"""
Der Zeuge sagt, er ___ den Mann gesehen. (Konjunktiv I)|habe
Sie erklärt, sie ___ nach Hause gegangen. (Konjunktiv I)|sei
Er berichtet, er ___ die Rechnung bezahlt. (Konjunktiv I)|habe
Sie sagt, der Zug ___ angekommen. (Konjunktiv I)|sei
Er behauptet, er ___ den Brief geschrieben. (Konjunktiv I)|habe
Sie berichtet, er ___ eingeschlafen. (Konjunktiv I)|sei
Der Fahrer erklärt, er ___ das Schild bemerkt. (Konjunktiv I)|habe
Er sagt, sie ___ umgezogen. (Konjunktiv I)|sei
Die Kundin sagt, sie ___ den Vertrag gelesen. (Konjunktiv I)|habe
Er erklärt, das Kind ___ aufgewacht. (Konjunktiv I)|sei
""", "Reported past uses the Konjunktiv I auxiliary '{answer}' plus participle; the lexical verb retains its usual haben/sein auxiliary.")
meanings(138,"""
Er sagt, er habe alles bezahlt.|report
Ich habe alles bezahlt. (eigene Aussage)|assert
Hätte ich doch früher angerufen!|wish
Hast du die Rechnung bezahlt? (echte Frage)|question
Sie erklärt, sie sei gestern angekommen.|report
Wir sind gestern angekommen. (eigene Aussage)|assert
Wäre ich doch früher losgefahren!|wish
Bist du gestern angekommen? (echte Frage)|question
Die Zeitung schreibt, er habe den Unfall gesehen.|report
Die Zeugin sagt, sie sei zu Hause geblieben.|report
""",report_labels,'Is this attributed past, a direct statement, a wish or a question?')

for action in ACTIONS[:10]:
    patient,plural,part,inf,present,past,obj,zu=action
    LESSONS.setdefault(139, []).append(question(f'Anna erklärt, sie ___ morgen {obj} {inf}. (Konjunktiv I, Zukunft)','werde',
        ['wird','wurde','würden'],
        'Werde plus infinitive marks reported future with a singular third-person subject; the reporter attributes the plan to Anna.','Complete the reported future.'))
reported_future={
 'reported':('An attributed future plan or prediction','Werde plus infinitive in the reporting frame is Konjunktiv I future.'),
 'ordinary':('A direct future statement','Wird/werden plus infinitive here is ordinary indicative Futur I.'),
 'passive':('An event passive','Wird/werden plus participle describes an action on the subject, not a reported future.'),
 'past':('An attributed past event','Habe/sei plus participle reports an already completed event.'),
}
meanings(139,"""
Sie sagt, sie werde später anrufen.|reported
Ich werde später anrufen. (eigene Aussage)|ordinary
Der Brief wird verschickt.|passive
Er sagt, er habe angerufen.|past
Die Zeitung schreibt, die Firma werde neue Stellen schaffen.|reported
Wir werden morgen kommen. (eigene Aussage)|ordinary
Die Gäste werden begrüßt.|passive
Sie sagt, sie sei gekommen.|past
Er erklärt, er werde den Vertrag prüfen.|reported
Sie berichtet, er werde bald abreisen.|reported
""",reported_future,'Which construction is used?')

gaps(140,'hätte|hätten|wäre|wären|hatte|hat|ist|war',"""
Wenn ich früher losgefahren ___, hätte ich den Zug erreicht. (irreal)|wäre
Wenn wir mehr gelernt ___, hätten wir bestanden. (irreal)|hätten
Wenn sie angerufen ___, hätte ich geholfen. (Singular, irreal)|hätte
Wenn wir pünktlich gekommen ___, hätten wir den Anfang gesehen. (irreal)|wären
Ich ___ den Fehler bemerkt, wenn ich genauer gelesen hätte. (irreal)|hätte
Wir ___ zu Hause geblieben, wenn wir das gewusst hätten. (irreal)|wären
Er ___ die Rechnung bezahlt, wenn er Geld gehabt hätte. (irreal)|hätte
Sie ___ früher angekommen, wenn der Zug pünktlich gewesen wäre. (Singular, irreal)|wäre
Wir ___ geholfen, wenn wir Zeit gehabt hätten. (irreal)|hätten
Ich ___ gegangen, wenn du es gesagt hättest. (irreal)|wäre
""", "The unreal past uses Konjunktiv II of haben/sein plus participle: '{answer}'. The lexical verb determines haben versus sein.")
unreal_past={
 'unreal':('An imagined past alternative','Hätte/wäre plus participle presents a counterfactual or wished-for past alternative, not an asserted event.'),
 'actual':('An asserted completed past event','Indicative haben/sein plus participle states a completed event directly.'),
 'earlier':('An asserted event before a past reference point','Hatte/war plus participle is indicative Plusquamperfekt, not Konjunktiv II.'),
 'present':('A present hypothetical situation','Hätte/wäre without a past participle here refers to an imagined present state.'),
}
meanings(140,"""
Ich hätte dir geholfen, aber ich war nicht da.|unreal
Ich habe dir gestern geholfen.|actual
Als du kamst, hatte ich schon gegessen.|earlier
Wenn ich jetzt Zeit hätte, würde ich helfen.|present
Wäre ich doch zu Hause geblieben!|unreal
Wir sind gestern gefahren.|actual
Als wir ankamen, war sie schon gegangen.|earlier
Ich wäre gern jetzt am Meer.|present
Wir hätten den Zug erreicht, wenn wir früher gefahren wären.|unreal
Er hätte die Rechnung bezahlt, wenn er genug Geld gehabt hätte.|unreal
""",unreal_past,'Which time/status does this verb group express?')

for inf in ['arbeiten','warten','lernen','helfen','kommen','gehen','bleiben','anrufen','bezahlen','umziehen']:
    correct=f'{inf} müssen'
    LESSONS.setdefault(141, []).append(question(f'Ich habe gestern ___. ({inf} + müssen)',correct,
        [f'{inf} gemusst',f'zu {inf} müssen',f'müssen {inf}'],
        'In the Perfekt, a modal governing another verb takes a replacement infinitive: habe + lexical infinitive + müssen, not gemusst.','Complete the past modal group.'))
modal_past={
 'required':('A past necessity','Habe … müssen states that the action was required in the past.'),
 'allowed':('A past permission','Habe … dürfen expresses permission in the past.'),
 'able':('A past ability or possibility','Habe … können expresses past ability or possibility.'),
 'regret':('A past action that should have happened','Hätte … sollen expresses an unreal past recommendation or regret; it does not assert completion.'),
}
meanings(141,"""
Ich habe länger arbeiten müssen.|required
Sie hat früher gehen dürfen.|allowed
Er hat uns helfen können.|able
Ich hätte früher anrufen sollen.|regret
Wir haben warten müssen.|required
Ihr habt mitkommen dürfen.|allowed
Wir haben die Datei öffnen können.|able
Sie hätte mehr lernen sollen.|regret
Weil er hat arbeiten müssen, blieb er im Büro.|required
Weil sie hätte anrufen sollen, ärgert sie sich.|regret
""",modal_past,'What does the past modal group mean?')

future_perfect={
 'deadline':('Completion by a future reference point','Werden + participle + haben/sein with a future deadline marks something expected to be completed by then.'),
 'inference':('An inference about a completed event','With a present evidential context, Futur II can express a guess about something already completed.'),
 'future':('An ordinary future event','Werden plus a bare infinitive is Futur I, with no explicit completed-event perspective.'),
 'perfect':('An asserted completed past event','Indicative haben/sein plus participle directly asserts the completed event rather than guessing with Futur II.'),
}
meanings(142,"""
Bis Freitag wird sie alles erledigt haben.|deadline
Er ist nicht da; er wird wohl schon gegangen sein.|inference
Sie wird morgen kommen.|future
Er hat die Rechnung bezahlt.|perfect
Bis morgen werden wir angekommen sein.|deadline
Das Licht ist aus; sie wird wohl eingeschlafen sein.|inference
Wir werden nächste Woche reisen.|future
Sie ist gestern angekommen.|perfect
Bis acht wird er den Bericht geschrieben haben.|deadline
Er antwortet nicht; er wird wohl den Bus verpasst haben.|inference
Ich werde später anrufen.|future
Wir haben das Zimmer geputzt.|perfect
Bis Juni werden sie umgezogen sein.|deadline
Die Küche riecht gut; er wird wohl schon gekocht haben.|inference
Die Kinder werden morgen spielen.|future
Sie hat die Briefe verschickt.|perfect
Bis Monatsende werde ich den Kurs abgeschlossen haben.|deadline
Er wirkt erholt; er wird wohl gut geschlafen haben.|inference
Wir werden bald aufbrechen.|future
Die Gäste sind gegangen.|perfect
""",future_perfect,'How should the tense construction be understood in this context?')

zu_modal={
 'mustpassive':('Someone must carry out the action on the subject','Sein zu with an obligation cue expresses passive necessity: muss … werden.'),
 'canpassive':('The action on the subject is possible','Sein zu with leicht/kaum and a feasibility context expresses passive possibility: kann … werden.'),
 'mustactive':('The subject is required to act','Haben zu places an obligation on the subject: muss … tun.'),
 'perfect':('An ordinary completed action','Haben plus a past participle without a governed zu-infinitive is active Perfekt.'),
}
meanings(143,"""
Die Regeln sind unbedingt zu beachten.|mustpassive
Die Aufgabe ist leicht zu lösen.|canpassive
Du hast den Antrag bis morgen abzugeben.|mustactive
Ich habe den Antrag abgegeben.|perfect
Die Tür ist laut Vorschrift stets zu schließen.|mustpassive
Die Schrift ist gut zu lesen.|canpassive
Wir haben die Frist einzuhalten.|mustactive
Sie hat die Frist eingehalten.|perfect
Die Gebühr ist zwingend zu bezahlen.|mustpassive
Der Fehler ist einfach zu erkennen.|canpassive
Er hat die Unterlagen zu prüfen.|mustactive
Er hat die Unterlagen geprüft.|perfect
Die Anweisungen sind unbedingt zu befolgen.|mustpassive
Das Fenster ist ohne Mühe zu öffnen.|canpassive
Ihr habt euch pünktlich anzumelden.|mustactive
Ihr habt euch angemeldet.|perfect
Der Ausweis ist auf Verlangen vorzuzeigen.|mustpassive
Das Gerät ist problemlos zu reparieren.|canpassive
Sie hat den Bericht heute abzuliefern.|mustactive
Sie hat den Bericht abgeliefert.|perfect
""",zu_modal,'Interpret sein/haben with the following verb group.')

gaps(144,'treffen|stellen|stehen|kommen|nehmen|bringen|geben|leisten|führen|setzen',"""
Wir müssen eine Entscheidung ___.|treffen|Eine Entscheidung treffen means decide; treffen is the fixed support verb.
Ich möchte eine Frage ___.|stellen|Eine Frage stellen means ask a question; stellen is the fixed support verb.
Mehrere Termine ___ zur Verfügung.|stehen|Zur Verfügung stehen means be available; plural Termine requires stehen.
Diese Lösung kann in Frage ___.|kommen|In Frage kommen means be a possible or suitable option.
Wir müssen Rücksicht auf die Nachbarn ___.|nehmen|Rücksicht nehmen means show consideration; the person considered follows auf.
Er möchte den Motor in Gang ___.|bringen|In Gang bringen means start or set in motion, requiring bringen.
Kannst du mir Bescheid ___?|geben|Bescheid geben means inform or let someone know; the recipient is dative mir.
Wir wollen einen Beitrag ___.|leisten|Einen Beitrag leisten means contribute; leisten is the conventional verb.
Sie möchte ein Gespräch mit dem Chef ___.|führen|Ein Gespräch führen means have or conduct a conversation.
Wir müssen den Plan in die Tat ___.|umsetzen|In die Tat umsetzen means put a plan into practice; the complete verb is umsetzen.
Die Firma kann Unterstützung zur Verfügung ___.|stellen|Zur Verfügung stellen means make available, whereas zur Verfügung stehen means be available.
Das neue Gesetz soll in Kraft ___.|treten|In Kraft treten means come into force; treten is the fixed verb here.
Wir wollen Abschied ___.|nehmen|Abschied nehmen means say goodbye; nehmen belongs to the fixed phrase.
Er will einen Antrag auf Urlaub ___.|stellen|Einen Antrag stellen means submit an application or request.
Ich möchte eine Antwort ___.|geben|Eine Antwort geben means answer; geben is the fixed verb in this noun-based expression.
Wir müssen die Maschine in Betrieb ___.|nehmen|In Betrieb nehmen means put into operation, not merely describe its existing state.
Sie will Hilfe ___.|leisten|Hilfe leisten means provide assistance; leisten is the support verb.
Wir wollen Kontakt mit der Firma auf___. (Infinitiv ergänzen)|nehmen|Kontakt aufnehmen means establish contact; the full infinitive is aufnehmen.
Er kann die Sache zum Abschluss ___.|bringen|Zum Abschluss bringen means finish or bring to a conclusion.
Wir müssen eine Auswahl ___.|treffen|Eine Auswahl treffen means make a selection; treffen is the conventional support verb.
""", "The fixed noun-verb expression requires '{answer}'; learn the phrase as a unit rather than translating each word independently.")
