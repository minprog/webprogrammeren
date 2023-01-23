# Curl

Gebruik `curl` om de HTML van een webpagina op te vragen. Zo kun je bijvoorbeeld de HTML van zoekmachine DuckDuckGo krijgen:

    curl -L duckduckgo.com

Dit commando stuurt een verzoek naar de server http://duckduckgo.com, dus via het HTTP-protocol. Nu worden tegenwoordig bijna alle websites bij voorkeur via HTTPS gebruikt. Daarom stuurt de server als antwoord dat de pagina te vinden is op https://duckduckgo.com/ en dat het verzoek dáárheen gestuurd moet worden.

De optie `-L` zorgt ervoor dat in zo'n geval meteen de juiste pagina wordt opgevraagd (zolang de server maar zegt welke het moet zijn).

## JSON via Curl

In de volgende module gaan we aan de slag met HTML maar nu gaan we eerst JSON-data opvragen via `curl`. Vraag eens de locatie van het International Space Station op:

    curl -s https://api.wheretheiss.at/v1/satellites/25544

Je ziet dan meteen dat je JSON als antwoord krijgt in plaats van HTML. We gebruiken de flag `-s` voor `curl` om te zorgen dat deze geen "progress bar" geeft bij het binnenhalen van de data.

    {"name":"iss","id":25544,"latitude":-24.135574363392,"longitude":-111.86401960141,"altitude":425.37210858971,"velocity":27557.51464498,"visibility":"eclipsed","footprint":4534.693976796,"timestamp":1659509744,"daynum":2459794.7887037,"solar_lat":17.482788938462,"solar_lon":77.627649838076,"units":"kilometers"}

Om de JSON een beetje leesbaar te krijgen kun je deze **doorsturen** van `curl` naar `jq`:

    curl -s https://api.wheretheiss.at/v1/satellites/25544 | jq '.'

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

## Rate limit

Let op dat veel API's een **rate limit** hebben. Dat betekent dat je niet al te vaak een verzoek mag sturen (vanaf hetzelfde IP-adres), om misbruik te voorkomen. Zelfs als je met de hand, vanaf de terminal, aan het experimenteren bent kan dit gebeuren. Als je echt veel gaat experimenteren kun je de JSON ook even opslaan op je eigen computer:

    curl -s https://api.wheretheiss.at/v1/satellites/25544 > iss.json

Dan kun je `jq` zo gebruiken:

    cat iss.json | jq '.'

Zorg dat je voor de opdrachten hieronder wel gewoon het complete commando inclusief `curl` en de juiste URL van de API gebruikt.

## Oefeningen

1.  Neem de wheretheiss API en geef een commando om alleen de latitude én longitude uit te printen. Het resultaat zou er zo uit moeten zien (met andere getallen natuurlijk!):

        -41.536613527854
        -90.033171572304

    <textarea name="form[q1]" rows="4" required></textarea>

2.  Gegeven is de API op <https://nationalize.io>. Geef een complete UNIX one-liner om de landcode van het land te geven waar jouw naam (volgens de statistieken) het meest gebruikt wordt. Het is mogelijk dat de dataset niet compleet of up-to-date is dus je kunt ook een andere naam gebruiken.

    Tip: je hebt waarschijnlijk een vraagteken nodig (`?`) in de URL. Zorg dat je in dat geval de URL netjes tussen aanhalingstekens zet (`"`).

    <textarea name="form[q2]" rows="4" required></textarea>

3.  Gegeven is de API op <http://official-joke-api.appspot.com>. Geef een complete UNIX one-liner om de twee delen van een random grap te printen. De output moet zonder aanhalingstekens (`"`) zijn; daarvoor kun je de flag `-r` gebruiken voor `jq`.

    <textarea name="form[q3]" rows="4" required></textarea>

4.  Gegeven is de API op <https://randomuser.me/>. Geef een complete UNIX one-liner die de postcode van een random user print.

    <textarea name="form[q4]" rows="4" required></textarea>

5.  Gegeven is de API op <http://universities.hipolabs.com/search?country=Netherlands> (geen documentatie). Geef een complete UNIX one-liner die namen van alle universiteiten print (zonder aanhalingstekens).

    <textarea name="form[q5]" rows="4" required></textarea>

## Conclusie

JSON wordt veel gebruikt om informatie tussen websites te communiceren, omdat het zo simpel is en makkelijk om te genereren in bijna elke programmeertaal. Daarnaast worden API's zoals hierboven heel vaak als input gebruikt voor onderzoek of gewoon om andere websites mee te maken (en te vullen). Een [befaamde API is die van het Rijksmuseum](https://data.rijksmuseum.nl/object-metadata/api/), waar je ongeveer alle informatie over alle kunstwerken kunt krijgen en hergebruiken. Voor die API moet je wel een account maken, zodat ze jouw hoeveelheid "requests" kunnen beperken.
