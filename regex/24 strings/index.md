# Reguliere expressies

Beantwoord de vragen hieronder.

Als je testbestanden maakt voor de opdrachten, doe dat dan niet in Windows met Notepad of Atom. Gebruik in plaats daarvan `nano` (zoals uitgelegd in de Software Carpentry workshop). Dan zijn de line endings correct voor gebruik van `grep`. Als je er technisch niet uitkomt, vraag dan ook hulp!

## Opdracht

Voor deze opdrachten moet je reguliere expressies schrijven en voorbeelden geven die wél en niet werken. Je moet hiervoor `grep`, `egrep` of `fgrep` gebruiken zoals in het boek beschreven. Gebruik de UNIX manual pages op jouw systeem om te juiste opties (flags) te vinden die je nodig hebt.

Er wordt hieronder ook gevraagd naar **edge cases**. Dit zijn de voorbeelden waar je het uiterste vraagt van de reguliere expressie. Stel dat je een commando moet geven om alle woorden met een letter `a` erin te vinden; dan wil je zeker checken of een woord met daarin alleen de letter `a` (en niets anders) ook correct matcht. In sommige gevallen kan het zinvol zijn om te kijken of een match aan het begin of eind van een regel ook correct werkt en niet alleen in het midden. Welke edge case zinvol is hangt af van de reguliere expressie.

## Strings

In de volgende opgaven ga je op zoek naar **strings** die matchen. De input is een bestand met tekst, eventueel met meerdere regels, en de output zijn de losse strings (delen) die matchen. Hiervoor gebruik je normaal de optie `-o` van `grep`. Je kunt deze ook combineren met de optie `-w` om alleen strings te matchen die een heel woord zijn.

1.  Geef een compleet grep-commando waarmee je elke string selecteert die bestaat uit het woord `we`. Geef een aantal voorbeeldteksten met matchen en markeer duidelijk welke delen een match zijn. Kijk zoals altijd naar edge cases en geef ook teksten die geen matches bevatten.

2.  Geef een compleet grep-commando waarmee je elke string selecteert die begint met "Wachtwoord" en eindigt met een viercijferig getal. Hoofd- of kleine letters mogen allebei. Geef een aantal voorbeeldteksten met matchen en markeer duidelijk welke delen een match zijn. Kijk zoals altijd naar edge cases en geef ook teksten die geen matches bevatten.

3.  Geef een compleet grep-commando waarmee je elk woord selecteert dat met `A`, `D` of `W` begint. Geef een aantal voorbeeldteksten met matchen en markeer duidelijk welke delen een match zijn. Kijk zoals altijd naar edge cases en geef ook teksten die geen matches bevatten.

4.  Geef een compleet grep-commando waarmee je elk woord selecteert waarin een `o` staat gevolgd door één of meer `r`. Geef een aantal voorbeeldteksten met matchen en markeer duidelijk welke delen een match zijn. Kijk zoals altijd naar edge cases en geef ook teksten die geen matches bevatten.
