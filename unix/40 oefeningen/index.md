# Oefeningen

Deze vragen zijn goede oefeningen voor het tentamen. Op het tentamen zelf zul je minder vragen krijgen over UNIX, maar verwacht een mix van onderstaande. De verwachting is dat je alle vragen op het tentamen correct beantwoordt, foutjes daargelaten. Je hebt dus parate kennis nodig van de commando's en wat ze doen. Als je merkt dat je deze kennis nog niet echt paraat hebt, dan kun je extra studeren met hulp van de Software Carpentry-workshop.

De commando's die je moet kennen staan expliciet vermeld op de [pagina van de Software Carpentry workshop](/unix/carpentry).


## Behandelde commando's

Algemeen:

- man

Navigatie door directories:

- ls, ls --help, ls -F, ls -l, ls -h, ls -r, ls -t
- pwd
- cd, cd -, cd ..

Files en directories manipuleren:

- mkdir, mkdir -p
- touch
- mv
- cp, cp -r
- rm, rm -i, rm -r

Data processing:

- wc, wc -l
- sort, sort -n, sort -r
- head, head -n
- echo
- tail, tail -n
- cut, cut -d, cut -f
- uniq, uniq -c
- cat

Daarnaast is het voor UNIX nodig om te weten:

- hoe paths werken (van files en directories)
- hoe wildcards werken
- hoe pipes en redirects werken


## Vragen over commando's

Beantwoord de volgende vragen. Geef altijd een concreet en compleet commando. Als er geen file- of directorynaam is opgegeven moet je zelf een naam verzinnen.

1. Wat is het commando om de man-pagina van een bepaald programma te openen in de terminal?
1. Welk commando gebruik je om de inhoud van een map weer te geven, inclusief datum en grootte?
1. Wat is het commando om de huidige locatie in het bestandssysteem weer te geven?
1. Hoe verander je de huidige locatie naar een andere map?
1. Wat is het commando om een nieuwe map aan te maken in de huidige locatie?
1. Hoe maak je een nieuw leeg bestand aan met de naam `gegevens.dat`?
1. Hoe verplaats je een bestand naar de directory `data` met het mv-commando?
1. Wat is het commando om hele map te kopiëren naar een andere locatie?
1. Hoe verwijder je een bestand?

## Opgaven met one-liners

Gegeven dit bestand:

    apple
    banana
    cherry
    apple
    date
    fig
    banana
    grape
    apple
    date

Geef one-liners voor de volgende opdrachten:

1. Count the number of occurrences of each unique word in the file.
2. Display the last 5 lines of the file.
3. Display the first 3 lines of the file.
4. Display the unique words in the file in alphabetical order.
5. Display the number of lines in the file.
6. Count the number of occurrences of each unique word in the file, ignoring any spaces.
7. Display the unique words in the file in order of most to least common.
8. Display the 3 most common words in the file.
9. Display the 3 least common words in the file.

## One-liners deel 2

Gegeven dit bestand:

    John, 25, New York
    Mary, 32, Los Angeles
    Mike, 19, Chicago
    Jane, 27, New York
    Steve, 22, Chicago

Geef one-liners voor de volgende opdrachten:

1. Sort the contents of the file alphabetically by the first column.
2. Display only the first column of the file (the names).
3. Display only the third column of the file (cities) and show only unique values.
4. Create a new file with the first 3 lines of `example.txt`.
5. Show the second column of the file (ages) in numerical order.

(Deze oefeningen zijn gegenereerd met ChatGPT.)
