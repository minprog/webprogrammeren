# Bootstrappen van het project

Niet te verwarren met [de gelijknamige library](https://getbootstrap.com/), is bootstrappen de eerste stap van het project. Hier ga je ervoor zorgen dat iedereen in het team een draaiende versie van de website voor zich heeft, en daaraan kan bijdragen. Dat is een kwestie van de juiste software en packages installeren, en ook de code met elkaar delen. Dit gaat nooit helemaal soepel, want iedereen heeft een andere machine voor zich. Daarom ga je voor deze milestone in een Zoom-sessie met je teamgenoten zodat jullie elkaar kunnen helpen. Kom je er nou niet uit, dan is het direct taak om contact met een assistent op te nemen via de hands.


## Finance

Vorige week hebben jullie allemaal een versie van Finance geïmplementeerd. Dit wordt het beginpunt van de website, het eerste raamwerk waar je vanaf gaat bouwen. Zo heb je meteen een initiële database, een homepagina en een loginscherm. Dat maakt het mogelijk dat je samen kan werken, zonder elkaar op elk punt in de weg te zitten. Allereerst zul je moeten kiezen welke Finance project de basis gaat vormen. Kijk even naar elkaars code en maak die keuze.


## Git

De volgende stap is om de code met elkaar te delen. Dit doe je via `git`, zie ook [de lecture](/lectures/git) en [de naslag](/naslag/git). Git zul je waarschijnlijk moeten installeren. Hoe je dat doet hangt af van wat voor besturingssysteem je gebruikt.

Voor Windows kan je `git` hier downloaden: [git-scm.com/downloads](https://git-scm.com/downloads) en daarvandaan installeren.

Op de Mac wordt git automatisch geïnstalleerd als je dit voor de eerste keer gebruikt. Je kan dit controleren met:

        git --version

Had je git nog niet geïnstalleerd? Dan krijg je nu de vraag of je de "Command line tools" wilt installeren. Anders krijg je te zien welke versie van git je hebt geïnstalleerd.

Onder Linux vertrouwen we erop dat je zelf de beste weg vindt. Het hangt nou eenmaal af van welke distributie je draait en hoe je zelf het systeem wilt onderhouden. Natuurlijk kan je ons wel om hulp vragen!


## GitHub

De volgende stap is om de code op een locatie te zetten waardoor je teamgenoten (en wij) er ook bij kunnen. Hiervoor gebruiken we bij dit vak GitHub (Classroom), door op [deze](https://classroom.github.com/g/CLqDDtqT) link te klikken maakt één persoon een groep aan. Vervolgens kunnen je groepsgenoten via dezelfde link de groep selecteren.


## Eerste commit & push

GitHub geeft je bij het aanmaken ook meteen de instructies voor de eerstvolgende stappen:

![eerste push](firstpush.png)

Onze situatie is iets anders dan die hierboven, want je hebt al een project (Finance) en wilt dit nu in deze repository zetten. Dus pak je code van Finance, zet deze in een map op je computer. Navigeer met je terminal naar die map en draai daar de volgende commando's:

        git init
        git add .
        git commit -m "first commit"
        git branch -M main
        git remote add origin https://github.com/uva-webapps/WebIK-<TEAMNAAM>.git
        git push -u origin main

> Vergeet niet `<TEAMNAAM>` te vervangen met jouw teamnaam naam.


## Finance draaien

Om Finance lokaal te kunnen draaien moet je Flask installeren, dit gaat via `pip`. Dit is even afhankelijk van hoe Python geïnstalleerd staat op jouw machine. Check allereerst even je Pythonversie met

        python --version

en:

        python3 --version

Eén van de twee zou een versienummer met 3.+ moeten opleveren. Afhankelijk daarvan draai je:


        python -m pip install flask

Of

        python3 -m pip install flask

> Mocht je al bekend zijn met pip, en nu denken: Huh, `python -m pip` i.p.v. gewoon `pip`? `python -m` is een snelle manier om een package van een Python installatie te draaien. Zo weet je zeker dat je de juiste `pip` te pakken hebt, en niet ééntje die hoort bij een andere Python installatie.

Vervolgens kan je Finance draaien met:

        flask run

Wellicht dat je eerst nog een API_KEY moet `export`en. Zie daarvoor de [Finance opdracht](/problems/finance).


## Inleveren

Staat alle Finance code op GitHub, deel dan hieronder de GitHub-url van jullie repo.
