# Scraping

> Bestudeer de stof en beantwoord de vragen hieronder. Je antwoorden worden beoordeeld op uitleg en correctheid (2 punten voor de hele opdracht).

Lees de [README](https://github.com/EricChiang/pup) van de tool `pup`. Met deze tool kun je informatie scrapen uit HTML-pagina's. Zo kun je informatie van een website laten zien in je terminal, maar je kunt dit ook gebruiken voor bijvoorbeeld dataverzameling voor onderzoek.

Installatie voor Ubuntu en WSL:

    curl -LO https://github.com/ericchiang/pup/releases/download/v0.4.0/pup_v0.4.0_linux_amd64.zip
    unzip pup_v*

Dit geeft in de huidige directory een executable genaamd `pup` die je zoals normaal kunt runnen met `./pup`. Je kunt het programma dus niet runnen door alleen `pup` in te tikken. Pas dit aan in de voorbeelden hieronder! Als pup helemaal niet werkt, stuur even een mail naar <help@mprog.nl>.

Installatie voor Mac:

    brew install pup

Dit installeert een commando `pup` dat je kunt aanroepen met `pup` (anders dan op Windows dus!).

Om Pup uit te testen met websites kun je `curl` gebruiken voor het binnenhalen van de pagina en het resultaat via een pipe doorsturen naar pup. Als voorbeeld kun je op deze pagina de pagina van het KNMI binnen halen en "netjes" uitprinten:

    curl -s 'https://www.knmi.nl/home' | pup -c

Met de optie `-s` voor `curl` zorgen we ervoor dat het programma geen "loading" indicator geeft. Die is ook niet echt interessant omdat het laden van de meeste HTML-pagina's maar heel kort duurt. Met de optie `-c` voor `pup` zorgen we ervoor dat de output in kleur wordt weergegeven. Die kun je ook weglaten.

## Opdrachten

Geef steeds de complete pipeline inclusief het gebruikte `curl`-commando, pipes en andere commando's.

1.  Zoek uit hoe je alle `span`s met de class `green` kunt scrapen van de pagina <https://www.pythonscraping.com/pages/warandpeace.html>.

    <textarea name="form[q1]" rows="4" required></textarea>

1.  Zoek uit hoe je <u>alleen de tekst</u> van bovenstaande `span`s kunt scrapen.

    <textarea name="form[q2]" rows="4" required></textarea>

1.  Zoek uit met welk commando (curl + pup) je alle URL's (links) naar het laatste nieuws van de NOS kunt scrapen. Gebruik hiervoor de pagina <https://nos.nl/nieuws>.

    <textarea name="form[q3]" rows="4" required></textarea>

1.  Zoek uit hoe je alle headlines kunt scrapen, dus de koppen van het nieuws.

    <textarea name="form[q4]" rows="4" required></textarea>

1.  Zoek uit hoe je een korte omschrijving van het weer kunt printen vanuit de website van het KNMI.

    <textarea name="form[q5]" rows="4" required></textarea>

1.  Zoek uit hoe je alle `tr` elementen uit de tabel op <https://pythonscraping.com/pages/page3.html> kunt scrapen, maar met uitzondering van het eerste `tr`-element (deze bevat de tabelkopjes en die hebben we niet nodig). In de README van Pup staan de selectors die je kunt gebruiken. Volg de link naar MDN om uit te zoeken hoe ze werken.

    <textarea name="form[q6]" rows="4" required></textarea>

1.  Extra opdracht (optioneel): zoek uit hoe je een JSON kunt genereren met daarin alle links en headlines als paren. Zo'n paar ziet er dan zo uit:

        {
          "href": "/artikel/2441789-vogelspin-ontsnapt-op-kinderdagverblijf-velp",
          "text": "Vogelspin ontsnapt op kinderdagverblijf Velp"
        }

    Omdat het een lijst van paren is verwachten we dat hele de JSON een array is, dus begint met `[` en eindigt met `]`.

    <textarea name="form[q7]" rows="4" required></textarea>
