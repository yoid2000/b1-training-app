from .core import gaps, meanings, explicit, LESSONS, question

relatives = [
 ('der Mann','m','hier wohnt','ich auf dem Foto sehe'),
 ('die Frau','f','im Büro arbeitet','ich gestern getroffen habe'),
 ('das Kind','n','im Garten spielt','ich von früher kenne'),
 ('die Nachbarn','p','neben uns wohnen','ich zum Essen eingeladen habe'),
 ('der Kurs','m','morgen beginnt','ich besuchen möchte'),
 ('die Wohnung','f','im Zentrum liegt','ich mieten möchte'),
 ('das Buch','n','auf dem Tisch liegt','ich gerade lese'),
 ('die Geräte','p','wieder funktionieren','ich repariert habe'),
 ('der Zug','m','nach Köln fährt','ich nehmen werde'),
 ('die Tasche','f','mir gehört','ich im Laden gekauft habe'),
 ('das Auto','n','dort steht','ich gestern gefahren habe'),
 ('die Briefe','p','heute angekommen sind','ich beantwortet habe'),
 ('der Film','m','heute läuft','ich sehen will'),
 ('die Schule','f','neu eröffnet wird','ich früher besucht habe'),
 ('das Hotel','n','am See liegt','ich gebucht habe'),
 ('die Gäste','p','gerade ankommen','ich begrüßen möchte'),
 ('der Arzt','m','mir geholfen hat','ich morgen anrufen werde'),
 ('die Leiterin','f','den Kurs organisiert','ich noch nicht kenne'),
 ('das Geschäft','n','sonntags schließt','ich sehr gern besuche'),
 ('die Bücher','p','hier im Regal stehen','ich ausgeliehen habe'),
]
for noun,g,nom_clause,acc_clause in relatives:
    for unit,clause,correct in [(107,nom_clause,{'m':'der','f':'die','n':'das','p':'die'}[g]),(108,acc_clause,{'m':'den','f':'die','n':'das','p':'die'}[g])]:
        intro='Das sind' if g=='p' else 'Das ist'
        LESSONS.setdefault(unit, []).append(question(f'{intro} {noun}, ___ {clause}.',correct,
            [x for x in ['der','die','das','den','dem','denen'] if x!=correct][:3],
            f"The antecedent '{noun}' supplies gender/number, while the pronoun is {'the nominative subject' if unit==107 else 'the accusative object'} inside the relative clause.",'Complete the relative pronoun.'))
    correct='dessen' if g in ('m','n') else 'deren'
    LESSONS.setdefault(111, []).append(question(f'Hier sehen wir {noun.replace("der ","den ",1) if g=="m" else noun}, ___ Beschreibung ich gelesen habe.',correct,
        ['deren' if correct=='dessen' else 'dessen','denen','dem'],
        f"'{noun}' is {'masculine/neuter singular' if g in ('m','n') else 'feminine singular/plural'}, so relative possession uses '{correct}'. The case of Beschreibung does not change this choice.",'Choose the possessive relative pronoun.'))

gaps(109,'dem|der|denen|den|die|das',"""
Das ist der Kollege, ___ ich geholfen habe.|dem
Das ist die Frau, ___ ich danke.|der
Das sind die Kinder, ___ ich zuhöre.|denen
Hier ist das Kind, ___ der Hund folgt.|dem
Das ist der Arzt, ___ ich vertraue.|dem
Die Nachbarin, ___ wir begegnet sind, ist nett.|der
Die Gäste, ___ das Essen schmeckt, bleiben.|denen
Das ist der Lehrer, ___ ich antworte.|dem
Die Freundin, ___ das Buch gehört, kommt.|der
Die Kollegen, ___ die Zeit fehlt, gehen.|denen
Das ist der Mann, ___ die Jacke passt.|dem
Das Mädchen, ___ ich gratuliere, freut sich.|dem
Die Eltern, ___ ich schreibe, wohnen hier.|denen
Die Leiterin, ___ wir zustimmen, erklärt weiter.|der
Der Junge, ___ ich das Rad leihe, ist zwölf.|dem
Die Kundin, ___ ich die Rechnung schicke, wartet.|der
Die Teilnehmer, ___ der Kurs gefällt, kommen wieder.|denen
Der Freund, ___ ich Bescheid sage, arbeitet noch.|dem
Die Frau, ___ er das Paket bringt, wohnt oben.|der
Die Menschen, ___ das hilft, sind dankbar.|denen
""",{'dem':'The relative clause requires dative; masculine and neuter singular use dem.', 'der':'The relative clause requires dative; feminine singular uses der.', 'denen':'The relative clause requires dative; plural relative pronouns use denen, not den.', 'den':'Den is accusative masculine, not the required dative relative.', 'die':'Die is not a dative relative form.', 'das':'Das is nominative/accusative neuter, not dative.'})

gaps(110,'mit dem|mit der|mit denen|für den|für die|auf den|auf die|in dem|in der|bei der|an dem|über den|über die|von dem|von der',"""
Das ist der Kollege, ___ ich spreche. (sprechen mit)|mit dem
Das ist die Frau, ___ ich arbeite. (arbeiten mit)|mit der
Das sind die Leute, ___ ich reise. (reisen mit)|mit denen
Das ist der Mann, ___ ich das Geschenk kaufe. (für)|für den
Das sind die Kinder, ___ wir kochen. (für)|für die
Hier ist der Bus, ___ wir warten. (warten auf)|auf den
Das ist die Antwort, ___ ich warte. (auf)|auf die
Das ist das Büro, ___ sie arbeitet. (in; Ort)|in dem
Das ist die Wohnung, ___ wir leben. (in; Ort)|in der
Die Firma, ___ sie arbeitet, ist klein. (bei)|bei der
Das ist der Tag, ___ die Prüfung stattfindet. (an)|an dem
Der Film, ___ wir sprechen, ist neu. (über)|über den
Die Reise, ___ sie erzählt, war lang. (von)|von der
Der Nachbar, ___ ich das weiß, wohnt hier. (von)|von dem
Das sind die Fragen, ___ wir reden. (über)|über die
Die Freundin, ___ ich telefoniere, kommt morgen. (mit)|mit der
Das Haus, ___ er wohnt, ist alt. (in)|in dem
Die Schule, ___ die Kinder lernen, ist neu. (in)|in der
Das Kind, ___ ich spiele, ist müde. (mit)|mit dem
Die Gäste, ___ ich gesprochen habe, sind nett. (mit)|mit denen
""", "The preposition remains immediately before the relative pronoun; '{answer}' combines it with the gender/number and case required inside the relative clause.")

embedded = [
 ('Ich weiß, dass der Kurs, den du empfiehlst, morgen beginnt.','beginnt','empfiehlst'),
 ('Sie sagt, dass die Frau, die hier wohnt, morgen kommt.','kommt','wohnt'),
 ('Wir hoffen, dass das Gerät, das er repariert, wieder funktioniert.','funktioniert','repariert'),
 ('Er glaubt, dass der Bus, auf den wir warten, bald abfährt.','abfährt','warten'),
 ('Ich sehe, dass das Kind, dem sie hilft, schon lächelt.','lächelt','hilft'),
 ('Sie merkt, dass der Schlüssel, den sie sucht, auf dem Tisch liegt.','liegt','sucht'),
 ('Wir wissen, dass die Firma, bei der er arbeitet, Personal braucht.','braucht','arbeitet'),
 ('Er sagt, dass das Buch, das ich lese, ihm gehört.','gehört','lese'),
 ('Ich glaube, dass die Gäste, die du eingeladen hast, heute kommen.','kommen','hast'),
 ('Sie hofft, dass die Wohnung, die wir mieten möchten, noch frei ist.','ist','möchten'),
]
for sentence,outer,inner in embedded:
    for target,correct,wrongword in [('dass-Satz',outer,inner),('eingeschobenen Relativsatz',inner,outer)]:
        wrong=[wrongword,'the infinitive marker zu','the first verb of the whole sentence']
        LESSONS.setdefault(112, []).append(question(sentence+f' Welches finite Verb gehört zum {target}?',correct,wrong,
            f"'{correct}' closes the {target}; the embedded clause has its own verb and comma boundaries.",'Identify the clause’s own finite verb.'))

transfers=[('gebe','das Buch','es','dem Mann','ihm'),('schicke','den Brief','ihn','der Frau','ihr'),('zeige','das Foto','es','den Kindern','ihnen'),('bringe','die Tasche','sie','meinem Bruder','ihm'),('leihe','den Wagen','ihn','meiner Schwester','ihr'),('erkläre','die Regel','sie','den Gästen','ihnen'),('reiche','das Formular','es','dem Kunden','ihm'),('schenke','die Blumen','sie','meiner Mutter','ihr'),('empfehle','den Film','ihn','der Kollegin','ihr'),('verkaufe','das Rad','es','dem Nachbarn','ihm')]
for verb,obj,acc,recipient,dat in transfers:
    for pronoun_before_noun in (True,False):
        correct=f'{dat} {obj}' if pronoun_before_noun else f'{acc} {dat}'
        wrong=[f'{obj} {dat}',f'{recipient} {acc}',f'{dat} {acc}'] if pronoun_before_noun else [f'{dat} {acc}',f'{recipient} {acc}',f'{dat} {obj}']
        LESSONS.setdefault(113, []).append(question(f'Morgen {verb} ich ___. (Ersetze {recipient} durch {dat}'+(f'; {obj} bleibt ein Nomen.)' if pronoun_before_noun else f' und {obj} durch {acc}.)'),correct,wrong,
            'In neutral order, an unstressed pronoun precedes a full noun object; with two unstressed pronouns, accusative precedes dative.','Choose the neutral order and make exactly the requested substitutions.'))

neg_scope={
 'person':('The person is corrected','Nicht immediately before the named person, followed by sondern, rejects that person as the relevant alternative.'),
 'time':('The time is corrected','The focused time phrase after nicht is replaced by the time after sondern.'),
 'place':('The place is corrected','Nicht … sondern contrasts the two place phrases rather than negating the whole event.'),
 'whole':('The whole action is denied','With no corrective constituent contrast, the sentence denies that the stated event took place.'),
}
meanings(114,"""
Nicht Anna, sondern Paul hat angerufen.|person
Er kommt nicht morgen, sondern am Freitag.|time
Sie wohnt nicht in Bonn, sondern in Köln.|place
Er hat den Brief nicht abgeschickt.|whole
Nicht der Chef, sondern die Kollegin hilft.|person
Die Prüfung ist nicht heute, sondern nächste Woche.|time
Wir treffen uns nicht im Büro, sondern im Café.|place
Sie hat die Rechnung nicht bezahlt.|whole
Nicht ich, sondern mein Bruder fährt.|person
Wir fahren nicht im Juni, sondern im Juli.|time
Er arbeitet nicht hier, sondern dort.|place
Ich habe das Fenster nicht geöffnet.|whole
Nicht die Lehrerin, sondern der Schüler liest.|person
Sie kommt nicht um acht, sondern um neun.|time
Das Paket liegt nicht auf dem Tisch, sondern im Schrank.|place
Wir haben den Film nicht gesehen.|whole
Nicht du, sondern sie bekommt den Schlüssel.|person
Der Kurs beginnt nicht montags, sondern dienstags.|time
Wir gehen nicht ins Kino, sondern ins Theater.|place
Er kann heute nicht mitkommen.|whole
""",neg_scope,'What is the scope of the negation in this context?')

references={
 'man':('A previously named male person','Er/ihm takes up the male person in the preceding sentence.'),
 'woman':('A previously named female person','Sie/ihr takes up the female person in the preceding sentence.'),
 'plural':('Several previously named people or things','A plural personal pronoun takes up the plural antecedent.'),
 'thing':('One previously named thing','The singular personal pronoun agrees with the named noun, not necessarily with natural gender.'),
 'fact':('The preceding fact or proposition','The da-compound points to the situation or fact just stated, not to a person.'),
}
meanings(115,"""
Paul wartet. Er ist nervös. (Er)|man
Anna kommt. Sie hat Zeit. (Sie)|woman
Die Gäste sind da. Sie warten draußen. (Sie)|plural
Das Gerät ist kaputt. Es wird repariert. (Es)|thing
Der Kurs fällt aus. Darüber bin ich enttäuscht. (Darüber)|fact
Der Nachbar hilft. Ich danke ihm. (ihm)|man
Die Lehrerin erklärt alles. Ich höre ihr zu. (ihr)|woman
Die Bücher sind teuer. Ich kaufe sie später. (sie)|plural
Die Tasche ist schön. Ich nehme sie. (sie)|thing
Wir haben bestanden. Darüber freuen wir uns. (Darüber)|fact
Mein Bruder reist ab. Er ruft morgen an. (Er)|man
Meine Schwester ist krank. Ihr fehlt die Arbeit. (Ihr)|woman
Die Kinder sind müde. Sie schlafen bald. (Sie)|plural
Der Vertrag ist fertig. Er liegt im Büro. (Er)|thing
Die Rechnung fehlt. Darauf weisen wir hin. (Darauf)|fact
Der Arzt kommt. Ich frage ihn. (ihn)|man
Die Kundin wartet. Ich helfe ihr. (ihr)|woman
Die Fenster sind offen. Wir schließen sie. (sie)|plural
Das Buch ist spannend. Es gefällt mir. (Es)|thing
Er hat rechtzeitig geholfen. Dafür danke ich ihm. (Dafür)|fact
""",references,'What does the pronoun or compound in parentheses refer to?')

ellipsis={
 'subject':('The same subject is understood again','The second coordinated predicate shares the first subject; the person has not changed.'),
 'aux':('The subject and auxiliary are shared','A single subject and auxiliary govern both participles; the second participle needs no repeated auxiliary.'),
 'head':('A repeated noun or compound part is omitted','The remaining shared noun or compound part supplies the missing material.'),
 'answer':('A complete clause is understood from a short answer','The dialogue provides the omitted subject and verb in the elliptical answer.'),
}
meanings(116,"""
Anna kocht und räumt anschließend auf.|subject
Sie hat den Antrag ausgefüllt und abgeschickt.|aux
Wir brauchen einen roten und einen blauen Stift. (nach roten)|head
Wann kommst du? — Morgen.|answer
Paul kommt nach Hause und öffnet die Post.|subject
Er hat die Rechnung geprüft und bezahlt.|aux
Sie bestellt Hin- und Rückfahrt. (Hin-)|head
Wer hilft mit? — Die Nachbarn.|answer
Wir essen und gehen dann spazieren.|subject
Wir haben das Zimmer geputzt und gelüftet.|aux
Ich nehme das große und das kleine Buch. (nach große)|head
Wo treffen wir uns? — Im Büro.|answer
Die Lehrerin liest vor und erklärt die Wörter.|subject
Ihr habt angerufen und Bescheid gesagt.|aux
Er verkauft Kinder- und Jugendbücher. (Kinder-)|head
Was brauchst du? — Einen Stift.|answer
Er arbeitet und lernt nebenbei.|subject
Sie hat Brot gekauft und Kaffee gekocht.|aux
Das sind meine alten und neuen Kollegen. (nach alten)|head
Mit wem fährst du? — Mit Anna.|answer
""",ellipsis,'Which material is shared or understood in the marked second part?')

particle_labels={
 'warning':('An emphatic warning','Bloß intensifies the warning or request; it is not a literal reference to being bare or naked.'),
 'soft':('A softened, friendly request','Mal in this request makes it less abrupt; it does not count a literal occurrence.'),
 'shared':('A reminder of something treated as known','Doch/ja presents the information as already known or evident in this dialogue.'),
 'interest':('Interest or surprise in a question','Denn adds conversational interest or surprise; it is not the causal conjunction here.'),
 'accept':('Resigned acceptance of the situation','Halt/eben signals accepting the situation as it is, rather than naming a separate action.'),
}
meanings(117,"""
Könnten Sie bitte mal nachsehen? (mal)|soft
Du weißt es schon: Das ist doch erledigt. (doch)|shared
Was machst du denn hier? (denn)|interest
Der Bus fährt nicht. Dann gehen wir halt zu Fuß. (halt)|accept
Hilf mir bitte mal. (mal)|soft
Wie besprochen: Du hast ja schon bezahlt. (ja)|shared
Wo hast du denn den Schlüssel gefunden? (denn)|interest
Es gibt keine Tickets. Dann bleiben wir eben hier. (eben)|accept
Schau bitte mal auf die Rechnung. (mal)|soft
Wir kennen den Plan: Das weißt du doch. (doch)|shared
Warum bist du denn so früh da? (denn)|interest
Wenn es nicht anders geht, warten wir halt. (halt)|accept
Ruf bitte mal an. (mal)|soft
Du erinnerst dich: Morgen ist ja Feiertag. (ja)|shared
Wie heißt du denn? (denn)|interest
Die Wohnung ist vergeben. Dann suchen wir eben weiter. (eben)|accept
Komm bitte mal her. (mal)|soft
Wir haben es vereinbart: Du kommst doch morgen. (doch)|shared
Wer hat denn angerufen? (denn)|interest
Sei bloß vorsichtig mit dem Glas! (bloß; dringende Warnung)|warning
""",particle_labels,'How does the particle in parentheses function in this dialogue?')

stance={
 'confirmed':('A fact confirmed as actually true','Tatsächlich confirms what really happened, often in contrast to an expectation or earlier uncertainty.'),
 'possible':('A possibility without a firm claim','Vielleicht marks something as possible rather than certain.'),
 'probable':('A likely possibility','Wahrscheinlich expresses probability, not proof or a quotation of someone else.'),
 'hearsay':('A claim attributed to others','Angeblich signals a reported claim without the speaker guaranteeing it.'),
 'evidence':('An inference from apparent evidence','Offenbar presents an inference from what is apparent to the speaker.'),
 'certain':('Strong speaker confidence','Bestimmt presents the speaker as confident, although it is not itself evidence.'),
}
meanings(118,"""
Vielleicht kommt sie morgen.|possible
Wahrscheinlich fährt der Zug später.|probable
Angeblich fällt der Kurs aus.|hearsay
Die Straße ist nass. Offenbar hat es geregnet.|evidence
Er hilft uns bestimmt.|certain
Vielleicht ist die Tür noch offen.|possible
Sie ist wahrscheinlich schon zu Hause.|probable
Angeblich hat er alles bezahlt.|hearsay
Niemand antwortet. Offenbar ist keiner da.|evidence
Die Prüfung zeigt: Das ist tatsächlich richtig.|confirmed
Vielleicht finden wir ein Zimmer.|possible
Wahrscheinlich brauchen wir mehr Zeit.|probable
Angeblich wird das Geschäft verkauft.|hearsay
Das Licht brennt. Offenbar arbeitet noch jemand.|evidence
Sie kennt die Antwort bestimmt.|certain
Vielleicht hat er den Bus verpasst.|possible
Der Preis steigt wahrscheinlich.|probable
Angeblich ist die Reparatur kostenlos.|hearsay
Er trägt einen Gips. Offenbar hat er sich verletzt.|evidence
Wir haben nachgefragt: Er hat tatsächlich bezahlt.|confirmed
""",stance,'What stance does the marked adverb communicate?')

gaps(119,'sie|er|ich|du|ob|dass|wann|wo|am Dienstag|am Mittwoch|am Freitag',"""
Anna sagt: „Ich bin müde.“ Anna sagt, dass ___ müde ist. (Anna)|sie
Paul sagt: „Ich komme später.“ Paul sagt, dass ___ später kommt.|er
Anna sagt: „Ich habe bezahlt.“ Sie sagt, dass ___ bezahlt hat.|sie
Paul sagt: „Ich wohne hier.“ Er sagt, dass ___ hier wohnt.|er
Anna sagt: „Ich lerne Deutsch.“ Sie sagt, dass ___ Deutsch lernt.|sie
Paul sagt: „Ich brauche Hilfe.“ Er sagt, dass ___ Hilfe braucht.|er
„Kommst du?“ Sie fragt mich, ___ ich komme.|ob
„Hast du Zeit?“ Er fragt mich, ___ ich Zeit habe.|ob
„Der Kurs beginnt.“ Sie sagt, ___ der Kurs beginnt.|dass
„Es regnet.“ Er sagt, ___ es regnet.|dass
„Wann fährt der Zug?“ Sie fragt, ___ der Zug fährt.|wann
„Wo ist das Büro?“ Er fragt, ___ das Büro ist.|wo
Am Montag sagt Anna: „Ich komme morgen.“ Später berichtet Paul: Anna kommt ___.|am Dienstag
Am Dienstag sagt Paul: „Ich fahre morgen.“ Später berichtet Anna: Paul fährt ___.|am Mittwoch
Am Donnerstag sagt Anna: „Ich arbeite morgen.“ Später berichtet Paul: Anna arbeitet ___.|am Freitag
Anna sagt zu Paul: „Du bist pünktlich.“ Anna sagt, dass ___ pünktlich ist. (Paul)|er
Paul sagt zu Anna: „Du hast recht.“ Paul sagt, dass ___ recht hat. (Anna)|sie
„Ist das Geschäft offen?“ Er fragt, ___ das Geschäft offen ist.|ob
„Was kostet es?“ Sie fragt, ___ es kostet.|was|An indirect W-question keeps was and places the finite verb kostet last.
„Wie funktioniert es?“ Er fragt, ___ es funktioniert.|wie|The reported manner question retains wie and final verb order.
""",{'sie':'Report Anna with third-person feminine sie, rather than retaining the quoted ich/du.', 'er':'Report Paul with third-person masculine er, rather than retaining the quoted ich/du.', 'ob':'An indirect yes/no question begins with ob and ends with the finite verb.', 'dass':'A reported statement can use indicative dass with final verb order.', 'wann':'Keep wann when reporting a question about time.', 'wo':'Keep wo when reporting a question about location.', 'am Dienstag':'Tomorrow relative to Monday is Tuesday; reporting later requires preserving the original reference day.', 'am Mittwoch':'Tomorrow relative to Tuesday is Wednesday.', 'am Freitag':'Tomorrow relative to Thursday is Friday.'})

compounds=[('Teilnahmebescheinigung','Bescheinigung','die'),('Arbeitszeitregelung','Regelung','die'),('Haustürschlüssel','Schlüssel','der'),('Bahnhofsvorplatz','Platz','der'),('Krankenhauszimmer','Zimmer','das'),('Sprachkursangebot','Angebot','das'),('Fahrkartenautomat','Automat','der'),('Wohnungsbesichtigung','Besichtigung','die'),('Ausbildungsplatzsuche','Suche','die'),('Wettervorhersage','Vorhersage','die'),('Kinderzimmerfenster','Fenster','das'),('Geburtstagsgeschenk','Geschenk','das'),('Verkehrsunfallbericht','Bericht','der'),('Lebensmittelgeschäft','Geschäft','das'),('Reisekrankenversicherung','Versicherung','die'),('Stadtbibliotheksausweis','Ausweis','der'),('Kundendienstmitarbeiter','Mitarbeiter','der'),('Mietvertragskündigung','Kündigung','die'),('Wochenendfahrkarte','Fahrkarte','die'),('Bewerbungsgespräch','Gespräch','das')]
for compound,head,article in compounds:
    LESSONS.setdefault(120, []).append(question(f'Welches Grundwort bestimmt das Genus von „{compound}“?',head,
        ['the first word part','the linking -s- or -n-','the number of syllables'],
        f"The final noun '{head}' is the head: {article} {head}, therefore {article} {compound}. Linking elements do not determine gender.",'Identify the rightmost head noun.'))

prefix_meanings={
 'remove':('Removal or taking something out','In this lexical example, the prefix indicates taking something out or removing it.'),
 'enter':('Putting or going into something','In this lexical example, the prefix expresses entering, inserting or putting something in.'),
 'change':('Changing or doing again','In this lexical example, the prefix indicates a change or a repeated/new arrangement.'),
 'assume':('Taking over or revising work','This lexical item concerns assuming a task or working over it; learn its inseparability with the word.'),
}
meanings(121,"""
Sie nimmt die Batterie heraus. (herausnehmen)|remove
Er packt die Bücher ein. (einpacken)|enter
Wir bauen das Haus um. (umbauen)|change
Die Firma übernimmt den Auftrag. (übernehmen)|assume
Sie zieht den Mantel aus. (ausziehen, Kleidung)|remove
Er steigt in den Bus ein. (einsteigen)|enter
Wir stellen die Möbel um. (umstellen, Möbel)|change
Sie überarbeitet den Entwurf. (überarbeiten)|assume
Er entfernt den Fleck. (entfernen)|remove
Wir tragen die Daten ein. (eintragen)|enter
Sie schreibt den Text um. (umschreiben, neu formulieren)|change
Der Kollege übernimmt die Leitung. (übernehmen)|assume
Ich räume die Tasche aus. (ausräumen)|remove
Sie zieht in die Wohnung ein. (einziehen)|enter
Wir verändern den Plan. (verändern)|change
Er überarbeitet den Bericht. (überarbeiten)|assume
""",prefix_meanings,'Which meaning does the specified prefixed verb have here?')

explicit(121,"""
Der Fahrer fährt den Pfosten um. (trennbares umfahren)|He knocks the post over.|He drives around the post.|He translates the post.|He drives underneath the post.|Separable umfahren places um at the end and means knock over by driving into something.
Der Bus umfährt die Baustelle. (untrennbares umfahren)|The bus drives around the roadworks.|The bus knocks down the roadworks.|The bus is converted into a building site.|The bus drives into the roadworks on purpose.|Inseparable umfahren means bypass or drive around; the prefix stays with the finite verb.
Der Fährmann setzt uns über. (trennbares übersetzen)|The ferryman takes us across the water.|The ferryman translates our words.|The ferryman puts us underneath the boat.|The ferryman postpones our departure.|Separable übersetzen means ferry across; its finite form separates as setzt … über.
Sie übersetzt den Text. (untrennbares übersetzen)|She translates the text.|She ferries the text across the water.|She puts the text under the table.|She cancels the text.|Inseparable übersetzen means translate and keeps über with the finite verb.
""",'Interpret the meaning and separability of the prefixed verb.')

nouns=[('Sicherheit','die','-heit'),('Freiheit','die','-heit'),('Möglichkeit','die','-keit'),('Freundlichkeit','die','-keit'),('Freundschaft','die','-schaft'),('Gesellschaft','die','-schaft'),('Erlebnis','das','-nis'),('Ergebnis','das','-nis'),('Erlaubnis','die','-nis'),('Kenntnis','die','-nis'),('Eigentum','das','-tum'),('Reichtum','der','-tum'),('Lehrer','der','-er'),('Lehrerin','die','-erin'),('Fahrer','der','-er'),('Fahrerin','die','-erin'),('Entscheidung','die','-ung'),('Einladung','die','-ung'),('Bewegung','die','-ung'),('Wohnung','die','-ung')]
for noun,article,suffix in nouns:
    LESSONS.setdefault(122, []).append(question(f'Wortbildung: {noun} ({suffix}). Welcher Nominativartikel passt?',article,
        [x for x in ['der','die','das','den'] if x!=article],
        f"The noun is '{article} {noun}'. Suffixes help predict gender, but -nis and -tum in particular have lexical exceptions.",'Choose the noun’s gender in nominative singular.'))

explicit(123,"""
Das Wasser ist trinkbar. Was bedeutet trinkbar?|It can be drunk.|It contains much drink.|It has no water.|It must be thrown away.|-bar often describes a possible action: trinken → trinkbar.
Die Tasche ist waschbar.|It can be washed.|It is never washed.|It has no pockets.|It is full of water.|-bar marks the possibility of washing the item.
Das Angebot ist kostenlos.|It costs nothing.|It costs a great deal.|It has a fixed fee.|Its cost is unknown.|-los expresses absence; kostenlos means without cost.
Das Land ist waldreich.|It has many forests.|It has no forests.|It can be forested tomorrow.|It is only one forest.|-reich means rich in or containing much of something.
Die Antwort ist hilfreich.|It provides help.|It prevents all help.|It needs no answer.|It contains no information.|Hilfreich describes something that helps.
Der Text ist fehlerfrei.|It has no errors.|It has many errors.|It can only be read once.|It is about freedom.|-frei here means free of the named thing: errors.
Er ist arbeitslos.|He has no job.|He has much work.|He can work here.|He is a work supervisor.|-los indicates absence; arbeitslos means without employment.
Die Aufgabe ist lösbar.|It can be solved.|It has already been solved.|It has no solution.|It must be deleted.|-bar indicates possibility, not a completed action.
Die Stadt ist kinderfreundlich.|It is welcoming to children.|It has no children.|It contains only children.|It is unsafe for every child.|-freundlich describes an accommodating or supportive relation to the first element.
Die Region ist wasserarm.|It has little water.|It has abundant water.|It is made of water.|Its water is free.|-arm means poor in or lacking much of the named resource.
Sie arbeitet sorgfältig.|She works carefully.|She works carelessly.|She never works.|She works only at night.|Sorgfältig describes careful, attentive work; suffix meanings must be learned with the word.
Er ist rücksichtsvoll.|He is considerate.|He is inconsiderate.|He is uncertain.|He is invisible.|-voll means full of the named quality; Rücksicht is consideration.
Das Verhalten ist rücksichtslos.|It is inconsiderate.|It is considerate.|It is habitual only.|It is legally required.|-los negates the presence of consideration.
Die Nachricht ist verständlich.|It is understandable.|It is deliberately hidden.|It is not a message.|It has already been translated.|-lich can form an adjective meaning able to be understood in verständlich.
Die Lieferung ist unvollständig.|It is incomplete.|It is complete.|It is always free.|It is damaged beyond use.|Un- negates vollständig, which means complete.
Die Entscheidung ist sinnvoll.|It makes sense.|It has no purpose.|It has many separate senses only.|It is impossible to decide.|Sinnvoll means meaningful or sensible; -voll signals presence of the quality.
Der Weg ist gefahrlos.|It presents no danger.|It is very dangerous.|It has no destination.|It is forbidden.|-los marks absence of Gefahr, danger.
Die Arbeit ist mühsam.|It requires effort.|It requires no effort.|It has no result.|It is necessarily unpaid.|-sam occurs in mühsam, describing something effortful or laborious.
Der Bericht ist sachlich.|It is factual and objective.|It contains only objects.|It is deliberately fictional.|It is about a person’s clothing.|Sachlich is a lexical -lich adjective meaning factual/objective in this context.
Die Verbindung ist kabellos.|It is wireless.|It needs many cables.|It is disconnected forever.|It has a damaged cable.|-los expresses the absence of cables.
""",'Interpret the derived adjective in context.')

adverb_types={
 'manner':('Manner, usual pattern or partial extent','The -weise form describes a manner, usual pattern, grouping or partial extent, depending on the lexical item.'),
 'time':('A recurring time','The -s form or täglich denotes a repeated time rather than an adjective before a noun.'),
 'direction':('Direction','The -wärts form points in a direction.'),
 'duration':('Duration','The -lang form describes how long an activity lasts.'),
}
meanings(124,"""
Normalerweise fährt sie mit dem Bus. (normalerweise)|manner
Er arbeitet vormittags. (vormittags)|time
Sie geht rückwärts. (rückwärts)|direction
Wir warten stundenlang. (stundenlang)|duration
Teilweise ist die Straße gesperrt. (teilweise)|manner
Er lernt abends. (abends)|time
Die Reise führt südwärts. (südwärts)|direction
Es regnet tagelang. (tagelang)|duration
Wir arbeiten schrittweise weiter. (schrittweise)|manner
Sie kommt dienstags. (dienstags)|time
Er schaut aufwärts. (aufwärts)|direction
Sie war wochenlang krank. (wochenlang)|duration
Ausnahmsweise bleibt er zu Hause. (ausnahmsweise)|manner
Wir treffen uns sonntags. (sonntags)|time
Es geht abwärts. (abwärts)|direction
Die Reparatur dauerte monatelang. (monatelang)|duration
Das ist gewissermaßen eine Einladung. (gewissermaßen)|manner
Sie übt täglich. (täglich)|time
Er geht vorwärts. (vorwärts)|direction
Er arbeitete jahrelang dort. (jahrelang)|duration
""",adverb_types,'Which type of information does the specified adverb supply?')

abbreviations=[('z. B.','zum Beispiel'),('d. h.','das heißt'),('bzw.','beziehungsweise'),('usw.','und so weiter'),('u. a.','unter anderem'),('ca.','circa'),('ggf.','gegebenenfalls'),('inkl.','inklusive'),('zzgl.','zuzüglich'),('Nr.','Nummer'),('Str.','Straße'),('Tel.','Telefon'),('PLZ','Postleitzahl'),('Pkw','Personenkraftwagen'),('Lkw','Lastkraftwagen'),('EU','Europäische Union'),('EG','Erdgeschoss'),('OG','Obergeschoss'),('Info','Information'),('Uni','Universität')]
for abbreviation,expanded in abbreviations:
    LESSONS.setdefault(125, []).append(question(f'Was bedeutet „{abbreviation}“ in einer passenden Alltagsanzeige?',expanded,
        [v for a,v in abbreviations if v!=expanded][:3],
        f"'{abbreviation}' is a common abbreviation or shortened word for '{expanded}'; context still matters for abbreviations with several meanings.",'Expand the abbreviation.'))

gaps(126,'Lesen|lesen|Ausfüllen|ausfüllen|Neues|neues|Gute|gute|Angestellte|angestellte|Sie|sie|Ihnen|ihnen|Ihre|ihre',"""
Das ___ macht mir Spaß. (lesen als Nomen)|Lesen
Ich möchte das Buch ___. (Verb)|lesen
Beim ___ brauche ich Hilfe. (ausfüllen als Nomen)|Ausfüllen
Sie muss das Formular ___. (Verb)|ausfüllen
Ich habe etwas ___ gelernt. (neu)|Neues
Das ___ an dem Plan ist die Zeitersparnis. (gut als Nomen)|Gute
Die ___ hilft dem Kunden. (Person; angestellt)|Angestellte
Die ___ Mitarbeiterin hilft. (Adjektiv)|angestellte
Sehr geehrte Frau Roth, haben ___ Zeit? (formelle Anrede)|Sie
Sehr geehrter Herr Braun, ich danke ___.|Ihnen
Sehr geehrte Frau Roth, vielen Dank für ___ Hilfe. (Ihr)|Ihre
Die Kinder kommen; ___ warten draußen. (3. Person Plural)|sie
Die Gäste helfen; ich danke ___. (3. Person Plural)|ihnen
Anna hat angerufen; ___ kommt morgen. (3. Person)|sie
Das ___ der Hinweise ist wichtig. (lesen als Nomen)|Lesen
Wir sollen die Hinweise ___. (Verb)|lesen
Nach dem ___ schicken Sie das Formular ab. (ausfüllen als Nomen)|Ausfüllen
Er hat nichts ___ berichtet. (neu)|Neues
Sehr geehrte Frau Klein, ich rufe ___ morgen an. (Anrede, Akkusativ)|Sie
Die Nachbarn sind nett; ___ Wohnung ist oben. (ihr, 3. Person)|ihre
""", "'{answer}' follows capitalization for nominalized forms or formal address; ordinary verbs, attributive adjectives and third-person pronouns stay lowercase inside a sentence.")

comma_sentences=[
 'Ich weiß, dass du Zeit hast.','Wenn es regnet, bleiben wir hier.',
 'Das ist der Mann, der hier wohnt.','Ich komme, weil ich helfen möchte.',
 'Sie fragt, ob der Kurs stattfindet.','Ich weiß nicht, wann der Zug fährt.',
 'Wir lernen, um die Prüfung zu bestehen.','Er ging, ohne sich zu verabschieden.',
 'Sie bleibt, statt nach Hause zu gehen.','Er hat die Absicht, früher zu kommen.',
 'Die Möglichkeit, hier zu arbeiten, freut mich.','Das Buch, das ich lese, ist spannend.',
 'Nachdem sie gegessen hatte, ging sie hinaus.','Ich warte, bis du fertig bist.',
 'Obwohl es kalt ist, öffnet er das Fenster.','Sobald er anruft, sage ich Bescheid.',
 'Sie hofft, dass wir kommen, und wartet.','Der Kollege, dem ich helfe, ist neu.',
 'Es freut mich, dass du hier bist.','Er denkt daran, den Antrag abzugeben.',
]
for correct in comma_sentences:
    wrong=[correct.replace(',','',1),correct.replace(',',',,',1),correct.replace(',',';',1)]
    LESSONS.setdefault(127, []).append(question('Setze die Kommas: '+correct.replace(',',''),correct,wrong,
        'The comma separates a subordinate/relative clause or a clause-like zu-infinitive group. A parenthetical relative/infinitive clause needs both comma boundaries.','Choose the correctly punctuated version.'))

spellings=[
 ('Zwei-Zimmer-Wohnung','Zwei Zimmer Wohnung','Zwei-Zimmer Wohnung','Zwei Zimmer-Wohnung'),
 ('Drei-Zimmer-Wohnung','Drei Zimmer Wohnung','Drei-Zimmer Wohnung','Drei Zimmer-Wohnung'),
 ('Ein-Zimmer-Apartment','Ein Zimmer Apartment','Ein-Zimmer Apartment','Ein Zimmer-Apartment'),
 ('5-Euro-Schein','5 Euro Schein','5-Euro Schein','5 Euro-Schein'),
 ('10-Euro-Schein','10 Euro Schein','10-Euro Schein','10 Euro-Schein'),
 ('E-Mail-Adresse','E Mail Adresse','E-Mail Adresse','E Mail-Adresse'),
 ('2-Liter-Flasche','2 Liter Flasche','2-Liter Flasche','2 Liter-Flasche'),
 ('3-Tage-Reise','3 Tage Reise','3-Tage Reise','3 Tage-Reise'),
 ('40-Stunden-Woche','40 Stunden Woche','40-Stunden Woche','40 Stunden-Woche'),
 ('U-Bahn-Station','U Bahn Station','U-Bahn Station','U Bahn-Station'),
 ('Hin- und Rückfahrt','Hin und Rückfahrt','Hin- und -Rückfahrt','Hin und Rück-fahrt'),
 ('Kinder- und Jugendbücher','Kinder und Jugendbücher','Kinder- und -Jugendbücher','Kinder und Jugend-bücher'),
 ('Ein- und Ausgang','Ein und Ausgang','Ein- und -Ausgang','Ein und Aus-gang'),
 ('Vor- und Nachname','Vor und Nachname','Vor- und -Nachname','Vor und Nach-name'),
 ('An- und Abreise','An und Abreise','An- und -Abreise','An und Ab-reise'),
 ('Haustürschlüssel','Haus Türschlüssel','Haustür Schlüssel','Haus Tür Schlüssel'),
 ('Sprachkursangebot','Sprach Kursangebot','Sprachkurs Angebot','Sprach Kurs Angebot'),
 ('Bewerbungsgespräch','Bewerbung Gespräch','Bewerbungs Gespräch','Be Werbungsgespräch'),
 ('Arbeitszeitregelung','Arbeit Zeitregelung','Arbeitszeit Regelung','Arbeits Zeit Regelung'),
 ('Fahrkartenautomat','Fahr Kartenautomat','Fahrkarten Automat','Fahr Karten Automat'),
]
for correct,a,b,c in spellings:
    LESSONS.setdefault(128, []).append(question(f'Bilde ein korrekt geschriebenes zusammengesetztes Nomen: {a}',correct,[a,b,c],
        'Noun compounds are written together; digit compounds take linking hyphens, and a suspended compound part keeps an Ergänzungsstrich.','Choose the correct compound spelling.'))
