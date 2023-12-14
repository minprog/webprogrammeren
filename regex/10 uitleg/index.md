# Reguliere expressies

Reguliere expressies worden veel gebruikt voor het automatisch verwerken van teksten. Vaak gaat het dan niet om het inlezen van gestructureerde data (zoals uit een CSV-bestand) maar teksten die vrij ingevoerd kunnen worden door een gebruiker.

Het is onder andere gebruikelijk om met reguliere expressies het *format* van een mailadres te controleren. Een mailadres moet uit een aantal vaste componenten bestaan die je heel handig met een reguliere expressies kunt beschrijven. Als iemand een adres opgeeft dat niet aan de regels voldoet is het snel gespot.

    hwaziz@yahoo.com -> geldig mailadres
    d.malan@cs.harvard.edu -> geldig mailadres
    harrie+spam@gmail.com -> geldig mailadres
    geheimtipps2gmail.com -> niet geldig, '@' is per ongeluk vervangen door '2'?
    freedom_warrior@hotmailnl -> niet geldig, tikfout?

Een andere toepassing is het *ontleden* van een tekstje. Als je bijvoorbeeld een gebruiker een "adres" laat invoeren dan is er meestal sprake van een straatnaam en een huisnummer. In sommige landen komt het huisnummer eerst, en in andere landen staat het juist achteraan. Met één of meer reguliere expressies kun je zo'n ingevoerd adres makkelijk splitsen in beide componenten. Althans... makkelijk. Er zijn altijd uitzonderingen.

    2981 Rushdie Ave. -> Canadees adres?
    1098 XH -> dit lijkt verdacht veel op een NL postcode, niet een straat + nummer
    Science Park 900 -> Nederlands adres?
    12 Septemberstraat 26 -> in België
    Archipel 30 22 -> straatnamen waren op in Lelystad ("Archipel 30" is de straatnaam)

Je kunt proberen de geldige en ongeldige patronen te vatten in een reguliere expressie en daarmee fouten snel helpen oplossen (bijvoorbeeld vóórdat je webshop een duur pakketje naar een fout adres stuurt!). Zoals je ziet zijn er wel haken en ogen aan.

Overigens kan je ook in de problemen komen met simpelere regels. Zo zijn er mensen op de wereld [die maar één naam hebben](https://scholar.google.com/citations?user=eGOkAUMAAAAJ&hl=nl&oi=ao), dus niet per se een voornaam én een achternaam. Als je in je systeem vastlegt dat er een foutmelding komt als iemand geen spatie in de naam invoert, dan kan deze persoon zich alleen met omwegen registreren. Heel irritant!

Dat klinkt niet als een goed reclamepraatje voor reguliere expressies maar in de praktijk zijn ze dus erg handig om stukjes tekst automatisch te controleren of te ontleden. Bovendien kun je er heel handig mee zoeken in langere teksten.

## Studiemateriaal

1.  Lees het hoofdstuk "Regular expressions, text normalization" uit het boek _Speech and Language Processing_ van Jurafsky en Martin. Dit geeft een basisbegrip van de manier van werken met reguliere expressies.

2.  Webbrowsers kunnen ook reguliere expressies verwerken. Daarvan wordt gebruik gemaakt in de tutorial op [regexlearn.com](https://regexlearn.com/learn/regex101). Hier kun je je eerste praktische ervaring opdoen met reguliere expressies. Volg de tutorial.

    - Let op dat reguliere expressies voor een groot deel standaard zijn, maar dat ze soms ook een klein beetje anders kunnen werken op verschillende platforms. Zo krijg je in de tutorial hierboven wat extra syntax (manier van schrijven) die niet ondersteund wordt door `grep`.

    - Onthou dat het om de basis gaat van `*`, `.`, `+`, `?`, `()`, `[]` enzovoort. Die basis is overal gelijk en kun je steeds toepassen om teksten heel precies te filteren.

Na deze oefeningen kun je naar de volgende pagina om te oefenen met reguliere expressies.
