from .core import gaps, meanings, explicit, LESSONS, question

appositions=[
 ('Frau Berger, die neue Kursleiterin, begrüßt uns.','die neue Kursleiterin','Frau Berger'),
 ('Herr Braun, unser Nachbar, hilft uns.','unser Nachbar','Herr Braun'),
 ('Berlin, die deutsche Hauptstadt, ist groß.','die deutsche Hauptstadt','Berlin'),
 ('Ich spreche mit Herrn Klein, dem neuen Leiter.','dem neuen Leiter','Herrn Klein'),
 ('Wir besuchen Frau Roth, unsere Lehrerin.','unsere Lehrerin','Frau Roth'),
 ('Sie hilft Paul, ihrem Bruder.','ihrem Bruder','Paul'),
 ('Er fragt den Kollegen, einen erfahrenen Techniker.','einen erfahrenen Techniker','den Kollegen'),
 ('Wir wohnen in Bonn, einer Stadt am Rhein.','einer Stadt am Rhein','Bonn'),
 ('Das Fest beginnt am Montag, dem ersten Juni.','dem ersten Juni','Montag'),
 ('Das Gerät, ein alter Drucker, funktioniert noch.','ein alter Drucker','Das Gerät'),
]
for sentence,apposition,head in appositions:
    LESSONS.setdefault(159, []).append(question(sentence+' Welche Gruppe ist die Apposition?',apposition,
        [head,'the finite verb','an implied future action'],
        f"'{apposition}' is a second noun phrase identifying or explaining '{head}'; it is not a separate event.",'Identify the explanatory noun phrase.'))
    LESSONS[159].append(question(sentence+f' Wen oder was erklärt „{apposition}“?',head,
        ['the action of the verb','an unnamed new participant','the sentence’s tense'],
        f"The apposition and '{head}' identify the same person/thing; marked case normally follows the surrounding noun phrase.",'Find the apposition’s reference.'))

impersonal={
 'experience':('A dative experiencer without a nominative person','Mir/dir/ihm marks the person experiencing a feeling; it is not an accusative object or a dummy es.'),
 'passive':('An impersonal activity with no named agent','The impersonal passive describes an activity without naming a nominative participant who performs it.'),
 'instruction':('A subjectless instruction','An infinitive instruction directs the reader to act without naming a grammatical subject.'),
 'weather':('A formal weather subject','Weather es is a required formal subject; it does not identify a concrete person or object.'),
}
meanings(160,"""
Mir ist kalt.|experience
Hier wird nicht geraucht.|passive
Bitte nicht betreten!|instruction
Es regnet.|weather
Dir ist schlecht.|experience
Im Saal wird getanzt.|passive
Vor Gebrauch schütteln!|instruction
Es schneit.|weather
Ihm ist warm.|experience
Heute wird lange gearbeitet.|passive
Bitte leise sprechen!|instruction
Es hagelt.|weather
Ihr ist schwindlig.|experience
Hier wird viel gelacht.|passive
Nicht öffnen!|instruction
Es donnert.|weather
Uns ist kalt.|experience
Im Büro wird telefoniert.|passive
Rechts gehen!|instruction
Es blitzt.|weather
""",impersonal,'Identify the impersonal or subjectless construction.')

gaps(161,'mich|mir|dich|dir|ihn|ihm|sie|ihr|uns|euch',"""
Die Reparatur kostet ___ einen Arbeitstag. (ich)|mich
Der Fehler kostet ___ viel Geld. (du)|dich
Die Reise kostet ___ einen Monatslohn. (er)|ihn
Die Suche kostet ___ eine Stunde. (sie, Singular)|sie
Der Umzug kostet ___ viel Kraft. (wir)|uns
Die Verspätung kostet ___ den Anschluss. (ihr)|euch
Das Ticket kostet ___ zwanzig Euro. (ich)|mich
Die Änderung kostet ___ einen freien Tag. (du)|dich
Der Schaden kostet ___ viel Geld. (er)|ihn
Das Projekt kostet ___ viele Nerven. (sie, Singular)|sie
Die Arbeit kostet ___ Zeit. (wir)|uns
Das Warten kostet ___ Geduld. (ihr)|euch
Er nennt ___ einen Freund. (ich)|mich
Sie nennt ___ einen Experten. (du)|dich
Wir nennen ___ einen Helfer. (er)|ihn
Er nennt ___ eine gute Kollegin. (sie)|sie
Der Lehrer fragt ___ ein deutsches Wort ab. (ich)|mich
Die Lehrerin fragt ___ die neuen Wörter ab. (du)|dich
Der Kurs kostet ___ hundert Euro. (er)|ihn
Die Gebühr kostet ___ zehn Euro. (sie, Singular)|sie
""", "This frame governs an accusative person plus an accusative amount, designation or tested content; use '{answer}', not a dative pronoun.")

es_types={
 'anticipatory':('A placeholder for the following clause','Es anticipates the later dass- or infinitive clause and does not refer back to a concrete noun.'),
 'referential':('A previously named neuter noun','Here es refers back to the named neuter noun; no later content clause fills its role.'),
 'weather':('A formal weather subject','The weather predicate uses formal es, without a noun reference or following content clause.'),
 'presentative':('A first-position placeholder in an impersonal sentence','This initial es fills the first position; it disappears when another constituent moves there.'),
}
meanings(162,"""
Ich finde es wichtig, dass alle Bescheid wissen. (es)|anticipatory
Das Buch liegt hier. Es ist neu. (Es)|referential
Es regnet seit Stunden. (Es)|weather
Es wird heute getanzt. (Es)|presentative
Es freut mich, dass du kommst. (Es)|anticipatory
Das Kind ist müde. Es schläft. (Es)|referential
Es schneit stark. (Es)|weather
Es wird im Saal gelacht. (Es)|presentative
Sie findet es schön, zusammen zu lernen. (es)|anticipatory
Das Gerät ist kaputt. Ich repariere es. (es)|referential
Es donnert. (Es)|weather
Es wird hier gearbeitet. (Es)|presentative
Ich halte es für möglich, dass er kommt. (es)|anticipatory
Das Fenster ist offen. Ich schließe es. (es)|referential
Es hagelt. (Es)|weather
Es wird viel telefoniert. (Es)|presentative
Es ist wichtig, den Vertrag zu lesen. (Es)|anticipatory
Ich mag es, wenn alle mithelfen. (es)|anticipatory
Es ist schade, dass sie absagt. (Es)|anticipatory
Er bedauert es, den Termin verpasst zu haben. (es)|anticipatory
""",es_types,'What role does es play here?')

when_types={
 'content':('The recurring situation being evaluated','The wenn-clause supplies the situation that pleases, annoys or matters to someone, rather than merely a condition for a separate practical consequence.'),
 'condition':('A condition for a separate consequence','The main action depends on the stated condition; it is not a judgement about that situation.'),
 'question':('A question about the time of an event','Wann asks for a time; it is not the content-oriented conjunction wenn.'),
 'past':('A single past occasion','Als identifies a single past event or life period rather than a recurring evaluated situation.'),
}
meanings(163,"""
Es freut mich, wenn die Teilnehmer einander helfen.|content
Wenn es regnet, nehmen wir den Bus.|condition
Ich frage, wann du kommst.|question
Als ich ankam, war sie schon da.|past
Ich finde es schön, wenn wir gemeinsam lernen.|content
Wenn du Zeit hast, ruf mich an.|condition
Er weiß nicht, wann der Kurs beginnt.|question
Als wir Kinder waren, wohnten wir hier.|past
Mich ärgert es, wenn Leute zu spät kommen.|content
Wenn der Laden offen ist, kaufen wir Brot.|condition
Sag mir, wann die Prüfung stattfindet.|question
Als sie gestern anrief, war ich im Büro.|past
Es ist gut, wenn alle regelmäßig üben.|content
Wenn du fertig bist, können wir gehen.|condition
Ich mag es, wenn die Sonne scheint.|content
Sie findet es schade, wenn der Kurs ausfällt.|content
Es stört ihn, wenn man laut spricht.|content
Wir freuen uns, wenn alle teilnehmen.|content
Es gefällt mir, wenn die Wohnung hell ist.|content
Ich finde es hilfreich, wenn du Beispiele gibst.|content
""",when_types,'How is the wenn/W/als clause used in this context?')

spoken_types={
 'left':('A fronted topic resumed by a pronoun','A noun phrase is placed before the clause and taken up again by den/die/der; this is spoken left dislocation.'),
 'after':('A noun phrase added as an afterthought','The clause is already structurally complete before the final noun phrase identifies a participant.'),
 'neutral':('An ordinary integrated sentence','The noun phrase is part of the clause without an extra resumptive pronoun or afterthought.'),
 'relative':('A noun modified by a relative clause','The following clause describes the noun; it is not a resumptive main clause about a detached topic.'),
}
meanings(164,"""
Den neuen Kurs, den finde ich hilfreich.|left
Er ist angekommen, unser Nachbar.|after
Ich finde den neuen Kurs hilfreich.|neutral
Das ist der Kurs, den ich besuche.|relative
Die Rechnung, die habe ich bezahlt.|left
Sie kommt morgen, meine Schwester.|after
Ich habe die Rechnung bezahlt.|neutral
Hier ist die Rechnung, die du suchst.|relative
Mein Bruder, der hilft uns.|left
Es ist kaputt, das alte Gerät.|after
Mein Bruder hilft uns.|neutral
Das ist mein Bruder, der hier arbeitet.|relative
Das Buch, das lese ich gerade.|left
Sie sind schon da, die Gäste.|after
Ich lese gerade das Buch.|neutral
Das ist das Buch, das ich lese.|relative
Die Wohnung, die gefällt mir.|left
Er ruft später an, der Arzt.|after
Die Wohnung gefällt mir.|neutral
Hier wohnt die Frau, die uns hilft.|relative
""",spoken_types,'Identify the spoken structure or its integrated alternative.')

clefts=[
 ('Es ist die fehlende Unterschrift, die das Problem verursacht.','die fehlende Unterschrift'),
 ('Es ist Anna, die den Kurs organisiert.','Anna'),
 ('Es ist der Preis, der mich stört.','der Preis'),
 ('Es sind die Nachbarn, die uns helfen.','die Nachbarn'),
 ('Es ist Paul, den ich angerufen habe.','Paul'),
 ('Es ist die Leiterin, der ich vertraue.','die Leiterin'),
 ('Es ist das Wetter, das unsere Reise verhindert.','das Wetter'),
 ('Es ist der Termin, den wir ändern müssen.','der Termin'),
 ('Es sind die Kinder, die im Garten spielen.','die Kinder'),
 ('Es ist das Geld, das uns fehlt.','das Geld'),
]
for sentence,focus in clefts:
    LESSONS.setdefault(165, []).append(question(sentence+' Was wird hervorgehoben?',focus,
        ['the introductory es as a concrete object','a different unmentioned person','the tense alone'],
        f"The es ist/sind … relative-clause construction highlights '{focus}' as the relevant person or element.",'Identify the focus of the cleft.'))
    LESSONS[165].append(question(sentence+' Welche Funktion hat der Satzbau?','It highlights a particular element of the proposition.',
        ['It asks a yes/no question about es.','It reports a weather event.','It denies that the relative-clause event occurs.'],
        'The cleft splits one proposition into an identifying frame and a relative clause to emphasize the focused constituent.','Interpret the purpose of the cleft construction.'))

interleaved=[
 ('Wen glaubst du, dass Anna eingeladen hat?','eingeladen','Which person do you think Anna invited?'),
 ('Wen denkst du, dass Paul gesehen hat?','gesehen','Which person do you think Paul saw?'),
 ('Was glaubst du, dass Anna gekauft hat?','gekauft','What do you think Anna bought?'),
 ('Wen glaubst du, dass die Lehrerin gefragt hat?','gefragt','Which person do you think the teacher asked?'),
 ('Was denkst du, dass er vergessen hat?','vergessen','What do you think he forgot?'),
 ('Wen glaubst du, dass sie morgen besucht?','besucht','Which person do you think she will visit tomorrow?'),
 ('Was glaubst du, dass der Zeuge bemerkt hat?','bemerkt','What do you think the witness noticed?'),
 ('Wen denkst du, dass wir anrufen sollten?','anrufen','Which person do you think we should call?'),
 ('Was glaubst du, dass die Firma anbietet?','anbietet','What do you think the company offers?'),
 ('Wen glaubst du, dass der Fahrer erkannt hat?','erkannt','Which person do you think the driver recognized?'),
]
for sentence,verb,meaning in interleaved:
    LESSONS.setdefault(166, []).append(question(sentence+f' Zu welchem Verb gehört das Objekt „{sentence.split()[0]}“ inhaltlich?',verb,
        ['glaubst/denkst in the reporting frame','a missing imperative','the infinitive sein'],
        f"The initial object is interpreted with '{verb}' inside the embedded clause, even though it appears before the reporting frame. Recognition is the target here.",'Trace the embedded dependency; do not treat this as a production model.'))
    LESSONS[166].append(question(sentence,meaning,
        ['The speaker states the answer as an established fact.','The initial object is necessarily the person doing the thinking.','The sentence orders the listener to perform the embedded action.'],
        'The question asks about an object in the embedded event while the main frame adds what the listener believes about it.','Choose the interpretation of the interleaved question.'))

pragmatics={
 'criticism':('Criticism or disapproval, rather than a literal information request','The explicit situation makes the question a complaint about conduct, not a request for factual information.'),
 'surprise':('Surprise or emphatic astonishment','The context presents the question as an expression of astonishment, without expecting a factual answer.'),
 'information':('A genuine request for information','The stated situation requires an actual answer about time, place or other information.'),
 'counter':('A counterquestion challenging the premise','The reply asks a question back to question the assumption or demand instead of answering it directly.'),
}
meanings(167,"""
Lärm nachts: Muss das wirklich sein? (verärgert)|criticism
Unerwarteter Erfolg: Wer hätte das gedacht!|surprise
Am Bahnhof: Wann fährt der nächste Zug? (Auskunft gesucht)|information
„Du musst alles allein machen.“ — „Warum denn ich?“ (Einwand)|counter
Schon wieder zu spät: Kannst du nicht einmal pünktlich sein? (Vorwurf)|criticism
Nach einem Wunder: Ist das zu glauben!|surprise
Vor der Anmeldung: Was kostet der Kurs? (Preis gesucht)|information
„Du bist schuld.“ — „Woher willst du das wissen?“ (Einwand)|counter
Ein kaputtes Fenster: Musstest du den Ball hier spielen? (Vorwurf)|criticism
Nach einem unerwarteten Besuch: Wen haben wir denn da!|surprise
In einer fremden Stadt: Wo ist die Apotheke? (Weg gesucht)|information
„Kauf das sofort!“ — „Warum sollte ich?“ (Widerspruch)|counter
Schmutzige Schuhe auf dem Sofa: Muss das sein? (Tadel)|criticism
Nach einem überraschenden Sieg: Hätte das jemand erwartet!|surprise
Beim Arzt: Wann soll ich wiederkommen? (Termin gesucht)|information
„Das ist unmöglich.“ — „Wer sagt das?“ (Anzweifeln)|counter
Er unterbricht ständig: Kannst du mich nicht ausreden lassen? (Vorwurf)|criticism
Die Rechnung ist unerwartet hoch: Wer hätte mit so viel gerechnet!|surprise
Im Geschäft: Haben Sie das in Blau? (echte Frage)|information
„Du kommst bestimmt nicht.“ — „Warum denn nicht?“ (Gegenfrage)|counter
""",pragmatics,'What does the question do in the explicitly given context?')

regional={
 'south':('A recognized regional standard auxiliary variant','Sein with literal sitting, standing or lying occurs in southern standard varieties; it is not automatically an error.'),
 'general':('The widely used haben variant','Haben with literal sitting, standing or lying is widely used; regional sein variants do not make it wrong.'),
 'gender':('A recognized regional gender variation','Both der Joghurt and das Joghurt are standard; neuter is especially associated with Austria and Switzerland.'),
 'caseerror':('An inflection/case error, not the cited regional contrast','The determiner or auxiliary form disagrees with the stated case/person; the regional auxiliary/gender variation does not license this form.'),
}
meanings(168,"""
Ich bin auf der Bank gesessen. (südliche Standardvarietät)|south
Ich habe auf der Bank gesessen.|general
Das Joghurt steht im Kühlschrank. (österreichisch/schweizerisch)|gender
Ich fahre mit den Zug. (Singular)|caseerror
Er ist lange im Flur gestanden. (südliche Standardvarietät)|south
Er hat lange im Flur gestanden.|general
Der Joghurt steht im Kühlschrank.|gender
Du bin auf der Bank gesessen.|caseerror
Wir sind im Garten gelegen. (südliche Standardvarietät)|south
Wir haben im Garten gelegen.|general
Das frische Joghurt schmeckt gut. (österreichisch/schweizerisch)|gender
Ich sehe der Mann. (Akkusativobjekt)|caseerror
Sie ist am Fenster gesessen. (Singular; südliche Standardvarietät)|south
Sie hat am Fenster gesessen. (Singular)|general
Der frische Joghurt schmeckt gut.|gender
Wir ist im Garten gelegen.|caseerror
Die Gäste sind vor der Tür gestanden. (südliche Standardvarietät)|south
Die Gäste haben vor der Tür gestanden.|general
Das Joghurt ist kalt. (österreichisch/schweizerisch)|gender
Er hat auf dem Sofa gelegen.|general
""",regional,'Recognize regional standard variation without treating every different form as correct.')

gaps(169,'als|wie|dass|ob',"""
Der Kurs war leichter, ___ ich erwartet hatte. (Komparativ)|als
Die Fahrt dauerte so lange, ___ ich gedacht hatte. (Gleichheit)|wie
Sie kam früher, ___ wir vermutet hatten.|als
Er arbeitet genauso, ___ wir es vereinbart haben.|wie
Die Wohnung ist größer, ___ sie auf den Fotos wirkte.|als
Es war so schön, ___ ich es mir vorgestellt hatte.|wie
Der Preis ist höher, ___ ich gelesen hatte.|als
Sie spricht ebenso deutlich, ___ ihre Lehrerin es tut.|wie
Es ging schneller, ___ wir gehofft hatten.|als
Die Aufgabe ist so schwierig, ___ er gesagt hat.|wie
Die Prüfung war schwerer, ___ ich befürchtet hatte.|als
Er kocht genauso gut, ___ seine Mutter es tut.|wie
Der Zug kam später, ___ der Fahrplan angab.|als
Das Zimmer ist so ruhig, ___ wir es wollten.|wie
Sie hat mehr gelernt, ___ ich dachte.|als
Alles lief so, ___ wir es geplant hatten.|wie
Er ist älter, ___ ich angenommen hatte.|als
Das Buch ist genauso spannend, ___ du gesagt hast.|wie
Die Reise kostet weniger, ___ wir erwartet hatten.|als
Der Film war so gut, ___ ich gehofft hatte.|wie
""",{'als':'A comparative such as leichter, früher or mehr takes als; the finite comparative clause ends with its own verb group.', 'wie':'So/genauso/ebenso introduces equality and takes wie, including a full finite comparative clause.', 'dass':'Dass would introduce content or consequence, not the specified comparison.', 'ob':'Ob would embed a yes/no question rather than a comparison.'})

exclamations={
 'surprise':('An exclamation expressing surprise','The exclamation mark and explicit context make the verb-first/wie form an expression of surprise, not a literal question.'),
 'praise':('An exclamation expressing admiration','In the positive context, the form emphasizes appreciation of an impressive quality or action.'),
 'disapproval':('An exclamation expressing disapproval','The negative context makes the heightened form a complaint or reproach.'),
 'question':('A genuine information question','The context asks for an actual answer; the interrogative form is not being used as an exclamation.'),
}
meanings(170,"""
Unerwartetes Geschenk: Ist das eine Überraschung!|surprise
Nach einem Konzert: Wie schön sie singt!|praise
Ärger über Schmutz: Wie unordentlich es hier ist!|disapproval
Echte Frage: Wie spät ist es?|question
Unerwartet leerer Raum: Ist das hier still! (erstaunt)|surprise
Bewunderung: Hat sie das toll gemacht!|praise
Beschwerde: Ist das hier laut!|disapproval
Echte Frage: Ist die Tür offen?|question
Erstaunen: Wie schnell die Zeit vergangen ist!|surprise
Lob: Wie sorgfältig du gearbeitet hast!|praise
Tadel: Wie unhöflich er sich benimmt!|disapproval
Echte Frage: Wie funktioniert das Gerät?|question
Erstaunen über viele Gäste: Sind das viele Menschen!|surprise
Freude über die Aussicht: Ist das schön hier!|praise
Ärger über eine Rechnung: Ist das teuer!|disapproval
Echte Frage: Sind die Gäste schon da?|question
Erstaunen nach langer Pause: Bist du groß geworden!|surprise
Anerkennung: Wie gut du Deutsch sprichst!|praise
Vorwurf: Hat der wieder einen Unsinn erzählt!|disapproval
Echte Frage: Wie alt ist dein Bruder?|question
""",exclamations,'Interpret the clause’s effect in the stated context.')
