# Curl

Gebruik `curl` om de HTML van een webpagina op te vragen. Zo kun je bijvoorbeeld de HTML van zoekmachine DuckDuckGo krijgen:

    curl -L duckduckgo.com

Dit commando stuurt een verzoek naar de server http://duckduckgo.com, dus via het HTTP-protocol. Nu worden tegenwoordig bijna alle websites bij voorkeur via HTTPS gebruikt. Daarom stuurt de server als antwoord dat de pagina te vinden is op https://duckduckgo.com/ en dat het verzoek dáárheen gestuurd moet worden.

De optie `-L` zorgt ervoor dat in zo'n geval meteen de juiste pagina wordt opgevraagd (zolang de server maar zegt welke het moet zijn).

## JSON via Curl

In de volgende module gaan we aan de slag met HTML maar nu gaan we eerst JSON-data opvragen via `curl`. Vraag eens de locatie van het International Space Station op:

    curl https://api.wheretheiss.at/v1/satellites/25544

Je ziet dan meteen dat je JSON als antwoord krijgt in plaats van HTML.

    {"name":"iss","id":25544,"latitude":-24.135574363392,"longitude":-111.86401960141,"altitude":425.37210858971,"velocity":27557.51464498,"visibility":"eclipsed","footprint":4534.693976796,"timestamp":1659509744,"daynum":2459794.7887037,"solar_lat":17.482788938462,"solar_lon":77.627649838076,"units":"kilometers"}

Om de JSON een beetje leesbaar te krijgen kun je deze **doorsturen** van `curl` naar `jq`:

    curl https://api.wheretheiss.at/v1/satellites/25544 | jq '.'

Dan wordt de JSON zo op het scherm geprint:

    {
      "name": "iss",
      "id": 25544,
      "latitude": -28.483617342432,
      "longitude": -107.62821176958,
      "altitude": 427.23022766961,
      "velocity": 27552.819683785,
      "visibility": "eclipsed",
      "footprint": 4544.0662041756,
      "timestamp": 1659509837,
      "daynum": 2459794.7897801,
      "solar_lat": 17.482507366243,
      "solar_lon": 77.240127963861,
      "units": "kilometers"
    }

Let op dat veel API's een **rate limit** hebben. Dat betekent dat je niet al te vaak een verzoek mag sturen (vanaf hetzelfde IP-adres), om misbruik te voorkomen. Zelfs als je met de hand, vanaf de terminal, aan het experimenteren bent kan dit gebeuren. Als je echt veel gaat experimenteren kun je de JSON ook even opslaan op je eigen computer:

    curl https://api.wheretheiss.at/v1/satellites/25544 > iss.json

Dan kun je `jq` zo gebruiken:

    cat iss.json | jq '.'

🌵 Oefening

1.  Geef een commando om alleen de latitude én longitude uit te printen. Het resultaat zou er zo uit moeten zien (met andere getallen natuurlijk!):

        -41.536613527854
        -90.033171572304

    <textarea name="form[q1]" rows="4" required></textarea>

1.  Geef een commando om op basis van de timestamp uit de JSON de datum netjes uit te printen. Het zou er zo uit moeten zien:

        Wed Aug  3 09:02:30 CEST 2022

    De timestamp is het aantal seconden sinds 1 januari 1970. Dit wordt ook wel een "epoch" tijd genoemd. Er zijn verschillende manieren om zo'n getal te converteren naar een datum. Gebruik een zoekmachine om te achterhalen hoe dit moet.
    
    Het kan handig zijn om hier ook "command substitution" te gebruiken. Dit is een constructie die je in plaats van pipes of in samenwerking met pipes kan gebruiken. Zie [Command Substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html). Je mag zo'n command substitution gebruiken als parameter van een ander commando.

    Documenteer in je antwoord exact welke bronnen je hebt geprobeerd en hoe je ze hebt toegepast. Dus gebruikte zoektermen, een referentie naar een website met een techniek die niet werkte, hoe je het wél werkend hebt gekregen, dat soort dingen.

    **Besteed niet meer dan 1 uur aan dit probleem.** Als je er niet uitkomt dan is dat geen probleem, als je je zoektocht maar documenteert. Als je niet weet hoe te beginnen: vraag een assistent of stuur een mail.

    <textarea name="form[q2]" rows="12" required></textarea>
