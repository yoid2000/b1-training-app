from .core import gaps, meanings, explicit, LESSONS, question

weak = [('Kunde','Kunden'),('Kollege','Kollegen'),('Mensch','Menschen'),('Zeuge','Zeugen'),('Junge','Jungen'),('Student','Studenten'),('Polizist','Polizisten'),('Patient','Patienten'),('Nachbar','Nachbarn'),('Name','Namen')]
for nom, oblique in weak:
    for prompt in [f'Ich sehe den ___. ({nom}; Akkusativ)', f'Ich spreche mit dem ___. ({nom}; Dativ)']:
        pool = [nom, oblique+'s', nom+'er']
        LESSONS.setdefault(51, []).append(question(prompt, oblique, pool,
            f"{nom} takes -(e)n outside nominative singular: '{oblique}'. Name has Namen in accusative/dative but Namens in genitive.", 'Complete the singular noun.'))

gaps(52, 'Bekannter|Bekannte|Bekannten|Bekanntem|Neues|Neue|Neuen|Wichtiges|Wichtige|Wichtigen', """
Ein ___ hat angerufen. (bekannt; Mann)|Bekannter
Ich sehe einen ___. (bekannt; Mann)|Bekannten
Mit einem ___ gehe ich spazieren. (bekannt; Mann)|Bekannten
Eine ___ hilft mir. (bekannt; Frau)|Bekannte
Ich treffe die ___. (bekannt; Frau)|Bekannte
Mit der ___ spreche ich morgen. (bekannt; Frau)|Bekannten
Die ___ sind schon da. (bekannt; Plural)|Bekannten
Ich habe etwas ___ gelernt. (neu)|Neues
Er hat nichts ___ erzählt. (neu)|Neues
Sie berichtet von etwas ___. (neu; Dativ)|Neuem|After etwas in dative, the nominalized adjective has strong -em and is capitalized.
Das ___ interessiert mich. (neu)|Neue
Mit dem ___ bin ich zufrieden. (neu)|Neuen
Ich möchte etwas ___ sagen. (wichtig)|Wichtiges
Sie hat nichts ___ vergessen. (wichtig)|Wichtiges
Das ___ steht am Ende. (wichtig)|Wichtige
Mit dem ___ beginnen wir. (wichtig)|Wichtigen
Der ___ wartet draußen. (bekannt; Mann)|Bekannte
Die ___ arbeitet hier. (bekannt; Frau)|Bekannte
Ich helfe den ___. (bekannt; Plural)|Bekannten
Mein ___ kommt später. (bekannt; Mann)|Bekannter
""", "The adjective replaces a noun and is capitalized; '{answer}' has the ending required by its determiner, gender and case.")

gaps(53, 'der|die|das|den|dem|denen|dieser|diese|dieses|diesen|diesem', """
Siehst du den Mann? ___ kenne ich. (der-Pronomen)|Den|The pronoun is accusative masculine because it is the object of kenne; it is capitalized initially.
Hier ist das Gerät. Mit ___ arbeite ich. (der-Pronomen)|dem
Die Kollegin ist nett. ___ hilft uns. (der-Pronomen)|Die|The pronoun is a feminine nominative subject; capitalize at the start.
Die Leute sind schon da. Mit ___ spreche ich. (der-Pronomen)|denen
Der Zug kommt. ___ fährt nach Köln. (der-Pronomen)|Der|The pronoun refers to a masculine nominative subject.
Das Buch ist spannend. ___ lese ich gerade. (der-Pronomen)|Das|The pronoun is neuter accusative, referring to das Buch.
Die Tasche ist schön. ___ kaufe ich. (der-Pronomen)|Die|Feminine accusative uses die as a standalone demonstrative.
Der Kollege wartet. Ich helfe ___. (der-Pronomen)|dem
Die Frau ist hier. Ich danke ___. (der-Pronomen)|der
Die Kinder spielen. Ich rufe ___. (der-Pronomen)|die
Von den Mänteln nehme ich ___. (dies-; Singular)|diesen
Welches Rad? Ich nehme ___. (dies-)|dieses
Welche Tasche? Ich nehme ___. (dies-)|diese
Welcher Bus fährt? ___ fährt zuerst. (dies-)|Dieser|Masculine nominative dies- takes -er, with initial capitalization.
Mit welchem Wagen? Mit ___. (dies-)|diesem
Mit welcher Frau? Mit ___. (dies-)|dieser
Welche Kinder? Ich sehe ___. (dies-; Plural)|diese
Welchen Gästen hilfst du? ___. (dies-; Dativ Plural)|Diesen|The dative plural standalone pronoun is diesen, capitalized as a sentence fragment.
Das ist mein Plan. ___ gefällt mir. (der-Pronomen)|Der|Plan is masculine; the subject of gefällt is nominative der.
Diese Geräte sind neu. Ich arbeite mit ___. (der-Pronomen)|denen
""", "A standalone demonstrative takes the case of its role in its own clause; '{answer}' also matches the antecedent's gender and number.")

gaps(54, 'meiner|meine|meines|meinen|meinem|deiner|deine|deines|deinen|deinem', """
Ist das dein Mantel? Ja, das ist ___. (mein; Nominativ)|meiner
Ist das deine Tasche? Ja, das ist ___. (mein)|meine
Ist das dein Buch? Ja, das ist ___. (mein; volle Form)|meines
Sind das deine Schuhe? Ja, das sind ___. (mein)|meine
Welchen Stift nehme ich? Nimm ___. (mein)|meinen
Mit welchem Rad fährst du? Mit ___. (mein)|meinem
Mit welcher Tasche reist du? Mit ___. (mein)|meiner
Mit welchen Schuhen gehst du? Mit ___. (mein)|meinen
Dieser Mantel ist nicht meiner, sondern ___. (dein; Nominativ)|deiner
Diese Tasche ist nicht meine, sondern ___. (dein)|deine
Dieses Buch ist nicht meines, sondern ___. (dein; volle Form)|deines
Diese Schlüssel sind nicht meine, sondern ___. (dein)|deine
Welchen Wagen nimmt er? Er nimmt ___. (dein)|deinen
Mit welchem Werkzeug arbeitet sie? Mit ___. (dein)|deinem
Mit welcher Kamera fotografierst du? Mit ___. (dein)|deiner
Mit welchen Freunden kommst du? Mit ___. (dein)|deinen
Dein Schlüssel ist hier; ___ liegt zu Hause. (mein; Nominativ)|meiner
Deine Wohnung ist hell; ___ ist dunkel. (mein)|meine
Dein Zimmer ist groß; ___ ist klein. (mein; volle Form)|meines
Du nimmst deinen Laptop, ich nehme ___. (mein; Akkusativ)|meinen
""", "When the noun is omitted, the possessive pronoun carries a full gender/case ending: '{answer}'.")

gaps(55, 'derselbe|dieselbe|dasselbe|denselben|demselben|derselben|solche|solchen|jener|jenes', """
Das ist genau ___ Mann wie gestern. (identische Person)|derselbe
Wir besuchen ___ Schule wie früher. (identische Schule)|dieselbe
Das ist ___ Auto wie gestern. (identisches Fahrzeug)|dasselbe
Ich lese noch ___ Roman. (identisches Buch)|denselben
Wir fahren mit ___ Zug wie unsere Freunde. (identischer Zug)|demselben
Sie wohnt in ___ Wohnung wie früher. (identische Wohnung)|derselben
Ich habe ___ Probleme noch nie gesehen. (diese Art von Problemen)|solche
Mit ___ Aufgaben habe ich Erfahrung. (dieser Art)|solchen
___ Mann dort drüben wartet schon. (jen-; Nominativ)|Jener|Jener points to a more distant masculine noun and is capitalized initially.
___ Haus dort drüben ist alt. (jen-; Nominativ)|Jenes|Jenes is the neuter nominative form of the distal demonstrative.
Wir haben ___ Lehrerin. (identische Person)|dieselbe
Er benutzt immer ___ Werkzeug. (identisches Werkzeug)|dasselbe
Ich spreche mit ___ Arzt wie du. (identische Person)|demselben
Sie trägt ___ Mantel wie gestern. (identischer Mantel)|denselben
Wir fahren zu ___ Freundin wie letzte Woche. (identische Person)|derselben
___ Angebote sind selten. (Angebote dieser Art)|Solche|Solche introduces things of a particular type; it is capitalized initially.
Mit ___ Geräten arbeiten wir nicht. (Geräte dieser Art)|solchen
___ Bus kommt jeden Morgen. (identischer Bus)|Derselbe|Derselbe identifies the same individual masculine noun as subject.
Ich gehe in ___ Geschäft wie du. (identisches Geschäft)|dasselbe
Sie beantwortet ___ Frage noch einmal. (identische Frage)|dieselbe
""", "The context requires identity, type or distal reference; '{answer}' also carries the noun's required gender and case ending.")

gaps(56, 'jeder|jede|jedes|jeden|jedem|einige|einigen|mehrere|mehreren|viele|vielen|wenige|wenigen', """
___ Teilnehmer erhält ein Blatt. (jeder; Singular)|Jeder|Jeder takes masculine nominative and a singular verb.
Ich spreche mit ___ Teilnehmer. (jeder; Singular)|jedem
Wir begrüßen ___ Gast. (jeder; Singular)|jeden
___ Frau erhält eine Einladung. (jeder)|Jede|Feminine nominative uses jede and a singular verb.
___ Kind bekommt ein Buch. (jeder)|Jedes|Neuter nominative uses jedes and a singular verb.
___ Teilnehmer fehlen. (einige; Nominativ)|Einige|Einige is plural and agrees with fehlen.
Ich helfe ___ Teilnehmern. (einige)|einigen
Wir bekommen ___ Hinweise. (mehrere; Akkusativ)|mehrere
Mit ___ Kollegen sprechen wir. (mehrere)|mehreren
Es gibt ___ freie Plätze. (viele)|viele
Mit ___ Gästen wird es eng. (viele)|vielen
Nur ___ Antworten sind falsch. (wenige)|wenige
Mit ___ Worten erklärt er alles. (wenige)|wenigen
___ Aufgabe ist wichtig. (jeder)|Jede|Jede is feminine singular, so the verb is singular ist.
Wir prüfen ___ Antrag. (jeder)|jeden
Das hilft ___ Kind. (jeder)|jedem
Sie liest ___ Bücher. (einige)|einige
Er hat mit ___ Bewerbern gesprochen. (mehrere)|mehreren
___ Schüler lernen hier. (viele)|Viele|Viele introduces a plural subject and takes the plural verb lernen.
___ Geld reicht nicht. (wenig; nicht zählbar)|Wenig|Before uncountable neuter Geld in this phrase, use uninflected wenig, capitalized initially.
""", "The quantifier '{answer}' matches the stated number and the case required by the sentence; jeder selects singular, while einige/mehrere select plural.")

gaps(57, 'irgendjemand|irgendjemanden|irgendjemandem|irgendetwas|irgendwo|irgendwann|irgendwie|irgendein|irgendeine|irgendeinen', """
___ hat angerufen; ich kenne die Person nicht.|Irgendjemand|Irgendjemand denotes an unspecified person as subject, capitalized initially.
Ich habe den Schlüssel ___ liegen lassen. (Ort)|irgendwo
Wir treffen uns ___ nächste Woche. (Zeit)|irgendwann
Es muss ___ funktionieren. (Art und Weise)|irgendwie
Ich möchte ___ essen. (Sache)|irgendetwas
Hast du ___ Stift? (Akkusativ)|irgendeinen
___ Frau wartet draußen. (nicht näher bekannt)|Irgendeine|Irgendeine is an unspecified feminine nominative determiner.
Ich brauche ___ Buch, egal welches.|irgendein
Wir müssen ___ fragen. (Person; mit Kasusendung)|irgendjemanden
Er hat ___ geholfen. (Person; mit Kasusendung)|irgendjemandem
Sie wohnt ___ in Bayern. (Ort)|irgendwo
Wir kommen ___ wieder. (Zeit)|irgendwann
Er hat ___ vergessen. (Sache)|irgendetwas
Ich muss das ___ lösen. (Methode)|irgendwie
Kennst du ___ Arzt? (Akkusativ)|irgendeinen
___ hat mein Fahrrad genommen. (Person)|Irgendjemand|Irgendjemand is an unspecified nominative person pronoun.
Sie sucht ___ Stelle. (Akkusativ)|irgendeine
Wir finden ___ Hotel. (Akkusativ)|irgendein
Ich habe mit ___ gesprochen. (Person; mit Kasusendung)|irgendjemandem
Er wartet auf ___. (Person; mit Kasusendung)|irgendjemanden
""", "'{answer}' matches the requested person, thing, place, time or manner reference; inflected person/determiner forms also follow the clause's case.")

negative_labels = {
 'person':('No person', 'Niemand/keiner excludes people in this context.'),
 'thing':('No thing at all', 'Nichts or gar nichts excludes any thing or content.'),
 'yet':('Not yet, with later possibility', 'Noch nicht negates completion up to now and leaves later completion possible.'),
 'longer':('No longer, unlike before', 'Nicht mehr says that a previous state or activity has stopped.'),
}
meanings(58, """
Niemand hat angerufen.|person
Er arbeitet nicht mehr hier.|longer
Ich habe noch nicht bezahlt.|yet
Die Schachtel enthält gar nichts.|thing
Keiner der Gäste bleibt.|person
Sie raucht nicht mehr.|longer
Der Zug ist noch nicht angekommen.|yet
Ich habe überhaupt nichts verstanden.|thing
Niemandem habe ich davon erzählt.|person
Wir wohnen nicht mehr in Bonn.|longer
Die Rechnung ist noch nicht da.|yet
Er hat nichts mitgebracht.|thing
Ich kenne hier keinen. (keine Person)|person
Die Tür ist nicht mehr offen.|longer
Die Kinder schlafen noch nicht.|yet
Das bedeutet gar nichts.|thing
Niemanden habe ich gesehen.|person
Sie hat keinen Hunger mehr.|longer
Wir haben noch keinen Termin.|yet
Ich brauche nichts.|thing
""",negative_labels,'Which negative meaning does the sentence express?')

attribute_examples = [
 ('Die Wohnung über der Apotheke ist frei.','Die Wohnung über der Apotheke','Die Wohnung ist frei','über der Apotheke'),
 ('Der Mann mit der roten Tasche wartet.','Der Mann mit der roten Tasche','Der Mann wartet','mit der roten Tasche'),
 ('Das Haus am See gehört ihr.','Das Haus am See','Das Haus gehört ihr','am See'),
 ('Die Frau dort drüben ist meine Lehrerin.','Die Frau dort drüben','Die Frau ist meine Lehrerin','dort drüben'),
 ('Der Kurs für Anfänger beginnt morgen.','Der Kurs für Anfänger','Der Kurs beginnt morgen','für Anfänger'),
 ('Das Zimmer neben der Küche ist klein.','Das Zimmer neben der Küche','Das Zimmer ist klein','neben der Küche'),
 ('Der Weg zum Bahnhof ist gesperrt.','Der Weg zum Bahnhof','Der Weg ist gesperrt','zum Bahnhof'),
 ('Die Nachricht von meiner Schwester freut mich.','Die Nachricht von meiner Schwester','Die Nachricht freut mich','von meiner Schwester'),
 ('Die Reise nach Wien ist gebucht.','Die Reise nach Wien','Die Reise ist gebucht','nach Wien'),
 ('Der Termin morgen passt mir.','Der Termin morgen','Der Termin passt mir','morgen'),
]
for sentence, full, basic, attr in attribute_examples:
    LESSONS.setdefault(59, []).append(question(sentence+' Welche vollständige Nomengruppe ist das Subjekt?',full,[attr,basic,sentence],f"'{attr}' identifies the noun more closely and belongs inside the subject noun phrase.",'Choose the full subject noun phrase.'))
    LESSONS[59].append(question(sentence+f" Worauf bezieht sich das Attribut „{attr}“?",full.split()[1],["the finite verb only","the entire event as an adverbial","an unnamed object"],f"The postnominal attribute '{attr}' describes '{full.split()[1]}', rather than the whole event.",'Which noun does the attribute describe?'))

gaps(60, 'ist|sind|hat|haben|dem|den|der|die|neuen|neue|neuer', """
Die Tasche der beiden Gäste ___ verschwunden. (sein)|ist
Die Kollegen meiner Schwester ___ freundlich. (sein)|sind
Das Ergebnis der Prüfungen ___ wichtig. (sein)|ist
Die Liste der Teilnehmer ___ auf dem Tisch. (sein)|ist
Die Bücher des Lehrers ___ teuer. (sein)|sind
Der Leiter der beiden Kurse ___ Zeit. (haben)|hat
Die Mitglieder des Vereins ___ abgestimmt. (haben)|haben
Das Auto meiner Eltern ___ kaputt. (sein)|ist
Die Schlüssel des Büros ___ weg. (sein)|sind
Die Tür der beiden Räume ___ offen. (sein)|ist
Mit ___ beiden neuen Kollegen meiner Schwester arbeite ich. (Dativ Plural)|den
Bei ___ neuen Leiterin des Teams bin ich. (Dativ)|der
Mit ___ alten Gerät meines Bruders arbeite ich. (Dativ)|dem
Die ___ Kollegen meiner Schwester kommen. (neu; Plural)|neuen
Ein ___ Kollege meiner Schwester kommt. (neu)|neuer
Die ___ Kollegin meines Bruders kommt. (neu)|neue
Der Sohn meiner Nachbarn ___ hier. (sein)|ist
Die Wohnungen des Besitzers ___ hell. (sein)|sind
Das Ende der langen Gespräche ___ erreicht. (sein)|ist
Die Freunde des neuen Kollegen ___ eingeladen. (sein)|sind
""", "Agreement follows the head noun, not the nearer genitive attribute; '{answer}' matches the head's number or the phrase's required case/ending.")

focus_labels = {
 'only':('Exclusion of other alternatives', 'Nur limits the statement to its focused element; alternatives are excluded.'),
 'even':('An unexpected included example', 'Sogar highlights an example that is surprising or beyond expectation.'),
 'late':('A time or amount restricted relative to expectation', 'Erst marks a late starting point or a still-small amount, elapsed time or degree of progress relative to expectation.'),
 'degree':('A degree or intensity', 'Ziemlich, völlig and besonders modify intensity rather than selecting an alternative.'),
}
meanings(61, """
Nur Anna hat bezahlt. (nur)|only
Sogar der Chef hilft mit. (sogar)|even
Er kommt erst um zehn. (erst)|late
Die Aufgabe ist ziemlich schwer. (ziemlich)|degree
Wir brauchen nur eine Kopie. (nur)|only
Sogar am Sonntag arbeitet sie. (sogar)|even
Sie hat erst zwei Seiten gelesen. (erst)|late
Der Raum ist völlig leer. (völlig)|degree
Nur heute ist der Eintritt frei. (nur)|only
Sogar ein Anfänger versteht das. (sogar)|even
Der Laden öffnet erst morgen. (erst)|late
Der Film war besonders spannend. (besonders)|degree
Ich trinke nur Wasser. (nur)|only
Sogar meine Großmutter benutzt die App. (sogar)|even
Wir sind erst am Anfang. (erst)|late
Das ist ganz unmöglich. (ganz)|degree
Nur im Erdgeschoss ist Platz. (nur)|only
Er hat sogar den Keller geputzt. (sogar)|even
Es ist erst sechs Uhr. (erst)|late
Die Antwort ist völlig richtig. (völlig)|degree
""",focus_labels,'What does the word in parentheses contribute here?')

quantity_labels = {
 'min':('A lower bound: at least', 'Mindestens sets the minimum; a larger amount is allowed.'),
 'max':('An upper bound: at most', 'Höchstens sets the maximum; a smaller amount is allowed.'),
 'almost':('Nearly the whole, with exceptions', 'Fast alle means most but not quite all members.'),
 'part':('A subset of a whole', 'Ein Teil or die Hälfte names part of the larger group; Hälfte means half.'),
}
meanings(62, """
Mindestens zehn Personen kommen.|min
Höchstens zehn Personen dürfen hinein.|max
Fast alle Teilnehmer sind da.|almost
Ein Teil der Gruppe bleibt.|part
Sie braucht mindestens drei Tage.|min
Die Fahrt kostet höchstens zwanzig Euro.|max
Fast alle Fenster sind offen.|almost
Die Hälfte des Geldes fehlt.|part
Das Paket wiegt mindestens ein Kilo.|min
Höchstens zwei Antworten sind falsch.|max
Fast alle Bewerber haben geantwortet.|almost
Ein Teil des Gartens gehört uns.|part
Wir warten mindestens eine Stunde.|min
Sie bleibt höchstens eine Woche.|max
Fast alle Kinder schlafen.|almost
Die Hälfte der Plätze ist besetzt.|part
Du musst mindestens achtzehn sein.|min
Es dürfen höchstens fünf Gäste kommen.|max
Fast alle Rechnungen sind bezahlt.|almost
Ein Teil der Arbeit ist erledigt.|part
""",quantity_labels,'Which quantity relation is expressed?')

acc_frames = [
 ('Ich denke','an','den Termin','daran','woran'),
 ('Wir warten','auf','die Antwort','darauf','worauf'),
 ('Sie bewirbt sich','um','die Stelle','darum','worum'),
 ('Er spricht','über','das Problem','darüber','worüber'),
 ('Ich freue mich','auf','die Reise morgen','darauf','worauf'),
 ('Wir freuen uns','über','das Geschenk hier','darüber','worüber'),
 ('Sie interessiert sich','für','den Kurs','dafür','wofür'),
 ('Er kümmert sich','um','die Reparatur','darum','worum'),
 ('Ich erinnere mich','an','den Urlaub','daran','woran'),
 ('Wir bitten','um','eine Auskunft','darum','worum'),
 ('Sie antwortet','auf','die Frage','darauf','worauf'),
 ('Er verzichtet','auf','das Auto','darauf','worauf'),
 ('Ich glaube','an','den Erfolg','daran','woran'),
 ('Wir achten','auf','die Regeln','darauf','worauf'),
 ('Sie beschwert sich','über','den Lärm','darüber','worüber'),
 ('Er entscheidet sich','für','das Angebot','dafür','wofür'),
 ('Ich bereite mich','auf','die Prüfung vor','darauf','worauf'),
 ('Wir diskutieren','über','den Plan','darüber','worüber'),
 ('Sie sorgt','für','die Verpflegung','dafür','wofür'),
 ('Er kämpft','gegen','das Verbot','dagegen','wogegen'),
]
for start, prep, obj, da, wo in acc_frames:
    article,rest=obj.split(' ',1)
    choices=['den','die','das','dem','der','des'] if article in ('den','die','das') else ['eine','einen','einem','einer']
    kind='bestimmter Artikel' if article in ('den','die','das') else 'ein-Artikel'
    LESSONS.setdefault(63, []).append(question(f'{start} {prep} ___ {rest}. ({kind})',article,
        [x for x in choices if x!=article][:3],
        f"This fixed '{prep}' frame takes accusative; '{article}' matches the stated definite/indefinite noun phrase.",'Complete the required accusative article.'))

dat_frames = [
 ('Ich nehme','an','einer Weiterbildung teil'),('Wir sprechen','mit','der Leiterin'),
 ('Die Gruppe besteht','aus','zehn Personen'),('Er erzählt','von','seiner Reise'),
 ('Ich frage','nach','dem Weg'),('Wir gehören','zu','diesem Team'),
 ('Sie träumt','von','einem Haus'),('Das hängt','von','der Entscheidung ab'),
 ('Ich rechne','mit','einer Antwort'),('Wir beginnen','mit','der Arbeit'),
 ('Sie leidet','an','einer Krankheit'),('Er leidet','unter','dem Lärm'),
 ('Ich zweifle','an','der Erklärung'),('Wir gratulieren','zu','deinem Erfolg'),
 ('Sie arbeitet','an','einem Projekt'),('Er warnt','vor','dem Gewitter'),
 ('Ich entschuldige mich','bei','der Kollegin'),('Wir verabschieden uns','von','den Gästen'),
 ('Sie erholt sich','von','der Operation'),('Er beschäftigt sich','mit','der Grammatik'),
]
for start, prep, obj in dat_frames:
    article,rest=obj.split(' ',1)
    if article=='zehn':
        LESSONS.setdefault(64, []).append(question(f'{start} ___ {obj}.',prep,['mit','von','nach'],
            'Bestehen aus names the components or members and governs dative.','Complete the composition frame.'))
    else:
        if article in ('dem','der','den'):
            choices=['dem','der','den','die','das','des']; kind='bestimmter Artikel'
        elif article in ('einem','einer'):
            choices=['einem','einer','einen','eine']; kind='ein-Artikel'
        else:
            root=next(x for x in ['dies','dein','sein','mein','unser','euer','ihr'] if article.startswith(x))
            choices=[root+e for e in ['em','er','en','e']]; kind=root+'-Artikel'
        LESSONS.setdefault(64, []).append(question(f'{start} {prep} ___ {rest}. ({kind})',article,
            [x for x in choices if x!=article][:3],
            f"This verb uses '{prep}' with a dative complement; '{article}' matches the noun's gender/number and determiner type.",'Complete the required dative determiner.'))

two_frames = [
 ('Ich bedanke mich','bei meiner Kollegin','für die Hilfe'),
 ('Wir sprechen','mit dem Chef','über den Vertrag'),
 ('Sie entschuldigt sich','bei dem Kunden','für den Fehler'),
 ('Er beschwert sich','bei der Verwaltung','über den Lärm'),
 ('Ich bewerbe mich','bei einer Firma','um eine Stelle'),
 ('Wir erkundigen uns','bei der Leiterin','nach dem Termin'),
 ('Sie bedankt sich','bei den Nachbarn','für das Geschenk'),
 ('Er spricht','mit seiner Schwester','über die Reise'),
 ('Ich entschuldige mich','bei meiner Freundin','für die Verspätung'),
 ('Wir beschweren uns','bei dem Anbieter','über die Rechnung'),
 ('Sie bewirbt sich','bei einem Verlag','um einen Ausbildungsplatz'),
 ('Er erkundigt sich','bei dem Mitarbeiter','nach dem Preis'),
 ('Ich bedanke mich','bei meinem Bruder','für die Einladung'),
 ('Wir sprechen','mit den Eltern','über die Schule'),
 ('Sie entschuldigt sich','bei der Lehrerin','für das Verhalten'),
 ('Er beschwert sich','bei dem Vermieter','über die Heizung'),
 ('Ich bewerbe mich','bei der Bank','um ein Praktikum'),
 ('Wir erkundigen uns','bei dem Arzt','nach dem Ergebnis'),
 ('Sie bedankt sich','bei ihrer Mutter','für die Unterstützung'),
 ('Er spricht','mit dem Kollegen','über das Projekt'),
]
for start, first, second in two_frames:
    prep1, rest1 = first.split(' ',1); prep2, rest2=second.split(' ',1)
    wrong=[f'{prep2} {rest1} {prep1} {rest2}',f'ohne {rest1} wegen {rest2}',f'gegen {rest1} aus {rest2}']
    LESSONS.setdefault(65, []).append(question(f'{start} ___. (Person: {rest1}; Sache: {rest2})',f'{first} {second}',wrong,
        f"This verb frame combines '{prep1}' for the person with '{prep2}' for the topic, reason or goal; both complements must be preserved.",'Choose both required prepositional complements.'))

gaps(66, 'mit|an|auf|für|von|über|zu|dem|der', """
Ich bin ___ dem Ergebnis zufrieden.|mit
Sie ist ___ ihren Erfolg stolz.|auf
Wir sind ___ dem Kurs interessiert.|an
Er ist ___ die Hilfe dankbar.|für
Ich bin ___ meinen Eltern abhängig.|von
Sie ist ___ das Geschenk froh.|über
Wir sind ___ dem Vorschlag einverstanden.|mit
Er ist ___ der Reise bereit.|zu
Ich bin ___ den Fehler verantwortlich.|für
Sie ist ___ ihre Tochter besorgt.|um|Besorgt um takes accusative and names the person one worries about.
Das Kind ist ___ Vater ähnlich.|dem
Die Lösung ist ___ ersten ähnlich.|der
Ich bin ___ das Ergebnis gespannt.|auf
Sie ist ___ die Nachricht glücklich.|über
Wir sind ___ dem Service unzufrieden.|mit
Er ist ___ seinem Erfolg überzeugt.|von
Ich bin ___ Fremden freundlich. (gegenüber + Personen; Präposition)|gegenüber|Freundlich gegenüber takes dative; gegenüber marks the people treated kindly.
Sie ist ___ Musik interessiert.|an
Wir sind ___ diesen Aufgaben fähig.|zu
Er ist ___ den Termin froh.|über
""", "The adjective requires the fixed complement shown by '{answer}'; learn the adjective together with its preposition or dative object.")

person_questions = [
 ('Du sprichst mit einer Person.','Mit wem'),('Du wartest auf eine Person.','Auf wen'),
 ('Du denkst an eine Person.','An wen'),('Du erzählst von einer Person.','Von wem'),
 ('Du kaufst das für eine Person.','Für wen'),('Du beschwerst dich bei einer Person.','Bei wem'),
 ('Du erkundigst dich nach einer Person.','Nach wem'),('Du gehst zu einer Person.','Zu wem'),
 ('Du sprichst über eine Person.','Über wen'),('Du kümmerst dich um eine Person.','Um wen'),
 ('Du arbeitest mit einer Person.','Mit wem'),('Du freust dich auf eine Person.','Auf wen'),
 ('Du erinnerst dich an eine Person.','An wen'),('Du verabschiedest dich von einer Person.','Von wem'),
 ('Du sorgst für eine Person.','Für wen'),('Du entschuldigst dich bei einer Person.','Bei wem'),
 ('Du fragst nach einer Person.','Nach wem'),('Du gehörst zu einer Gruppe von Personen.','Zu wem'),
 ('Du lachst über eine Person.','Über wen'),('Du bittest um eine Person als Helfer.','Um wen'),
]
for sentence, answer in person_questions:
    prep, pronoun = answer.split()
    other = 'wen' if pronoun=='wem' else 'wem'
    LESSONS.setdefault(67, []).append(question(f'{sentence} Frage nach dieser Person: ___?',answer,
        [f'{prep} {other}',f'Wo{prep.lower()}', 'Was'],
        f"For a person, keep '{prep.lower()}' and use {'dative wem' if pronoun=='wem' else 'accusative wen'} rather than a wo-compound.",'Choose the personal prepositional question.'))

for start, prep, obj, da, wo in acc_frames:
    # Keep separable vor outside the replaced prepositional object.
    tail = ' vor' if start == 'Ich bereite mich' else ''
    full = f'{start} {prep} {obj}.'
    LESSONS.setdefault(68, []).append(question(f'{full} Ersetze die Sache durch ein da-Wort: {start} ___{tail}.', da,
        [x for x in ['daran','darauf','darum','darüber','dafür','dagegen'] if x!=da][:3],
        f"The thing-complement of '{prep}' becomes '{da}'; add r between da and a vowel-initial preposition.",'Replace the thing/proposition with a da-compound.'))
    LESSONS.setdefault(69, []).append(question(f'{full} Frage nach der Sache mit einem wo-Wort: ___?', wo,
        [x for x in ['woran','worauf','worum','worüber','wofür','wogegen'] if x!=wo][:3],
        f"Keep the required preposition '{prep}': its question compound is '{wo}', with r before a vowel.",'Choose the wo-compound for this thing.'))

infinitives = [
 ('den Antrag abschicken','den Antrag abzuschicken','den Antrag zu abschicken','den Antrag abschicken zu','den Antrag abgeschickt'),
 ('die Rechnung bezahlen','die Rechnung zu bezahlen','die Rechnung bezahlen zu','die Rechnung zu bezahlt','die Rechnung bezahlt'),
 ('früh aufstehen','früh aufzustehen','früh zu aufstehen','früh aufstehen zu','früh aufgestanden'),
 ('die Tür öffnen','die Tür zu öffnen','die Tür öffnen zu','die Tür zu geöffnet','die Tür geöffnet'),
 ('das Zimmer aufräumen','das Zimmer aufzuräumen','das Zimmer zu aufräumen','das Zimmer aufräumen zu','das Zimmer aufgeräumt'),
 ('Deutsch lernen','Deutsch zu lernen','Deutsch lernen zu','Deutsch zu gelernt','Deutsch gelernt'),
 ('pünktlich ankommen','pünktlich anzukommen','pünktlich zu ankommen','pünktlich ankommen zu','pünktlich angekommen'),
 ('die Datei speichern','die Datei zu speichern','die Datei speichern zu','die Datei zu gespeichert','die Datei gespeichert'),
 ('sich anmelden','sich anzumelden','sich zu anmelden','sich anmelden zu','sich angemeldet'),
 ('die Frage beantworten','die Frage zu beantworten','die Frage beantworten zu','die Frage zu beantwortet','die Frage beantwortet'),
]
for unit, prefixes in {
 70:['Ich versuche,','Sie hat vergessen,'],
 71:['Es ist wichtig,','Es ist möglich,'],
 72:['Wir haben die Möglichkeit,','Ich habe die Absicht,'],
}.items():
    for prefix in prefixes:
        for bare, correct, a,b,c in infinitives:
            # Reflexive pronoun must agree with the controller.
            if bare=='sich anmelden':
                pronoun = 'uns' if prefix.startswith('Wir') else 'mich' if prefix.startswith('Ich') else 'sich'
                correct,a,b,c = [x.replace('sich',pronoun) for x in [correct,a,b,c]]
            LESSONS.setdefault(unit, []).append(question(f'{prefix} ___. ({bare})',correct,[a,b,c],
                f"This {'verb' if unit==70 else 'adjective expression' if unit==71 else 'noun'} takes a zu-infinitive; in separable verbs, zu goes between prefix and stem.",'Complete the infinitive group.'))

gaps(73, 'hilft|helfen|ist|sind|freut|freuen|bleibt|bleiben', """
Dass du pünktlich kommst, ___ mir. (helfen)|hilft
Deutsch zu lernen, ___ wichtig. (sein)|ist
Was er erzählt, ___ mich. (freuen)|freut
Wann wir fahren, ___ offen. (bleiben)|bleibt
Dass alle mithelfen, ___ uns. (helfen)|hilft
Früh aufzustehen, ___ schwierig. (sein)|ist
Wer die Leitung übernimmt, ___ unklar. (bleiben)|bleibt
Dass ihr anruft, ___ mich. (freuen)|freut
Regelmäßig zu üben, ___ beim Lernen. (helfen)|hilft
Ob er kommt, ___ unsicher. (sein)|ist
Dass sie Zeit hat, ___ uns. (helfen)|hilft
Was du sagst, ___ richtig. (sein)|ist
Dass wir uns sehen, ___ mich. (freuen)|freut
Wie es weitergeht, ___ offen. (bleiben)|bleibt
Die Regeln zu kennen, ___ wichtig. (sein)|ist
Dass du Bescheid sagst, ___ der Gruppe. (helfen)|hilft
Ob die Plätze reichen, ___ unklar. (bleiben)|bleibt
Mit Freunden zu lernen, ___ schön. (sein)|ist
Dass alle bestanden haben, ___ mich. (freuen)|freut
Wann sie zurückkommen, ___ unbekannt. (sein)|ist
""", "The entire subject clause or infinitive group counts as one subject, so the main predicate takes singular '{answer}'.")

for unit, connector, main_prefixes in [
 (74,'ohne',['Er geht,','Sie geht,']),
 (75,'statt',['Er sieht fern,','Sie sieht fern,'])]:
    actions = [
      ('sich verabschieden','sich zu verabschieden'),('Bescheid sagen','Bescheid zu sagen'),
      ('die Rechnung bezahlen','die Rechnung zu bezahlen'),('die Tür abschließen','die Tür abzuschließen'),
      ('den Antrag abgeben','den Antrag abzugeben'),('die Datei speichern','die Datei zu speichern'),
      ('das Licht ausschalten','das Licht auszuschalten'),('die Kollegin anrufen','die Kollegin anzurufen'),
      ('sich anmelden','sich anzumelden'),('die Frage beantworten','die Frage zu beantworten')]
    for prefix in main_prefixes:
        for bare, correct in actions:
            wrong=[bare,'zu '+correct,correct+' ist']
            LESSONS.setdefault(unit, []).append(question(f'{prefix} {connector} ___. ({bare})',correct,wrong,
                f"{connector.capitalize()} … zu {'names an omitted accompanying action' if unit==74 else 'names an alternative action not taken'}; the infinitive shares the main clause's subject.",'Complete the shared-subject infinitive clause.'))

gaps(76, 'reparieren|zu reparieren|repariert|reparierte|lassen|gelassen|ließ|lässt', """
Ich lasse mein Fahrrad ___. (reparieren)|reparieren
Sie hat ihr Fahrrad reparieren ___. (Perfekt von lassen)|lassen
Gestern ___ er sein Fahrrad reparieren. (Präteritum von lassen)|ließ
Sie ___ ihr Fahrrad reparieren. (Präsens, 3. Person)|lässt
Wir lassen den Drucker ___. (reparieren)|reparieren
Er hat den Drucker reparieren ___. (Perfekt)|lassen
Gestern ___ sie den Drucker reparieren. (Singular, Präteritum)|ließ
Er ___ den Drucker reparieren. (Präsens)|lässt
Ich lasse das Auto ___. (reparieren)|reparieren
Sie hat das Auto reparieren ___. (Perfekt)|lassen
""", {'reparieren':'Lassen takes a bare infinitive; the speaker arranges for someone to repair the item.', 'lassen':'With another infinitive in the Perfekt, lassen uses the replacement infinitive: hat reparieren lassen.', 'ließ':'Ließ is the singular Präteritum of lassen.', 'lässt':'Third-person singular present is lässt.', 'zu reparieren':'Lassen requires the infinitive without zu.', 'repariert':'A participle does not complete lassen here.', 'reparierte':'The lexical verb remains an infinitive after lassen.', 'gelassen':'Gelassen is used when lassen is not governing another infinitive in this construction.'})

meanings(76,"""
Ich lasse mein Fahrrad reparieren.|service
Die Eltern lassen das Kind draußen spielen.|permission
Lass die Tür bitte offen!|unchanged
Sie lässt sich die Haare schneiden.|service
Der Chef lässt uns früher gehen.|permission
Wir lassen alles, wie es ist.|unchanged
Er lässt das Auto in der Werkstatt prüfen.|service
Die Lehrerin lässt die Schüler nachfragen.|permission
Lass das Fenster geschlossen!|unchanged
Ich lasse die Heizung vom Techniker warten.|service
""",{
 'service':('Arranging a service by someone else','Lassen plus infinitive means arranging a service rather than necessarily doing it personally.'),
 'permission':('Allowing another person to act','Lassen with another person and infinitive expresses permission in this context.'),
 'unchanged':('Leaving an existing condition unchanged','Lassen with a state expression means keeping that state as it is.'),
 'prohibition':('Explicitly forbidding an action','A prohibition would require negative permission; these positive lassen frames do not forbid the action.'),
},'What does lassen mean in this context?')

bare_actions=[('Ich gehe','einkaufen'),('Wir gehen','schwimmen'),('Sie bleibt','sitzen'),('Er bleibt','stehen'),('Ich höre die Kinder','lachen'),('Wir sehen den Bus','kommen'),('Sie hört den Hund','bellen'),('Er sieht die Nachbarin','laufen'),('Ich gehe','spazieren'),('Wir bleiben','liegen')]
for prefix,verb in bare_actions:
    for tail in ['heute','morgen']:
        words=prefix.split()
        frame=f'{tail.capitalize()} {words[1]} {words[0].lower()} '+ ' '.join(words[2:])
        LESSONS.setdefault(77, []).append(question(f'{frame.strip()} ___. ({verb})',verb,
            ['zu '+verb,'ge'+verb,verb+' zu'],
            f"In this familiar {'movement' if 'gehe' in prefix else 'position/perception'} construction, '{verb}' is a bare infinitive without zu.",'Choose the infinitive required by this construction.'))

gaps(78, 'zu|um|für|ohne', """
Du brauchst heute nicht ___ kommen.|zu
Ich brauche das Formular nicht aus___füllen. (ein Wort)|zu
Wir brauchen nicht länger ___ warten.|zu
Sie braucht morgen nicht ___ arbeiten.|zu
Ihr braucht nicht früh auf___stehen. (ein Wort)|zu
Er braucht das nicht ___ bezahlen.|zu
Du brauchst den Brief nicht ab___schicken. (ein Wort)|zu
Wir brauchen nicht ___ fahren.|zu
Ich brauche nicht noch einmal an___rufen. (ein Wort)|zu
Sie braucht nicht ___ kochen.|zu
""", "In the formal written model, negative brauchen takes zu plus infinitive and means 'do not need to', not 'must not'. With a separable verb, zu goes inside it.")

meanings(78,"""
Du brauchst heute nicht zu kommen.|noneed
Du musst heute nicht kommen.|noneed
Du darfst heute nicht kommen.|forbidden
Du musst heute kommen.|necessary
Ihr braucht nichts mitzubringen.|noneed
Sie braucht die Gebühr nicht zu zahlen.|noneed
Hier darf nicht geraucht werden.|forbidden
Wir müssen jetzt gehen.|necessary
Ihr dürft heute früher gehen.|allowed
Du brauchst dich nicht anzumelden.|noneed
""",{
 'noneed':('The action is unnecessary, not forbidden','Nicht brauchen … zu and nicht müssen remove necessity; they do not impose a prohibition.'),
 'forbidden':('The action is forbidden','Nicht dürfen denies permission, unlike nicht brauchen … zu.'),
 'necessary':('The action is required','Positive müssen states an obligation rather than lack of necessity.'),
 'allowed':('The action is permitted','Positive dürfen grants permission rather than stating a requirement.'),
},'Distinguish unnecessary, forbidden, required and permitted.')

modal_labels = {
 'need':('A requirement or relayed instruction', 'Müssen expresses a requirement; sollen can relay an instruction from someone else.'),
 'permission':('Permission or prohibition', 'Dürfen concerns permission; nicht dürfen prohibits the action.'),
 'ability':('An ability or possibility', 'Können concerns capability or possibility, not an obligation.'),
 'intention':('A wish or intention', 'Wollen expresses the subject’s intention rather than permission from someone else.'),
 'noneed':('No necessity', 'Nicht müssen means the action is unnecessary, not forbidden.'),
}
meanings(79, """
Ich muss den Antrag heute abgeben.|need
Du darfst hier nicht rauchen.|permission
Sie kann schon gut schwimmen.|ability
Wir wollen morgen umziehen.|intention
Ihr müsst nicht kommen; es ist freiwillig.|noneed
Die Ärztin sagt, ich soll mich ausruhen.|need
Du darfst das Buch mitnehmen.|permission
Er kann den schweren Koffer tragen.|ability
Sie will einen neuen Beruf lernen.|intention
Du musst nicht bezahlen; ich lade dich ein.|noneed
Wir müssen vor acht losfahren.|need
Hier dürfen nur Mitarbeiter hinein.|permission
Ich kann dir morgen helfen.|ability
Er will die Ausbildung abschließen.|intention
Wir müssen nicht reservieren; es gibt genug Platz.|noneed
Der Chef sagt, wir sollen anrufen.|need
Ihr dürft keine Fotos machen.|permission
Sie kann die Aufgabe allein lösen.|ability
Ich will heute früh schlafen.|intention
Sie muss nicht warten; sie kann sofort gehen.|noneed
""",modal_labels,'What does the modal verb mean in this context?')

phase_labels = {
 'appearance':('It appears to be the case', 'Scheinen plus zu-infinitive marks an appearance or inference, not a confirmed fact.'),
 'begin':('The action starts', 'Beginnen/anfangen plus zu-infinitive identifies the beginning of an action.'),
 'habit':('A habitual action', 'Pflegen plus zu-infinitive means habitually do; it does not mean taking care of someone here.'),
 'light':('Literal shining', 'Scheinen without a governed zu-infinitive can describe sunlight, not an inference.'),
}
meanings(80, """
Die Sitzung scheint länger zu dauern.|appearance
Er beginnt zu sprechen.|begin
Sie pflegt früh aufzustehen.|habit
Die Sonne scheint heute hell.|light
Der Kurs scheint auszufallen.|appearance
Wir fangen an zu arbeiten.|begin
Er pflegt abends spazieren zu gehen.|habit
Das Licht scheint durch das Fenster.|light
Sie scheint krank zu sein.|appearance
Das Kind beginnt zu weinen.|begin
Wir pflegen sonntags gemeinsam zu essen.|habit
Die Sonne scheint auf den Balkon.|light
Er scheint die Antwort zu kennen.|appearance
Sie fängt an zu lachen.|begin
Die Leiterin pflegt pünktlich zu kommen.|habit
Am Nachmittag scheint die Sonne.|light
Der Plan scheint zu funktionieren.|appearance
Wir beginnen, die Räume aufzuräumen.|begin
Er pflegt seine Briefe sofort zu beantworten.|habit
Das Sonnenlicht scheint durch die Wolken.|light
""",phase_labels,'How is the verb used in this sentence?')
