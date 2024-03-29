# Oefeningen

Onderstaande vragen zijn goede verdere oefeningen voor toetsje en tentamen. Om ze te beantwoorden heb je parate kennis nodig van reguliere expressies. Als je merkt dat je deze kennis nog niet echt hebt, dan kun je extra studeren met hulp van het materiaal in de module.

Onderstaande vragen zijn *grotendeels* representatief voor de vragen die je op het tentamen tegen zou kunnen komen. De vraagstelling kan wat anders zijn maar je zult sowieso `grep`-commando's op basis van reguliere expressies moeten schrijven.

## Parate kennis

Wat je zeker moet weten voor het tentamen:

- Verschil tussen selecteren van regels (ook wel zinnen), tekst (ook wel strings), of losse woorden.
- Hoe je dingen aan begin/eind regel kunt selecteren.
- Hoe je woorden met iets ervoor of erachter kunt selecteren.
- Betekenis van speciale tekens zoals `()|[]^$` enz.
- Alle andere dingen die je nodig had om de regex-opdrachten te doen.

## Opgaven

Gegeven is de volgende ChatGPT-poëzie:

    0 Winter, een tijd van stilte en verdriet,
    1 Met sneeuw bedekte bomen, als een doodskleed geweven.
    2 De koude wind die blaast door de straten,
    3 Een bevroren wereld, verstild en verlaten.
    4 De zon verdwijnt vroeg achter de horizon,
    5 De nacht wordt langer, het daglicht verdwijnt.
    6 In deze stille tijd, wordt het hart geroerd,
    7 Door de herinneringen aan de zomer, voorbij en verloren.
    8 Maar de winter heeft ook schoonheid,
    9 In de besneeuwde bossen en de heldere nachten.

Geef hieronder UNIX-onliners gebaseerd op `grep`. Een voorbeeld kan zijn `grep -E -o "zon"`.

1. Geef een commando om alle regels te selecteren waarin de string "sneeuw" staat, onafhankelijk van hoofdlettergebruik. De uitvoer bestaat uit regels 0 en 9.

2. Geef een commando om alle regels te selecteren waarin het woord "de" staat, onafhankelijk van hoofdlettergebruik. Het woord "deze" mag niet gematcht worden. De uitvoer bestaat daarom uit regels 2, 4, 5, 7, 8, 9 maar niet regel 6.

3. Geef een commando om alle woorden te selecteren die eindigen op een komma. De uitvoer begint met:

        Winter,
        verdriet,
        bomen,

4. Geef een commando om alle woorden te selecteren die aan het begin van de regel staan (de regelnummers horen niet tot het bestand, dus die mag je negeren!). De uitvoer begint met:

        Winter
        Met
        De

5. Geef een commando om alle woorden te selecteren die beginnen met een letter "v", daarna een klinker (a, e, i, o, u, y). De rest van het woord maakt niet uit. De uitvoer begint met:

        van
        verdriet
        verstild
