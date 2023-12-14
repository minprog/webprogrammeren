# Installatie

Tijdens dit vak ga je diverse opdrachten uitvoeren in een UNIX-omgeving.
UNIX is een systeem dat speciaal is bedacht voor het snel kunnen uitvoeren en combineren van allerlei tools die teksten verwerken. Dit hoeven niet per se geschreven teksten te zijn, maar het kan ook gaan om CSV-bestanden of andere datafiles.

Sommige besturingssystemen zijn direct gebaseerd op UNIX, namelijk Linux en macOS. Heb je zo'n systeem, dan hoef je alleen een "Terminal" te openen en je kunt UNIX-commando's invoeren.

Windows is juist niet gebaseerd op UNIX, maar op Windows is het mogelijk om "Git Bash" te installeren waarmee je eigenlijk precies zoals in UNIX kunt werken. Zo heb je dezelfde mogelijkheden als in Linux of macOS.

## macOS en Linux

1. Open de "Terminal". Deze staat tussen de programma's die al standaard geinstalleerd zijn. Weet je niet hoe dit moet, vraag dan om assistentie.

2. Je moet daarna nog de [bestanden van de tutorial](https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip) downloaden. Zorg dat je deze zipfile uitpakt in een map in je homedirectory of "Documents"-directory.

3. Ga naar "Verdere tools installeren voor de shell" hieronder.

## Windows

1. Installeer eerst Windows Terminal door [deze link te volgen](https://aka.ms/terminal). Je hoeft het programma nog niet op te starten.

2. Installeer Git Bash door [deze link te volgen](https://git-scm.com/download/win). Normaal kun je de 64-bit installer downloaden, maar heel misschien werkt dat niet en moet je de 32-bit downloaden.

    - Start de installer door het gedownloade programma te klikken (Git-2.39.0.2-64-bit.exe).

    - **Klik bij de opties van Select Components op "(NEW) Add a Git Bash Profile to Windows Terminal".**

    - Als je een editor mag kiezen, selecteer dan **Nano**.

    - Alle andere opties kun je zo laten.

3. Stel je "User profile directory" in voor Git Bash:

    - Open de command prompt (Open het startmenu, tik `cmd` en dan Enter)

    - Geef het commando `setx HOME "%USERPROFILE%"` en druk Enter (zorg dat je het heel precies overneemt).
    
    - Er moet geprint worden: `SUCCESS: Specified value was saved.`

4. Start Windows Terminal (eerst sluiten als je 'm toch al geopend had) en open een "Git Bash"-tabblad.

    ![git bash](gitbash.png)

5. Je moet daarna nog de [bestanden van de tutorial](https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip) downloaden. Zorg dat je deze zipfile uitpakt in een map in je homedirectory of "Documents"-directory.

6. Ga naar "Verdere tools installeren voor de shell" hieronder.

## Verdere tools installeren voor de shell

Om enkele extra tools te installeren kun je het commando hieronder kopiëren en plakken je terminal.

Hiermee wordt een script gedownload dat twee tools installeert voor opdrachten die hierna volgen.

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/uvapl/installer/main/web.sh)"

Let op: dit script werkt niet op Linux. Gebruik je Linux, vraag dan om hulp.

Het script installeert de tools [pup](https://github.com/ericchiang/pup) en [SQLite](https://www.sqlite.org/index.html) zodat je deze in de terminal kunt gebruiken.

Als het script is afgelopen zou je `pup` moeten kunnen opstarten door dit commando te geven:

    pup --help

Dan verschijnt zo'n soort melding:

    Usage
        pup [flags] [selectors] [optional display function]
    Version
        0.4.0
    Flags
        -c --color         print result with color
        -f --file          file to read from
        -h --help          display this help
        -i --indent        number of spaces to use for indent or character
        -n --number        print number of elements selected
        -l --limit         restrict number of levels printed
        -p --plain         don't escape html
        --pre              preserve preformatted text
        --charset          specify the charset for pup to use
        --version          display version

Als dat bij jou ook zo is ben je helemaal klaar. Mocht het niet lukken, vraag dan hulp voordat je verder gaat!
