# Homepage

Bouw een profielpagina voor jezelf met HTML, CSS en wat JavaScript.

## Achtergrond

Op het internet kun je de meest uiteenlopende toepassingen gebruiken: we kunnen met een zoekmachine onderzoek doen naar alles wat er maar te weten is, we kunnen communiceren met vrienden en familieleden over de hele wereld, spelletjes spelen, cursussen volgen en nog veel meer.

Het blijkt dat bijna alle pagina's die we bezoeken zijn gebouwd op basis van drie talen, die elk een eigen doel dienen:

1. HTML, of _HyperText Markup Language_, dat wordt gebruikt om de inhoud van websites te beschrijven;
2. CSS, _Cascading Style Sheets_, dat wordt gebruikt om de layout en esthetiek van websites te beschrijven; en
3. JavaScript, dat wordt gebruikt om websites interactief en dynamisch te maken.

Maak in deze opdracht een profielpagina waarmee jezelf introduceert aan de wereld, en daarbij je favoriete hobby of buitenschoolse activiteiten, je interesses (denk aan muziek, boeken, eten) en/of je motivatie om Informatiekunde te studeren.

## Opstarten

Dit zijn de instructies om de "distributiecode" te downloaden die je nodig hebt om een begin te maken met deze opdracht:

1.  Open Git Bash en voer `cd` uit om ervoor te zorgen dat je in `~/` (oftewel je thuismap) bent.

2.  Geef het commando `curl -LO https://cdn.cs50.net/2022/fall/psets/8/homepage.zip` om een (gecomprimeerd) zip-bestand met de distributie van dit probleem te downloaden.

3.  Geef het commando `unzip homepage.zip` om dat bestand uit te pakken.

4.  Geef het commando `rm homepage.zip` om het zip-bestand te verwijderen.

5.  Geef het commando `ls`. Je zou een map genaamd `homepage` moeten zien, met daarin de bestanden die uit het zip-bestand komen.

6.  Geef het commando `cd homepage` om naar die map te gaan.

7.  Geef het commando `ls`. Je zou de bestanden voor deze opdracht moeten zien, namelijk `index.html` en `styles.css`.

8.  Je kunt een "server" starten om de site te bekijken door het volgende uit te voeren:

        $ python3 -m http.server -b localhost 8080

9. Opening dan het addres <http://localhost:8080/> in je webbrowser.

## Specificatie

Maak op basis van de gegeven bestanden een website die voldoet aan de volgende eisen:

*   De website moet minimaal vier verschillende `.html`-pagina's bevatten, inclusief `index.html`  (de hoofdpagina van je website). Het moet mogelijk zijn om vanaf *elke* pagina op je website naar *elke* andere pagina te gaan door één of meer hyperlinks te volgen.

*   De pagina `index.html` moet een profielfoto, je naam en een korte beschrijving van jou en je interesses bevatten.

*   Gebruik minstens tien (10) verschillende HTML-tags naast `<html>`, `<head>`, `<body>`, en `<title>`. Het meerdere keren gebruiken van een tag (bijv. `<p>`) telt nog steeds als één (1) van die tien!

*   Integreer een of meer functies van Bootstrap in je site. Bootstrap is een populaire bibliotheek of library waarmee je je site kunt verfraaien. Bekijk de [documentatie van Bootstrap](https://getbootstrap.com/docs/5.3/) om aan de slag te gaan. Specifiek is het handig om te kijken bij de [componenten van Bootstrap](https://getbootstrap.com/docs/5.3/components/). Om Bootstrap aan je site toe te voegen, volstaat het om

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>

    in de `<head>` van je pagina's op te nemen. Daaronder heb je dan de link naar jouw eigen CSS-bestand staan:

        <link href="styles.css" rel="stylesheet">

*   Er moet ten minste één stylesheet-bestand `styles.css` gebruikt worden waarin je zelfgeschreven CSS-regels hebt staan. Hiervoor moet je minstens vijf (5) verschillende CSS-selectors gebruiken (bijvoorbeeld op tag (`voorbeeld`), class (`.voorbeeld`), of ID (`#voorbeeld`)), en minstens vijf (5) verschillende CSS-eigenschappen zoals `font-size` of `margin`.

*   Integreer een of meer functies van JavaScript in je site om je site interactiever te maken. Je kunt bijvoorbeeld JavaScript gebruiken om waarschuwingen toe te voegen, om een effect op regelmatige tijdstippen te laten plaatsvinden, of om interactiviteit toe te voegen aan knoppen, keuzemenu's of formulieren. Voel je vrij om creatief te zijn!

## Testen

Om de website te bekijken terwijl je er aan werkt gebruik je het volgende commando:

    $ python3 -m http.server -b localhost 8080

In je webbrowser moet je dan naar het adres <http://localhost:8080/> gaan.

## Nakijken

De website zal beoordeeld worden door te controleren of deze aan de eisen voldoet die hierboven worden genoemd, én of je HTML er netjes uitziet, valide is, en goed gebruik hebt gemaakt van de mogelijkheden van de talen om een verzorgde website te maken.

**Validiteit HTML** Om te zorgen dat je HTML inderdaad valide is, gebruik je de [Markup Validation Service](https://validator.w3.org/#validate_by_input), waar je je HTML-pagina's direct in de tekstbox plakt.

Zorg dat je *alle* warnings en errors oplost voordat je definitief gaat submitten.

**Netheid HTML en CSS** Zorg dat je indentatie op orde is in je HTML-bestanden, CSS en Javascript. Ook kun je als volgt comments schrijven in HTML:

    <!-- Comment goes here -->

In CSS kun je als volgt comments schrijven:

    /* Comment goes here */

**Overige aanwijzingen**

* Denk goed na of de layout en andere design-keuzes voor je website ervoor zorgen dat een gebruiker intuitief de juiste informatie kan vinden en op een prettige manier kan navigeren.

* Denk na of het nodig is de CSS op te splitsen over meerdere bestanden als deze groot wordt.

* Bestudeer hoe je herhaling van instructies kunt voorkomen in CSS door goed gebruik te maken van het "cascading" idee van CSS.

## Naslag

Gebruik deze tutorials voor meer hulp bij het begrijpen van de drie talen en de mogelijkheden die je hebt:

* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)
