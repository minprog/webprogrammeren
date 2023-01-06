# Reguliere expressies

Beantwoord de vragen hieronder. Let ook weer op de laatste vraag.

- Je antwoorden moeten in een PDF worden ingeleverd met een overzichtelijke opmaak
- De PDF moet bij voorkeur gemaakt zijn met LaTeX
- De vragen moeten zijn opgenomen in de PDF met het antwoord er steeds direct onder
- De naam van de cursus, de opdracht en jouw eigen naam moeten ook vermeld zijn bovenaan het document
- Je mag géén titelblad gebruiken, dat is teveel onzinnige ruimte voor zo'n korte opdracht
- Als je informatie van buiten het boek gebruikt moet je een bronvermelding doen, maar je hoeft hiervoor geen LaTeX-referenties te gebruiken; je mag gewoon de site/titel noemen in de tekst

Als je testbestanden maakt voor de opdrachten, doe dat dan niet in Windows met Notepad of Atom. Gebruik in plaats daarvan `nano` (zoals uitgelegd in de Software Carpentry workshop). Dan zijn de line endings correct voor gebruik van `grep`. Als je er technisch niet uitkomt, vraag dan ook hulp!

Zorg dat je de reguliere expressies en voorbeelden netjes opmaakt in je PDF, zodat ze goed herkenbaar en leesbaar zijn als code. Vermeld bovenaan ook welke omgeving je gebruikt (Linux, MacOS, Git Bash, enz.) omdat grep op verschillende platforms anders werkt.

## Opdracht

Voor deze opdrachten moet je reguliere expressies schrijven en voorbeelden geven die wél en niet werken. Je moet hiervoor `grep`, `egrep` of `fgrep` gebruiken zoals in het boek beschreven. Gebruik de UNIX manual pages op jouw systeem om te juiste opties (flags) te vinden die je nodig hebt.

Er wordt hieronder ook gevraagd naar **edge cases**. Dit zijn de voorbeelden waar je het uiterste vraagt van de reguliere expressie. Stel dat je een commando moet geven om alle woorden met een letter `a` erin te vinden; dan wil je zeker checken of een woord met daarin alleen de letter `a` (en niets anders) ook correct matcht. In sommige gevallen kan het zinvol zijn om te kijken of een match aan het begin of eind van een regel ook correct werkt en niet alleen in het midden. Welke edge case zinvol is hangt af van de reguliere expressie.

## Zinnen

In de volgende opgaven ga je op zoek naar **zinnen** die matchen. De input is een bestand met meerdere regels en de output zijn de regels (zinnen) waarin een match voorkomt. Dit is een standaard-gebruik van `grep` zoals in het boek ook steeds wordt getoond.

1.  Geef een compleet grep-commando waarmee je elke regel selecteert waar aan het eind van de regel een punt (`.`) staat. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

2.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin de string `the` (of `The`) staat. `There is nothing.` moet ook matchen. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

3.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin het woord (dus niet de string) `we` staat. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

4.  Geef een compleet grep-commando waarmee je elke regel selecteert die met `A`, `D` of `W` begint. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

5.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin een `o` staat gevolgd door één of meer `r`. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

6.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin een vraagteken óf een backslash staan. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

## Strings

In de volgende opgaven ga je op zoek naar **strings** die matchen. De input is een bestand met tekst, eventueel met meerdere regels, en de output zijn de losse strings (delen) die matchen. Hiervoor gebruik je normaal de optie `-o` van `grep`. Je kunt deze ook combineren met de optie `-w` om alleen strings te matchen die een heel woord zijn.

1.  Geef een compleet grep-commando waarmee je elke string selecteert die bestaat uit het woord `we`. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

2.  Geef een compleet grep-commando waarmee je elke string selecteert die begint met "Wachtwoord" en eindigt met een viercijferig getal. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

## Reflectie

1.  Beschrijf welke opvallende dingen je hebt geleerd bij het lezen in het boek, doen van de tutorial en het uitwerken van de vragen. Geef aan wat je eventueel moeilijk vond en welke bronnen je hebt gebruikt om verder uit te zoeken wat je moest begrijpen. Zonder uitgebreid antwoord op deze vraag kun je geen punten halen voor de opdracht.

<!--
- https://leanpub.com/bastards-regexes
- https://algs4.cs.princeton.edu/54regexp/
- https://v4.software-carpentry.org/regexp/index.html
-->

## Nakijken

Deze opdracht wordt afgetekend. Kom dus langs bij een laptopcollege om dat te regelen. Bovenstaande oefeningen zijn nuttig om reguliere expressies te leren maar ze zijn makkelijk "op te zoeken". Reguliere expressies worden daarom ook getoetst op het tentamen, want de bedoeling is dat je er wat handigheid in krijgt!
