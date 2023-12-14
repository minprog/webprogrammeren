# Strings matchen

In deze opgaven ga je op zoek naar **strings** die matchen. De input is een bestand met tekst, eventueel met meerdere regels, en de output zijn de losse strings (delen van regels) die matchen. Dat kunnen daarom ook meerdere strings op één regel zijn. Hiervoor gebruik je de optie `-o` van `grep`.

Om een voorbeeld te geven gebruiken we weer `zin.txt`:

    woorden schieten
    tekort maar daarna
    blijft alles hangen

Een `grep`-commando om strings te selecteren met voorbeeld-output:

    $ grep -o "\b[st]"
    s
    t

Vergelijk met de vorige pagina en begrijp waarom dit zo werkt voordat je gaat oefenen. Bespreek altijd met je medestudenten en de assistenten als je iets niet begrijpt.

## Opdrachten

Het doel van deze opgaven is om te experimenteren en uit te vogelen hoe alles werkt. Probeer het antwoord niet direct op te zoeken maar denk goed na welke onderdelen van reguliere expressies je kunt combineren om het doel te bereiken. Vraag ook hulp waar nodig!

1.  Geef een compleet grep-commando waarmee je elke string selecteert die bestaat uit de letters `we`. Bedenk voorbeeldteksten die matchen en controleer goed welke delen een match zijn. Bedenk ook teksten die geen matches bevatten.

2.  Geef een compleet grep-commando waarmee je elke string selecteert die begint met "Wachtwoord" en eindigt met een viercijferig getal. Hoofd- of kleine letters mogen allebei. Bedenk voorbeeldteksten die matchen en controleer goed welke delen een match zijn. Bedenk ook teksten die geen matches bevatten.

3.  Geef een compleet grep-commando waarmee je elke string selecteert die begint met `A`, `D` of `W` en daarna één of meer kleine letters heeft. Bedenk voorbeeldteksten die matchen en controleer goed welke delen een match zijn. Bedenk ook teksten die geen matches bevatten.

4.  Geef een compleet grep-commando waarmee je elk woord selecteert waarin een `o` staat gevolgd door één of meer `r`. Bedenk voorbeeldteksten die matchen en controleer goed welke delen een match zijn. Bedenk ook teksten die geen matches bevatten.
