# Technisch ontwerp

Je hebt een voorstel gemaakt en aangepast, en nu is het tijd om te gaan puzzelen hoe je website past in het Flask-framework. Je hebt inmiddels wat ervaring opgedaan met dat framework, dus je weet dat MVC hier een belangrijke rol speelt (zie Lecture 8).

## Controllers

In Flask werk je standaard met één controller, namelijk `application.py`. Hierin worden diverse functies gedefinieerd, die elk een bepaalde "route" afhandelen. Je kunt nu al goed voorspellen welke pagina's je gaat maken: veel heb je al uitgetekend in je proposal.

Er zijn ook routes die niet aan een scherm gekoppeld zijn. Soms heb je een route die er voor dient om een formulier te verwerken. Deze route zal eindigen met een redirect naar een andere route.

> Doen: maak een lijst van routes (met korte omschrijving) en bedenk alvast de naam van de functie. Geef aan of er een scherm bij hoort en of het een GET of POST request is.

## Views

Als je gaat nadenken over de controllers zal waarschijnlijk blijken dat er nog schermen ontbreken in je projectvoorstel. Nu is het moment om dat uit te breiden.

> Doen: maak een nieuwe schets van je applicatie, waarin alle schermen uitgetekend zijn. Het doel is om snel een goed overzicht van de hele applicatie te krijgen. Zorg dus dat je schermen die bij elkaar horen ook groepeert. En laat met pijlen zien als een knop doorlinkt naar een ander scherm.

## Models/helpers

In CS50 Finance schrijf je zelf de SQL-queries direct in de functies van de controller. Dat kun je nu ook weer doen. Mocht je ergens een stuk ingewikkelde code nodig hebben, dan heeft het wellicht zin om daar een aparte Python-module van te maken die je dan `import` in de controller. Ook kan het zijn dat je bepaalde functies vaak nodig hebt, zoals `apology()` en `usd()` in de `helpers.py` van CS50 Finance.

> Doen: bekijk zoveel mogelijk wat voor hulpfuncties je nodig zal hebben en maak een lijst van één of meer helper-modules met die functies. Geef van elke functie een korte omschrijving waar deze voor dient.

## Geavanceerde architectuur

Als je veel ervaring hebt met webprogrammeren dan zul je misschien op zoek gaan naar mogelijkheden om een grote Flask-app beter te structureren, bijvoorbeeld om de controller op te splitsen in meerdere bestanden. Dat is akkoord, maar het is belangrijk dat de hele groep goed mee kan komen hierin. Als jij de lead neemt hierin, dan is het jouw taak om de rest van de groep goed uit te leggen hoe het werkt.

## Plugins en frameworks

Wil je plugins voor Flask gebruiken of een framework zoals Bootstrap? Dat moet nu ook vastgelegd worden in het ontwerpdocument. Dan weet je wat je nog moet uitzoeken.

> Doen: geef een korte lijst van plugins en frameworks die je gebruikt, elk met een URL van waar informatie/documentatie te vinden is.

## Update projectvoorstel

Je projectvoorstel moet nu nog aangepast worden aan de nieuwe ideeën die je hebt opgedaan sinds het inleveren van de eerste versie.

> Doen: pas je projectvoorstel aan zodat het precies in sync is met je technisch ontwerp. Je projectvoorstel gaat ook dienen als README van je project op GitHub, zodat iedereen snel kan zien waar het voor dient.

## Submit

Je kunt Markdown-documenten ook in Slack posten. Zet het definitieve document (en het nieuwe "voorsgtel") dus in het kanaal van je groep zodat de docenten dit kunnen bekijken. We bespreken het bij de afspraak op donderdag/vrijdag. Vergeet niet om de schetsen er ook bij te zetten!

## Verder

De volgende stap in het project is een eerste versie van je Flask-app op GitHub zetten, en werken aan het invullen van alle pagina's!
