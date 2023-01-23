# Scraping

Lees de [README](https://github.com/EricChiang/pup) van de tool `pup`. Met deze tool kun je informatie scrapen uit HTML-pagina's.

HTML is weliswaar goed gestructureerd maar primair bedoeld om in een visuele vorm omgezet te worden in een "web browser". Ook is HTML niet altijd zo gestructureerd dat de interessante data er makkelijk uit te halen is.

Daarom is het fenomeen "scraping" bedacht, waar het doel is om interessante data toch te verkrijgen. Eén typisch voorbeeld is het scrapen van prijsinformatie van een verkoopwebsite, zodat deze kan weergegeven op een website die informatie van allerlei verkopers bij elkaar wil plaatsen. Winkels willen hun data enerzijds liever niet afstaan, maar tegelijk willen ze hun prijzen wel publiceren voor consumenten. Daarom is zulke informatie vaak wel te scrapen.

Je kunt scraping ook gebruiken voor bijvoorbeeld dataverzameling voor onderzoek. Als je wil onderzoeken hoe informatie wordt geformuleerd op een bepaalde website, of je hebt informatie nodig van, bijvoorbeeld, alle medewerkers van de UvA, dan kun je daar scraping voor inzetten.

Om Pup uit te testen met websites kun je `curl` gebruiken voor het binnenhalen van de pagina en het resultaat via een pipe doorsturen naar pup. Als voorbeeld kun je op deze pagina de pagina van het KNMI binnen halen en "netjes" uitprinten:

    curl -s 'https://www.knmi.nl/home' | pup -c

Met de optie `-c` voor `pup` zorgen we ervoor dat de output in kleur wordt weergegeven. Die kun je eventueel ook weglaten.

## Opdrachten

Upload je antwoorden in een PDF met naam, studentnummer, vermelding van de vragen en de antwoorden.

Geef steeds de complete one-liner inclusief het gebruikte `curl`-commando, pipes en andere commando's.

1.  Zoek uit hoe je alle `span`s met de class `green` kunt scrapen van de pagina <https://www.pythonscraping.com/pages/warandpeace.html>.

1.  Zoek uit hoe je <u>alleen de tekst</u> van bovenstaande `span`s kunt scrapen.

1.  Zoek uit met welk commando (curl + pup) je alle URL's (links) naar het laatste nieuws van de NOS kunt scrapen. Gebruik hiervoor de pagina <https://nos.nl/nieuws>.

1.  Zoek uit hoe je alle headlines kunt scrapen, dus de koppen van het nieuws.

1.  Zoek uit hoe je een korte omschrijving van het weer kunt printen vanuit de website van het KNMI.

1.  Zoek uit hoe je alle `tr` elementen uit de tabel op <https://pythonscraping.com/pages/page3.html> kunt scrapen, maar met uitzondering van het eerste `tr`-element (deze bevat de tabelkopjes en die hebben we niet nodig). In de README van Pup staan de selectors die je kunt gebruiken. Volg de link naar MDN om uit te zoeken hoe ze werken.

1.  Extra opdracht (optioneel): zoek uit hoe je een JSON kunt genereren met daarin voor elke nieuwslink een object met een link-tekst:

        {
          "href": "/artikel/2441789-vogelspin-ontsnapt-op-kinderdagverblijf-velp",
          "text": "Vogelspin ontsnapt op kinderdagverblijf Velp"
        }

    Omdat je alle nieuwslinks wil hebben is het JSON-document uiteindelijk een JSON-array, dus dat begint met `[` en eindigt met `]`.
