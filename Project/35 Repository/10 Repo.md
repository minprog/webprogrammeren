# Repository

Alle documentatie en code van je project moet op GitHub terecht komen, en vanaf de tweede week zul je ook samenwerken via Git. Als het goed is heb je een college gevolgd over het gebruik van Git. Voor meer uitleg over dit systeem, zie [de Git-naslag](/naslag/git).

> Tip: er zijn allerlei manieren om goed samen te werken via git. We houden het hier simpel. Het belangrijkste is dat we "merge conflicts" willen voorkomen: als twee teamleaden aan het zelfde bestand werken en aanpassingen met elkaar botsen. Er zijn twee maatregelen die je moet nemen: 1) zorg dat je goed verdeelt wie aan welk bestand werkt, je kunt bijvoorbeeld meerdere CSS-bestanden maken als dit handig is, en 2) voordat je `git commit` doet even de laatste versie van de centrale repo binnen halen met `git pull`.

## Aanmaken van je repository

1.  Ga naar <https://github.com/new> en maak een nieuwe repository. Vink het boxje aan om alvast een lege `README.md` aan te maken.

    ![Check Initialize this repository with a README](readme.png)

2.  Je krijgt een overzicht van de repository waar nu alleen die `README` in staat. Bij **Settings** kun je toegang geven aan de overige teamleden.

3.  Nu kan iedereen een lokale kopie maken van de repository. Alle teamleden gaan naar de Terminal van hun IDE en halen de repository binnen via het commando:

        https://github.com/<username>/project.git

4.  Als je nieuwe repository "project" heet, dan wordt er ook een map aangemaakt in de IDE met die naam. Dit is de lokale kopie, waarin je wijzigingen kan doen en eventueel terugsturen naar de centrale repository op GitHub.

5.  Eén van de teamleden gaat de `README.md` vullen met het projectvoorstel. Zoals je zult zien, zorgt GitHub ervoor dat de Markdown uit de `README` netjes naar HTML wordt vertaald en dat de kopjes eruit zien als kopjes.

6.  Hetzelfde teamlid kan de aangepaste `README` nu committen en pushen via de terminal:

        git add README.md
        git commit -m "Overnemen projectvoorstel"
        git push origin master

    Let daarbij op dat je in de "project"-directory staat!

7.  De andere teamleden kunnen de aangepaste versie binnen halen:

        git pull origin master

## Toevoegen van je ontwerpdocument

Ook dit document wordt initieel door één teamlid toegevoegd aan de repository. Je ontwerpdocument moet `DESIGN.md` heten. Je kunt het net als de `README.md` toevoegen en pushen.

## Toevoegen van plaatjes

Er horen ook schetsen bij de documenten. Omdat je straks code gaat toevoegen aan je repository, is het handig om de andere spullen apart te houden. Maak in je lokale versie een map `doc` aan:

    mkdir doc

En upload de plaatjes door ze in de IDE naar die map te slepen. Vervolgens kun je die plaatjes op dezelfde manier toevoegen en pushen:

    git add doc/*
    git commit -m "Plaatjes voorstel en ontwerp"
    git push origin master
