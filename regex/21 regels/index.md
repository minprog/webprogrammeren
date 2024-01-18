# Regels matchen

In deze opgaven ga je op zoek naar **regels** die matchen in een tekstbestand. De output bestaat uit de regels (ook wel "zinnen" genoemd) waarin een match voorkomt. Dit is een standaard-gebruik van `grep`.

Als we het volgende tekstbestand `zin.txt` hebben:

    woorden schieten
    tekort maar daarna
    blijft alles hangen

En we gebruiken het commando `grep` met een reguliere expressie die matcht op de letter `s` of de letter `t` aan het begin van een woord:

    $ grep -E "\b[st]" zin.txt

Dan zal de output zijn:

    woorden schieten
    tekort maar daarna

Voor onderstaande opdrachten formuleer je je antwoord ook steeds als een `grep`-commando. Je ziet dat de reguliere expressie tussen aanhalingstekens wordt gegeven.

Gebruik tot slot de optie `-i` van grep om (indien gevraagd) matches onafhankelijk te maken van het gebruik van hoofd- of kleine letters. Het volgende commando selecteert regels waarin een grote of een kleine letter A staat:

    $ grep -E -i "A" zin.txt

Als je testbestanden maakt voor de opdrachten, doe dat dan niet in Windows met Notepad of Atom. Gebruik in plaats daarvan `nano` (zoals uitgelegd in de Software Carpentry workshop). Dan zijn de line endings correct voor gebruik van `grep`. Als je er technisch niet uitkomt, vraag dan ook hulp!

## Opgaven

Het doel van deze opgaven is om te experimenteren en uit te vogelen hoe alles werkt. Probeer het antwoord niet direct op te zoeken maar denk goed na welke onderdelen van reguliere expressies je kunt combineren om het doel te bereiken. Vraag ook hulp waar nodig!

1.  Geef een compleet grep-commando waarmee je elke regel selecteert waar aan het eind van de regel een punt (`.`) staat. Bedenk voorbeeldzinnen die matchen en zinnen die niet matchen.

2.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin de string `the` (of `The`) staat. `There is nothing.` moet ook matchen. Bedenk voorbeeldzinnen die matchen en zinnen die niet matchen.

3.  Geef een compleet grep-commando waarmee je elke regel selecteert die met `A`, `D` of `W` begint. Bedenk voorbeeldzinnen die matchen en zinnen die niet matchen.

4.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin een `o` staat gevolgd door één of meer `r`. Bedenk voorbeeldzinnen die matchen en zinnen die niet matchen.

5.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin een vraagteken óf een backslash staan. Bedenk voorbeeldzinnen die matchen en zinnen die niet matchen.
