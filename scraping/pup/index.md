# Werken met Pup

Lees de [README](https://github.com/EricChiang/pup) van de tool `pup`. Met deze tool kun je informatie "scrapen" uit HTML-pagina's. HTML-pagina's bevatten bijvoorbeeld interessante informatie zoals de prijs van een product, of beurskoersen, of het laatste bedrijfsnieuws. Door te "scrapen" filteren we deze relevante informatie uit HTML-pagina's. Deze informatie kun je laten zien in je terminal, maar je kunt dit ook gebruiken voor bijvoorbeeld dataverzameling voor onderzoek.

Scraping met `pup` gaat op basis van de selectors die ook in CSS gebruikt worden. Hiermee kun je aangeven welk deel van de HTML je wilt hebben. Op de gelinkte GitHub-pagina van `pup` staat ook een lijstje van de ondersteunde CSS-selectors in deze tool.

Als het goed is heb je `pup` al tot je beschikking omdat je het installatiescript hebt gedraaid.

Om Pup uit te testen met websites kun je `curl` gebruiken voor het binnenhalen van de pagina en het resultaat via een pipe doorsturen naar pup. Als voorbeeld kun je op deze pagina de pagina van het KNMI binnen halen en "netjes" uitprinten:

    curl -s 'https://www.knmi.nl/home' | pup -c

Met de optie `-s` voor `curl` zorgen we ervoor dat het programma geen "downloading" indicator geeft. Die is ook niet echt interessant omdat het laden van de meeste HTML-pagina's maar heel kort duurt. Met de optie `-c` voor `pup` zorgen we ervoor dat de output in kleur wordt weergegeven. Die kun je weglaten als je wilt.

## Opdrachten

Geef steeds de complete oneliner inclusief het gebruikte `curl`-commando, pipes en andere commando's.

1.  Zoek uit hoe je alle `span`s met de class `green` kunt scrapen van de pagina <https://www.pythonscraping.com/pages/warandpeace.html>.

1.  Zoek uit hoe je <u>alleen de tekst</u> van bovenstaande `span`s kunt scrapen.

1.  Zoek uit met welk commando (`curl` + `pup`) je alle URL's (links) naar het laatste nieuws van de NOS kunt scrapen. Gebruik hiervoor de pagina <https://nos.nl/nieuws/laatste>.

1.  Zoek uit hoe je alle headlines kunt scrapen, dus de koppen van het nieuws.

1.  Zoek uit hoe je een korte omschrijving van het weer kunt printen vanuit de website van het KNMI.

1.  Zoek uit hoe je alle `tr` elementen uit de tabel op <https://pythonscraping.com/pages/page3.html> kunt scrapen, maar met uitzondering van het eerste `tr`-element (deze bevat de tabelkopjes en die hebben we niet nodig). In de README van Pup staan de selectors die je kunt gebruiken. Volg de link naar MDN om uit te zoeken hoe ze werken.

1.  Extra opdracht (optioneel): zoek uit hoe je een JSON kunt genereren met daarin alle links en headlines als paren. Zo'n paar ziet er dan zo uit:

        {
          "href": "/artikel/2441789-vogelspin-ontsnapt-op-kinderdagverblijf-velp",
          "text": "Vogelspin ontsnapt op kinderdagverblijf Velp"
        }

    Omdat het een lijst van paren is verwachten we dat hele de JSON een array is, dus begint met `[` en eindigt met `]`.
