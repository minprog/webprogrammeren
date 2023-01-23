# JSON-formaat

JSON is een formaat om hierarchische structuren uit te drukken in simpele tekst. Je kunt het in de praktijk gebruiken om data uit te wisselen. Sommige websites bieden dan ook de mogelijkheid om data op te vragen in JSON-formaat.

## Hiërarchie

De basis van JSON is dat je twee soorten structuren hebt die weer andere structuren kunnen bevatten. Dit zijn *objecten* en *arrays*. Het feit dat structuren andere structuren bevatten maakt dat je hierarchiën kunt beschrijven in JSON.

Zo kun je een rijtje van objecten vatten in een array (denk aan een lijst van medewerkers). En je kunt een object "eigenschappen" meegeven waarin je weer andere waarden stopt (denk aan een persoon die een naam heeft en een huisnummer).

Hieronder een *array* met daarin twee *objects*. Elk object heeft daarin twee attributes, `name` en `address`. De waarde van `address` is ook weer een object, met daarin twee attributes, `street` en `number`.

Naast arrays en objects zijn er nog slechts twee soorten informatie in JSON (types), namelijk *numbers* en *strings*. In het voorbeeld hieronder zijn `name` en `street` allebei strings, en `number` is een... number.

    [
        {
            "name": "Ford Prefect",
            "address": {
                "street": "Science Park",
                "number": 900
            }
        },
        {
            "name": "Arthur Dent",
            "address": {
                "street": "Science Park",
                "number": 900
            }
        }
    ]

## Syntax

Dit alles wordt gevat in een zeer eenvoudige syntax. Er is een [formele specificatie](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf) van deze JSON-syntax. De paragrafen 4 t/m 9 zijn de complete specificatie van de taal. Men gebruikt zogenaamde "railroad diagrams" om uit te leggen waar JSON aan moet voldoen. Zorg dat je [deze korte handleiding](https://www.ibm.com/docs/en/integration-bus/10.0?topic=diagrams-how-read-railroad) van railroad diagrams doorneemt en dan heel precies begrijpt wat een **valide** JSON-document is.

Een opmerking die wordt gemaakt in de specificatie is dat JSON weliswaar een **syntax** definieert maar dat de bijbehorende **semantiek** (betekenis van de inhoud) niet vastligt. Elke gebruiker van JSON moet afspraken maken of vastleggen over welke data precies gecommuniceerd wordt en wat je er mee kunt. Als je verwacht dat er een lijst van medewerkers wordt verstuurd dan zal de JSON wel een array zijn met daarin objecten. Als je informatie over één persoon opvraagt dan zal de JSON wel een object zijn.

Filmpjes om JSON beter te begrijpen:

- [Web Dev Simplified: Learn JSON in 10 minutes](https://www.youtube.com/watch?v=iiADhChRriM)
- [ByteScout: JSON Specification](https://www.youtube.com/watch?v=Xi1B0EbSgTY)

## jq

Met de tool `jq` kun je data uit JSON-bestanden extraheren. Er is een speciale syntax voor het schrijven van kleine "queries" die aangeven welke data je wil hebben. Bestudeer goed de volgende pagina: <https://www.baeldung.com/linux/jq-command-json>

Filmpjes om JQ beter te begrijpen:

- [Szymon Stepniak: JSON on the command line](https://www.youtube.com/watch?v=FSn_38gDvzM)

## Movie data

Via [deze link](https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json) kun je een bestand downloaden met alle filminformatie die iemand van Wikipedia heeft gehaald. Bestudeer de structuur.

## Opdrachten

1.  Geef een complete UNIX one-liner om alleen de gegevens van de eerste film uit het bestand te laten zien.

    <textarea name="form[q1]" rows="8" required></textarea>

2.  Geef een complete UNIX one-liner om alleen de titel van de eerste film uit het bestand te laten zien.

    <textarea name="form[q2]" rows="8" required></textarea>

3.  Geef een complete UNIX one-liner om de titels van alle films uit het bestand te laten zien.

    <textarea name="form[q3]" rows="8" required></textarea>

## Conclusie

Het is niet zo makkelijk met JSON en het commando `jq` om echt interessante queries te doen in de informatie. JSON is geen database, het is een *dataformaat*. En `jq` is vooral bedoeld om fragementen van de informatie te filteren. Wil je de informatie intern relateren en daar interessante statistieken of nieuwe informatie uithalen, dan is een database een betere tool. Je kunt dan bijvoorbeeld de JSON-data in een database importeren.
