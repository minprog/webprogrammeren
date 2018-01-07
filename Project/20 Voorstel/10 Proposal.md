# Projectvoorstel

In de eerste dagen ga je een projectvoorstel maken. Dit document dient ervoor om te zorgen dat de groep het zelfde doel nastreeft, en om te zorgen dat assistenten en docenten een goede inschatting kunnen maken over de complexiteit van het project: is het te veel of misschien juist te weinig werk?

Je gaat je voorstel schrijven in "Markdown", een manier om snel teksten te schrijven met opmaak voor een HTML-browser. Zie [Markdown](/naslag/markdown) voor de documentatie.

## Samenvatting

Beschrijf in 4--5 zinnen wat het doel van je webapplicatie is, waarom het een uniek idee is[^1] en wat bezoekers er aan hebben. Schaaf een paar keer aan je omschrijving. Probeer 'm kort en bondig te houden, maar wel zodat anderen er een snel idee van je applicatie bij krijgen. Denk ook aan spelfouten!

## Schetsen

Om een concreet beeld te vormen van de applicatie, moeten er schetsen bijgevoegd zijn van de verschillende *schermen* die een rol spelen in de applicatie. Als je bijvoorbeeld naar Twitter kijkt, dan zie je deze belangrijke schermen:

1. ontvangstpagina voor niet-ingelogde gebruikers (homepage)
2. timeline voor ingelogde gebruikers (dat is hun homepage)
3. notificaties/meldingen
4. privéberichten (dit is een popup)
5. persoonlijke instellingen
6. schrijf een nieuwe tweet (popup)

De schetsen van deze pagina's moeten goed leesbaar en redelijk netjes zijn. Dat betekent niet dat je ze op de computer hoeft te maken: je mag ze ook met pen en papier maken en dan fotograferen (gebruik liefst een speciaal programma om er nette PDF's van te maken). Maar je kunt bijvoorbeeld ook Powerpoint of Keynote gebruiken om snel diagrammen te maken.

Hier een voorbeeld van een zeer nette en complete schets voor een mobiele app, waar met pijlen ook is aangegeven wat de navigatiemogelijkheden zijn. Dat is ook belangrijk bij een website.

![](screens-proposal.png)

## Features

Producten zijn altijd een combinatie van allerlei *features*. die beschrijven wat je er mee kunt. Bij websites heeft elke (grote) feature vaak een eigen scherm. Maar het is niet precies hetzelfde, want kleinere features zijn vaak details van een webpagina, en je hebt ook grote features die op meerdere plekken in de applicatie invloed hebben. Kijken we weer naar Twitter, dan kun je denken aan deze features:

1. gebruikers kunnen andere gebruikers volgen
2. gebruikers kunnen een lijst zien van tweets van andere gebruikers die zij volgen (de timeline)
3. gebruikers kunnen gewaarschuwd worden als:
    - er een nieuwe tweet is geplaatst door een gebruiker die zij volgen
    - er een nieuw privébericht aan ze is gestuurd
4. gebruikers kunnen kiezen of ze waarschuwingen per mail, sms, popup willen ontvangen
5. ....

In je document neem je een lijst features op. De meeste features moeten ook zichbaar zijn in de schetsen. Waarschijnlijk moet je (terwijl je met je team discussieert) een beetje heen en weer springen tussen schetsen maken en features verzinnen.

## Minimum viable product

We willen graag een *product* maken dat aan de eisen voldoet. Waarschijnlijk heb je al extra features bedacht of zijn er dingen waar je als groep over twijfelt. 

Om te zorgen dat je uiteindelijk wel een product oplevert dat "klopt", kun je nu al markeren welke combinatie van features nodig is voor het *minimum viable product* (MVP). Andere features zijn dan optioneel.

## Afhankelijkheden

Nu je dit hebt gedaan (en je hebt inmiddels ook een beetje een beeld van hoe webapplicaties in elkaar zitten) kun je een eerste lijst van afhankelijkheden maken: dingen die je niet zelf programmeert maar wel moet gebruiken, begrijpen of regelen.

- Maak een lijst van de **databronnen** die je gekozen hebt voor je project, bijvoorbeeld de URL van een website waar je de API kunt vinden.

- Maak een lijst van **externe componenten** die je nodig hebt. Bijvoorbeeld Bootstrap voor het maken van een simpele website.

- Zoek een paar **concurrende bestaande** websites en beschrijf een paar punten die interessant zijn. Elke website heeft natuurlijk nét weer een andere insteek en het is goed om je bewust te zijn van de kracht van jouw website tegenover de concurrentie.

- Maak een lijst van de **moeilijkste delen** van de applicatie. Wat wordt veel uitzoekwerk? Wat is gewoon echt moeilijk? Wat heb je nodig om het makkelijker te maken? Deze lijst is waarschijnlijk makkelijker te maken als je al weer wat meer weet van webapplicaties maken, maar als je nu al iets hebt, noteer het in je document.

## Sanity check

Check, voordat je verder gaat, of je voorgestelde applicatie klopt met de projecteisen zoals ze in de [studiewijzer](/) staan. En laat iemand van buiten je groep nog een keer je voorstel bekijken, dan kun je onduidelijkheden en spelfouten nog verbeteren. Vergeet ten slotten niet om in het document netjes de naam van de applicatie en de namen van de groepsleden op te nemen!

## Submit

Je kunt Markdown-documenten ook in Slack posten. Zet het definitieve document dus in het kanaal van je groep zodat de docenten dit kunnen bekijken. We bespreken het bij de afspraak op donderdag/vrijdag. Vergeet niet om de schetsen er ook bij te zetten!

## Verder

De volgende stap voor het project is om een *technisch ontwerpdocument* te maken. Daar vertaal je de eisen uit je projectvoorstel naar een technische opzet voor je project. Daarbij maak je gebruik van je kennis over hoe Flask-projecten in elkaar zitten.
