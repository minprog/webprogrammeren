# Woorden matchen

In deze volgende opgaven ga je op zoek naar **woorden** die matchen. De input is een bestand met tekst met meerdere regels, en de output zijn losse woorden die matchen met de reguliere expressie. Hiervoor gebruik je de optie `-w` van `grep`.

Daarbij kijken we enerzijds naar het zoeken van woorden in regels, waarbij de hele regel geprint wordt (alleen de optie `-w`); en anderzijds naar het zoeken van alleen de woorden zelf, waarbij als resultaat de woorden geprint worden (de gecombineerde optie `-o -w`).

## Opdrachten

Beantwoord de vragen hieronder. Het doel is om te experimenteren en uit te vogelen hoe alles werkt. Probeer het antwoord niet direct op te zoeken maar denk goed na welke onderdelen van reguliere expressies je kunt combineren om het doel te bereiken. Vraag ook hulp waar nodig!

1.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin het woord (dus niet de string) `we` staat. Bedenk voorbeelden die matchen en voorbeelden die niet matchen.

2.  Geef een compleet grep-commando waarmee je elk woord `we` selecteert. Bedenk voorbeelden die matchen en voorbeelden die niet matchen.

3.  Geef een compleet grep-commando waarmee je elke regel selecteert die een woord bevat dat begint met "Wachtwoord" en eindigt met een viercijferig getal. Hoofd- of kleine letters mogen allebei. Bedenk voorbeelden die matchen en voorbeelden die niet matchen.

4.  Geef een compleet grep-commando waarmee je elk woord selecteert dat begint met "Wachtwoord" en eindigt met een viercijferig getal. Hoofd- of kleine letters mogen allebei. Bedenk voorbeelden die matchen en voorbeelden die niet matchen.

5.  Geef een compleet grep-commando waarmee je elk woord selecteert dat met `A`, `D` of `W` begint. Bedenk voorbeelden die matchen en voorbeelden die niet matchen.

6.  Geef een compleet grep-commando waarmee je elk woord selecteert waarin een `o` staat gevolgd door één of meer `r`. Bedenk voorbeelden die matchen en voorbeelden die niet matchen.
