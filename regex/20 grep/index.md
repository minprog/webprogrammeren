# Het commando grep

Bij deze cursus ga je reguliere expressies gebruiken in het UNIX-commando `grep`. De standaard-manier van aanroepen ziet er zo uit:

    $ grep -E -i -o -w "regex" file.name

Je ziet de volgende onderdelen:

- `$` is de *prompt*. Dit is geen onderdeel van het commando, maar de UNIX-prompt waar je commando's kunt intikken. We zetten die neer zodat duidelijk is dat het om een voorbeeld gaat dat je in je terminal kunt intikken.

- `grep` is de *programmanaam*. We gebruiken altijd deze naam `grep`.

- `-E`, `-i`, `-o` en `-w` zijn *opties* voor grep. Hiermee kun je verschillende mogelijkheden instellen. De belangrijkste twee opties zijn de volgende:

    - `-E` is de optie om "extended regular expressions" te kunnen gebruiken. In het boek werd hier al naar verwezen. Sommige mogelijkheden, zoals het gebruik van haakjes `()`, werken niet zonder de optie `-E`. Je mag deze optie altijd gebruiken.
    
    - `-i` is de optie om *hoofdletteronafhankelijk* te zoeken. Als je in de reguliere expressie een letter gebruikt, bijvoorbeeld `A`, dan wordt zowel de kleine `a` als de grote `A` gematcht. Gebruik je deze optie niet, dan wordt alleen precies het teken gematcht dat je in de regex gebruikt.

- `"regex"` is de *reguliere expressie*. Je hebt hier al mee geoefend op de vorige pagina. Voor het commando `grep` zet je de regex altijd tussen aanhalingstekens `""` zodat de shell niet probeert de speciale tekens te begrijpen, maar de regex ongewijzigd doorgeeft aan het commando `grep`.

- `file.name` is de *bestandsnaam* van het bestand waarin je wil zoeken.
