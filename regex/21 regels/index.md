# Reguliere expressies

Beantwoord de vragen hieronder.

Als je testbestanden maakt voor de opdrachten, doe dat dan niet in Windows met Notepad of Atom. Gebruik in plaats daarvan `nano` (zoals uitgelegd in de Software Carpentry workshop). Dan zijn de line endings correct voor gebruik van `grep`. Als je er technisch niet uitkomt, vraag dan ook hulp!

## Opdracht

Voor deze opdrachten moet je reguliere expressies schrijven en voorbeelden geven die wél en niet werken. Je moet hiervoor `grep`, `egrep` of `fgrep` gebruiken zoals in het boek beschreven. Gebruik de UNIX manual pages op jouw systeem om te juiste opties (flags) te vinden die je nodig hebt.

Er wordt hieronder ook gevraagd naar **edge cases**. Dit zijn de voorbeelden waar je het uiterste vraagt van de reguliere expressie. Stel dat je een commando moet geven om alle woorden met een letter `a` erin te vinden; dan wil je zeker checken of een woord met daarin alleen de letter `a` (en niets anders) ook correct matcht. In sommige gevallen kan het zinvol zijn om te kijken of een match aan het begin of eind van een regel ook correct werkt en niet alleen in het midden. Welke edge case zinvol is hangt af van de reguliere expressie.

## Regels

In de volgende opgaven ga je op zoek naar **regels** die matchen. De input is een bestand met meerdere regels en de output zijn de regels (zinnen) waarin een match voorkomt. Dit is een standaard-gebruik van `grep` zoals in het boek ook steeds wordt getoond.

1.  Geef een compleet grep-commando waarmee je elke regel selecteert waar aan het eind van de regel een punt (`.`) staat. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

2.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin de string `the` (of `The`) staat. `There is nothing.` moet ook matchen. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

3.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin het woord (dus niet de string) `we` staat. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

4.  Geef een compleet grep-commando waarmee je elke regel selecteert die met `A`, `D` of `W` begint. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

5.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin een `o` staat gevolgd door één of meer `r`. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.

6.  Geef een compleet grep-commando waarmee je elke regel selecteert waarin een vraagteken óf een backslash staan. Geef een aantal voorbeeldzinnen die matchen en een aantal zinnen die niet matchen, waaronder edge cases.
