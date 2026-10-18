from .core import gaps, meanings, explicit, clauses, LESSONS, question

relations={
 'result':('An actual consequence','Sodass/so … dass links an outcome to the preceding situation; it does not merely state a purpose.'),
 'purpose':('An intended purpose','Damit/um … zu names the goal of an action without asserting that the goal was achieved.'),
 'reason':('A reason','Weil/da provides a reason for the main event, not its resulting consequence.'),
 'contrast':('An outcome contrary to expectation','Obwohl/trotzdem marks a result that conflicts with the expectation raised by the other fact.'),
}
meanings(145,"""
Es war so laut, dass ich nichts verstand.|result
Ich spreche laut, damit du mich hörst.|purpose
Ich blieb zu Hause, weil ich krank war.|reason
Obwohl ich krank war, ging ich arbeiten.|contrast
Der Bus fiel aus, sodass wir zu spät kamen.|result
Sie spart, um ein Fahrrad zu kaufen.|purpose
Da die Straße gesperrt war, fuhren wir anders.|reason
Es regnete. Trotzdem gingen wir hinaus.|contrast
Er war so müde, dass er sofort einschlief.|result
Die Tasche war so schwer, dass der Griff riss.|result
Das Gerät war kaputt, sodass wir nicht arbeiten konnten.|result
Ich schicke die Adresse, damit du uns findest.|purpose
Sie ruft an, weil sie eine Frage hat.|reason
Obwohl es teuer war, kaufte er das Rad.|contrast
Es war so kalt, dass der See zufror.|result
Sie hatte gut gelernt, sodass sie alles wusste.|result
Die Treppe war so glatt, dass er ausrutschte.|result
Der Laden war geschlossen, sodass wir nichts kaufen konnten.|result
Die Erklärung war so klar, dass alle sie verstanden.|result
Er verpasste den Bus, sodass er zu Fuß gehen musste.|result
""",relations,'Is the clause a consequence, purpose, reason or concession?')

method_labels={
 'method':('The means by which the main action is achieved','Indem presents an action as the method or means for achieving the main result.'),
 'time':('A simultaneous event only','Temporal während in this context only states what happens at the same time.'),
 'reason':('A reason rather than a method','Weil supplies the reason for the action, not the means used to carry it out.'),
 'purpose':('An intended goal rather than a method','Damit identifies the desired result; it does not specify the means used to achieve it.'),
}
meanings(146,"""
Man spart Energie, indem man die Heizung niedriger einstellt.|method
Sie verbessert ihr Deutsch, indem sie täglich liest.|method
Wir sparen Geld, indem wir selbst kochen.|method
Er öffnet die Tür, indem er den Knopf drückt.|method
Ich lerne Wörter, indem ich sie in Sätzen benutze.|method
Sie kocht, während ich gerade den Tisch decke. (gleichzeitig)|time
Er bleibt zu Hause, weil er krank ist.|reason
Ich rufe an, damit du Bescheid weißt.|purpose
Sie bezahlt, indem sie ihre Karte benutzt.|method
Wir finden den Weg, indem wir der Karte folgen.|method
Er liest, während ich um zehn telefoniere. (gleichzeitig)|time
Wir warten, weil der Zug spät kommt.|reason
Sie schreibt alles auf, damit sie nichts vergisst.|purpose
Er übt Aussprache, indem er laut nachspricht.|method
Sie erreicht die Schule, indem sie die Brücke überquert.|method
Ich ruhe mich aus, während der Zug fährt. (gleichzeitig)|time
Sie lernt, weil sie eine Prüfung hat.|reason
Wir reservieren, damit wir einen Platz haben.|purpose
Er löst das Problem, indem er das Gerät neu startet.|method
Wir vermeiden Fehler, indem wir den Text prüfen.|method
""",method_labels,'Which relation does the subordinate clause express?')

proportions=[
 ('früher wir buchen','günstiger wird die Reise','Earlier booking accompanies a lower price.'),
 ('mehr ich übe','sicherer werde ich','More practice accompanies greater confidence.'),
 ('länger wir warten','ungeduldiger werden die Gäste','Longer waiting accompanies increasing impatience.'),
 ('schneller du fährst','höher ist der Verbrauch','Greater speed accompanies higher consumption.'),
 ('weniger wir heizen','niedriger sind die Kosten','Less heating accompanies lower costs.'),
 ('öfter sie liest','mehr Wörter kennt sie','More frequent reading accompanies knowing more words.'),
 ('älter er wird','ruhiger wird er','Increasing age accompanies becoming calmer.'),
 ('größer die Wohnung ist','höher ist die Miete','A larger apartment accompanies a higher rent.'),
 ('genauer du prüfst','weniger Fehler bleiben','More careful checking accompanies fewer remaining errors.'),
 ('näher wir kommen','deutlicher sehen wir das Haus','Getting closer accompanies a clearer view of the house.'),
]
for first,second,meaning in proportions:
    sentence=f'Je {first}, desto {second}.'
    LESSONS.setdefault(147, []).append(question(f'Je {first}, ___ {second}.','desto',['obwohl','weil','damit'],
        'Je introduces a verb-final comparative clause; desto/umso introduces the correlated comparative in a main-clause pattern.','Complete the proportional construction using one of the offered connectors.'))
    LESSONS[147].append(question(sentence,meaning,
        ['The two quantities are explicitly unrelated.','The sentence specifies a single past event only.','The sentence states that both quantities stay constant.'],
        'The comparative in each half links a change in the first situation with the stated change in the second.','Interpret how the two changes are linked.'))

comparisons=[('er','alles','wüsste'),('sie','hier','wohnte'),('er','sehr reich','wäre'),('sie','keine Zeit','hätte'),('er','uns nicht','kennte'),('sie','nichts','hörte'),('er','schon fertig','wäre'),('sie','die Antwort','wüsste'),('er','alles bezahlen','könnte'),('sie','uns helfen','wollte')]
for index,(subj,middle,verb) in enumerate(comparisons):
    correct=f'als ob {subj} {middle} {verb}'
    full=f'{subj.capitalize()} tut so, {correct}.'
    LESSONS.setdefault(148, []).append(question(f'{subj.capitalize()} tut so, ___.',correct,
        [f'als ob {subj} {verb} {middle}',f'als ob {verb} {subj} {middle}',f'ob als {subj} {middle} {verb}'],
        'Als ob introduces an unreal comparison with final verb order; the Konjunktiv form describes an appearance, not an established fact.','Choose the ordered unreal comparison.'))
    interpretation=full if index<5 else f'{subj.capitalize()} tut so, als {verb} {subj} {middle}.'
    LESSONS[148].append(question(interpretation,'The person gives this impression; its truth is not asserted.',
        ['The speaker guarantees that the appearance is true.','The sentence asks a genuine yes/no question.','The sentence reports a mandatory instruction.'],
        'Als ob, or shortened als with the verb immediately after als, makes an unreal appearance comparison. It does not prove the described state or ability.','Interpret the truth status of the comparison.'))

while_labels={
 'contrast':('A contrast between general preferences or situations','While these general statements are set against each other, their simultaneous occurrence is not the point.'),
 'time':('Two events occurring at the same time','The explicit shared moment makes während temporal: the two actions overlap.'),
 'cause':('A causal explanation','A causal relation gives the reason for an event rather than contrast or simultaneity.'),
 'purpose':('An intended outcome','A purpose relation describes an intended goal rather than an opposition or overlapping event.'),
}
meanings(149,"""
Während ich lieber lese, hört sie lieber Musik. (allgemeine Vorlieben)|contrast
Während ich gerade lese, kocht sie gleichzeitig.|time
Während der Norden meist kühl ist, ist der Süden meist warm. (allgemeiner Gegensatz)|contrast
Während wir um zehn essen, klingelt das Telefon.|time
Während Paul Autos mag, bevorzugt Anna Fahrräder. (Vorlieben)|contrast
Während sie gerade spricht, mache ich Notizen.|time
Während diese Wohnung teuer ist, ist die andere günstig. (Preisvergleich)|contrast
Während er jetzt duscht, decke ich den Tisch.|time
Während ich Kaffee bevorzuge, trinkt sie lieber Tee. (Vorlieben)|contrast
Während wir gerade warten, fällt Schnee.|time
Während er gern früh arbeitet, arbeitet sie lieber spät. (Gewohnheiten im Gegensatz)|contrast
Während sie jetzt lernt, spielt ihr Bruder gleichzeitig.|time
Während der eine Kurs voll ist, hat der andere noch Plätze. (Gegensatz)|contrast
Während ich gerade koche, hört sie mir zu.|time
Während Anna für den Vorschlag ist, ist Paul dagegen. (Meinungen)|contrast
Während wir um neun ankommen, fährt der Bus gerade ab.|time
Während ich kurze Reisen mag, bevorzugt sie lange Aufenthalte. (Vorlieben)|contrast
Während er gerade die Tür öffnet, klingelt sein Handy.|time
Während wir sparen möchten, will er mehr ausgeben. (gegensätzliche Ziele)|contrast
Während die Ärztin gerade untersucht, wartet die Familie draußen.|time
""",while_labels,'Is während temporal or contrastive in the stated context?')

absence=[
 ('Er ging,','jemand','es','bemerkte'),('Sie öffnete die Tür,','das Kind','davon','aufwachte'),
 ('Er nahm das Buch mit,','ich','es','wusste'),('Sie änderte den Termin,','wir','davon','erfuhren'),
 ('Er fuhr los,','die anderen','fertig','waren'),('Sie bezahlte,','jemand','sie darum','bat'),
 ('Er arbeitete weiter,','seine Kollegen','ihm','halfen'),('Sie verließ den Raum,','die Lehrerin','es','sah'),
 ('Er zog um,','seine Freunde','Bescheid','wussten'),('Sie schloss das Fenster,','ich','es','bemerkte'),
]
for prefix,subj,middle,verb in absence:
    completion=f'{subj} {middle} {verb}'
    sentence=f'{prefix} ohne dass {completion}.'
    LESSONS.setdefault(150, []).append(question(f'{prefix} ohne dass ___.',completion,
        [f'{subj} {verb} {middle}',f'{verb} {subj} {middle}',f'{subj} {middle} zu {verb}'],
        'Ohne dass introduces a finite subordinate clause with its own subject; the finite verb goes last.','Complete the full absent-circumstance clause.'))
    LESSONS[150].append(question(sentence,'The main event occurred without the subordinate circumstance happening.',
        ['The subordinate event was the intended goal.','The subordinate event caused the main event.','The subordinate event is asserted as happening first.'],
        'Ohne dass denies an accompanying circumstance; its subject can differ from the main-clause subject.','Interpret the absent accompanying circumstance.'))

alternatives=[
 ('Alle sollten zuhören,','alle','gleichzeitig','sprechen'),
 ('Wir sollten warten,','er','allein','losfährt'),
 ('Anna könnte helfen,','Paul','alles allein','macht'),
 ('Die Gruppe sollte planen,','jeder','einfach','anfängt'),
 ('Wir könnten gemeinsam kochen,','sie','allein','arbeitet'),
 ('Der Chef sollte erklären,','die Mitarbeiter','nur','raten'),
 ('Wir sollten nachfragen,','die Kinder','lange','warten'),
 ('Eine Person sollte bestellen,','alle','gleichzeitig','anrufen'),
 ('Die Lehrerin könnte helfen,','die Schüler','alles selbst suchen','müssen'),
 ('Wir könnten teilen,','einer','alles','bezahlt'),
]
for prefix,subj,middle,verb in alternatives:
    completion=f'{subj} {middle} {verb}'
    LESSONS.setdefault(151, []).append(question(f'{prefix} statt dass ___.',completion,
        [f'{subj} {verb} {middle}',f'{verb} {subj} {middle}',f'{subj} {middle} zu {verb}'],
        'Statt dass gives an alternative with its own explicit subject and a final finite verb; an infinitive alone would lose that subject.','Complete the alternative with its own subject.'))
    LESSONS[151].append(question(f'{prefix} statt dass {completion}.','The main-clause option is proposed instead of the subordinate alternative.',
        ['Both options are necessarily carried out together.','The subordinate event is the main action’s purpose.','The sentence reports two unrelated facts.'],
        'Statt dass contrasts a proposed/chosen course with the alternative it replaces; it need not share the main-clause subject.','Interpret the relation between the alternatives.'))

exception_labels={
 'exception':('An exception to an otherwise negative or limited statement','Außer dass / außer … zu specifies the one exceptional fact or action.'),
 'absence':('An accompanying event that did not happen','Ohne dass negates an accompanying circumstance rather than identifying an exception.'),
 'alternative':('An alternative that is replaced','Statt dass contrasts an unused alternative with the main option.'),
 'purpose':('An intended goal','Um … zu names a purpose, not an exception.'),
}
meanings(152,"""
Er hat nichts getan, außer eine Nachricht zu schicken.|exception
Ich weiß nichts, außer dass sie in Bonn wohnt.|exception
Sie ging, ohne dass ich es bemerkte.|absence
Wir warten, statt dass einer allein losfährt.|alternative
Er lernt, um die Prüfung zu bestehen.|purpose
Es gab keine Probleme, außer dass der Zug spät kam.|exception
Ich habe nichts vor, außer das Zimmer aufzuräumen.|exception
Er kam, ohne dass jemand ihn eingeladen hatte.|absence
Wir helfen, statt dass sie alles allein macht.|alternative
Sie ruft an, um einen Termin zu vereinbaren.|purpose
Niemand wusste etwas, außer dass das Büro zu war.|exception
Er wollte nichts, außer sich auszuruhen.|exception
Sie fuhr weg, ohne dass wir Bescheid wussten.|absence
Wir teilen die Arbeit, statt dass einer alles macht.|alternative
Ich spare, um ein Rad zu kaufen.|purpose
Ich kann nichts berichten, außer dass alle angekommen sind.|exception
Er hat nichts gemacht, außer die Rechnung zu bezahlen.|exception
Alles ist geklärt, außer dass die Unterschrift fehlt.|exception
Sie tat nichts, außer auf den Anruf zu warten.|exception
Ich weiß nur wenig, außer dass die Prüfung morgen ist.|exception
""",exception_labels,'Identify exception, absence, alternative or purpose.')

restrictions={
 'condition':('A proviso that must hold','Sofern means provided that; the main claim is conditional on the subordinate proposition.'),
 'knowledge':('A limit to the speaker’s knowledge','Soweit/soviel ich weiß limits the authority of the claim to what the speaker knows.'),
 'extent':('A limit to what is possible','Soweit possible/feasible here restricts how far the action can be carried out.'),
 'spatial':('A literal spatial extent','Soweit das Auge reicht describes a literal range of vision rather than a knowledge disclaimer.'),
}
meanings(153,"""
Das Angebot gilt, sofern noch Plätze frei sind.|condition
Soweit ich weiß, beginnt der Kurs morgen.|knowledge
Wir helfen, soweit es möglich ist.|extent
Soweit das Auge reicht, sieht man Felder.|spatial
Du kannst mitfahren, sofern du pünktlich bist.|condition
Soviel ich weiß, ist sie schon angekommen.|knowledge
Wir prüfen alles, soweit uns das möglich ist.|extent
Soweit man sehen kann, liegt Schnee.|spatial
Die Anmeldung gilt, sofern die Gebühr bezahlt ist.|condition
Soweit ich weiß, wohnt er in Köln.|knowledge
Wir unterstützen dich, soweit unsere Mittel reichen.|extent
Sie kommt, sofern sie Zeit hat.|condition
Soviel ich weiß, ist das Büro geschlossen.|knowledge
Wir ändern den Plan, soweit es nötig ist.|extent
Sie erhalten Ersatz, sofern der Schaden gemeldet wurde.|condition
Soweit ich weiß, gibt es noch Karten.|knowledge
Der Vertrag gilt, sofern beide unterschreiben.|condition
Wir kommen, sofern das Wetter es erlaubt.|condition
Soweit ich weiß, hat er schon bezahlt.|knowledge
Sie kann teilnehmen, sofern sie sich anmeldet.|condition
""",restrictions,'What kind of restriction is expressed here?')

condition_types={
 'condition':('A condition equivalent to a wenn-clause','The verb-first clause is followed by its consequence; it means if the described case occurs.'),
 'question':('A genuine direct yes/no question','Without a following consequence, and in the explicit question context, verb-first order requests information.'),
 'command':('A direct instruction','The imperative directly tells someone to act rather than setting a condition.'),
 'statement':('A direct indicative statement','This ordinary statement asserts an event; it is not a verb-first subordinate condition.'),
}
meanings(154,"""
Sollte der Kurs ausfallen, bekommen Sie eine Nachricht.|condition
Hast du Zeit, können wir reden.|condition
Kommt er heute? (echte Frage)|question
Komm bitte heute!|command
Der Kurs beginnt morgen.|statement
Regnet es, bleiben wir hier.|condition
Ist der Laden offen, kaufen wir Brot.|condition
Hast du heute Zeit? (echte Frage)|question
Ruf mich bitte an!|command
Die Gäste kommen um acht.|statement
Sollten Fragen entstehen, rufen Sie an.|condition
Brauchen Sie Hilfe, wenden Sie sich an uns.|condition
Fährt der Zug schon? (echte Frage)|question
Bitte warten Sie hier!|command
Ich habe morgen frei.|statement
Sollte es Probleme geben, helfen wir.|condition
Fehlt die Unterschrift, ist der Antrag ungültig.|condition
Ist die Tür zu? (echte Frage)|question
Bleibt Zeit übrig, machen wir eine Pause.|condition
Geht das heute? (echte Frage)|question
""",condition_types,'How does the verb-first or main-clause form function in context?')

nominal_relations={
 'cause':('A cause or resulting circumstance','Wegen/infolge names a cause. Infolge emphasizes an effect following from that cause.'),
 'concession':('A fact that would normally prevent the outcome','Trotz presents an obstacle despite which the main event still happens.'),
 'motive':('An intentional motive','Aus plus a feeling or motive can explain why someone chooses to act.'),
 'reaction':('An involuntary reaction to an intense feeling','Vor plus a feeling can describe an involuntary physical reaction, not a deliberate motive.'),
}
meanings(155,"""
Wegen des Regens fällt das Fest aus.|cause
Trotz des Regens findet das Fest statt.|concession
Aus Freundlichkeit hilft er uns.|motive
Vor Angst zittert das Kind.|reaction
Infolge des Unfalls ist die Straße gesperrt.|cause
Trotz der Kälte gehen wir spazieren.|concession
Aus Interesse besucht sie den Kurs.|motive
Vor Freude weint sie.|reaction
Wegen der Reparatur bleibt der Laden zu.|cause
Trotz des Streiks kommt er pünktlich.|concession
Aus Höflichkeit sagt er nichts.|motive
Vor Aufregung kann er nicht schlafen.|reaction
Infolge des Sturms ist das Dach beschädigt.|cause
Trotz der Schwierigkeiten bleibt sie ruhig.|concession
Aus Neugier öffnet sie die Schachtel.|motive
Vor Wut wird er rot.|reaction
Wegen des Fehlers muss er neu anfangen.|cause
Trotz der Verspätung erreichen wir den Zug.|concession
Aus Liebe hilft sie ihm.|motive
Vor Schreck lässt er das Glas fallen.|reaction
""",nominal_relations,'Which relation does the initial noun phrase express?')

gaps(156,'wo|wohin|woher|wann',"""
Wir treffen uns dort, ___ die Brücke steht. (Ort)|wo
Er fährt dorthin, ___ die Straße führt. (Ziel)|wohin
Sie kommt von dort, ___ auch ich komme. (Herkunft)|woher
Bleib dort, ___ du bist. (Ort)|wo
Geh dorthin, ___ ich zeige. (Richtung)|wohin
Er erzählt, ___ seine Familie kommt. (Herkunft)|woher
Das ist die Stelle, ___ wir warten. (Ort)|wo
Sie geht dorthin, ___ die Gäste gegangen sind. (Ziel)|wohin
Ich weiß, ___ das Geräusch kommt. (Quelle)|woher
Wir essen dort, ___ es ruhig ist. (Ort)|wo
Er läuft dorthin, ___ der Bus fährt. (Ziel)|wohin
Sie fragt, ___ der Wind kommt. (Herkunft)|woher
Wir bleiben dort, ___ wir wohnen. (Ort)|wo
Ich sehe, ___ die Reise führt. (Ziel)|wohin
Er weiß, ___ die Nachricht stammt. (Quelle)|woher
Wir sitzen dort, ___ die Sonne scheint. (Ort)|wo
Zeig mir, ___ ich die Kiste tragen soll. (Ziel)|wohin
Sie erklärt, ___ das Wasser fließt. (Herkunft)|woher
Das ist der Platz, ___ wir uns trafen. (Ort)|wo
Er fragt, ___ wir umziehen. (Ziel)|wohin
""",{'wo':'Wo identifies the place where a state or activity is located.', 'wohin':'Wohin identifies the destination or direction of movement.', 'woher':'Woher identifies the source or origin.', 'wann':'Wann would ask about time, not this spatial relation.'})

relative_reference={
 'whole':('The entire preceding proposition','Was or a wo-compound comments on the whole previous fact, rather than agreeing with a single noun.'),
 'noun':('A particular noun, using a gendered relative pronoun','A gendered relative pronoun such as der/die/das takes up the stated noun.'),
 'question':('An indirect question','The W-word embeds a question after wissen/fragen, instead of commenting on a preceding proposition.'),
 'place':('A specific location, using wo','Wo specifies a location, rather than commenting on a whole preceding fact or using a gendered relative pronoun.'),
}
meanings(157,"""
Sie kam pünktlich, worüber wir uns freuten.|whole
Er half sofort, was mich überraschte.|whole
Das ist das Buch, das ich lese.|noun
Ich weiß nicht, was er liest.|question
Wir treffen uns dort, wo die Brücke steht.|place
Der Kurs fiel aus, worüber sich alle ärgerten.|whole
Sie hat bestanden, was uns freut.|whole
Hier ist die Frau, die uns hilft.|noun
Er fragt, worüber wir sprechen.|question
Bleib dort, wo du bist.|place
Er sagte ab, womit niemand gerechnet hatte.|whole
Wir hatten frei, was selten vorkommt.|whole
Der Bus, auf den wir warten, kommt.|noun
Sie weiß nicht, womit er fährt.|question
Das ist der Ort, wo wir wohnen.|place
Sie zog um, wovon ich erst später erfuhr.|whole
Er vergaß den Termin, was uns überraschte.|whole
Die Kundin, deren Brief hier liegt, wartet.|noun
Sie hat uns geholfen, wofür wir ihr danken.|whole
Er kam zu spät, worüber sich die Leiterin ärgerte.|whole
""",relative_reference,'What does the final relative/W-clause refer to or do?')

gaps(158,'wer|wen|wem|was|der|den|dem|das',"""
___ teilnehmen möchte, muss sich anmelden. (freie Relativkonstruktion)|Wer|Wer is the subject of teilnehmen möchte and means whoever.
Das ist alles, ___ ich weiß.|was
___ ich vertraue, dem helfe ich. (vertrauen + Dativ)|Wem|Vertrauen takes dative, so the free relative begins with wem.
___ ich sehe, den grüße ich. (sehen + Akkusativ)|Wen|Sehen requires an accusative object, so use wen.
Wer Zeit hat, ___ kann helfen. (wiederaufnehmend)|der
Das ist nichts, ___ mich überrascht.|was
___ früh kommt, bekommt einen Platz.|Wer|The free relative subject is wer, referring to any person who comes early.
___ du suchst, den kenne ich. (Person; Akkusativ)|Wen|The object of suchst is accusative wen.
___ du hilfst, dem danken wir. (Dativ)|Wem|Helfen takes dative, so use wem inside the free relative.
Ich höre etwas, ___ ich nicht verstehe.|was
Wer viel lernt, ___ weiß mehr.|der
Wen ich einlade, ___ begrüße ich. (wiederaufnehmend)|den
Wem ich antworte, ___ schreibe ich. (wiederaufnehmend)|dem
___ er sagt, ist wichtig. (Sache; freier Relativsatz)|Was|Was heads a free relative about the content of what he says.
Das ist alles, ___ du brauchst.|was
___ helfen will, ist willkommen.|Wer|Wer introduces a free relative without a preceding noun antecedent.
Ich nehme, ___ noch übrig ist. (Sache)|was
Wen sie kennt, ___ fragt sie. (Akkusativ)|den
Wem sie vertraut, ___ erzählt sie alles. (Dativ)|dem
Es gibt nichts, ___ ich ändern kann.|was
""", "Each clause supplies its own case: '{answer}' matches the verb's requirement or the free-relative pattern; was is used after alles/nichts/etwas here.")
