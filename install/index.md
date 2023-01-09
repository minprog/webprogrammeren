# Installatie voor Web + Data

Tijdens dit vak ga je diverse opdrachten uitvoeren in een UNIX-omgeving.
UNIX is een systeem dat speciaal is bedacht voor het snel kunnen uitvoeren en combineren van allerlei tools die teksten verwerken. Dit hoeven niet per se geschreven teksten te zijn, maar het kan ook gaan om CSV-bestanden of andere datafiles.

Sommige besturingssystemen zijn direct gebaseerd op UNIX, namelijk Linux en macOS. Heb je zo'n systeem, dan hoef je alleen een "Terminal" te openen en je kunt UNIX-commando's invoeren.

Windows is juist niet gebaseerd op UNIX, maar op Windows is het mogelijk om "Git Bash" te installeren waarmee je eigenlijk precies zoals in UNIX kunt werken. Zo heb je vrijwel precies dezelfde mogelijkheden als in Linux of macOS.

## macOS en Linux

Open de "Terminal". Deze staat tussen de programma's die al standaard geinstalleerd zijn. Ga daarna naar het kopje "Tools installeren" hieronder.

## Windows

1. Installeer eerst Windows Terminal door [deze link te volgen](https://aka.ms/terminal). Je hoeft het programma nog niet op te starten.

2. Installeer Git Bash door [deze link te volgen](https://git-scm.com/download/win). Normaal kun je de 64-bit installer downloaden, maar heel misschien werkt dat niet en moet je de 32-bit downloaden.

    - Start de installer door het gedownloade programma te klikken (Git-2.39.0.2-64-bit.exe).
    
    - **Klik bij de opties van Select Components op "(NEW) Add a Git Bash Profile to Windows Terminal".**
    
    - Als je een editor mag kiezen, selecteer dan **Nano**.
    
    - Alle andere opties kun je zo laten.
    
3. Start Windows Terminal (eerst sluiten als je 'm toch al geopend had) en open een "Git Bash"-tabblad.

    ![git bash](gitbash.png)

## Tools installeren

Nadat je toegang hebt gekregen tot een goedwerkende terminal voor UNIX-commando's kun je het volgende commando copy-pasten en uitvoeren door op ENTER te drukken.

Hiermee wordt een script gedownload dat twee tools installeert voor opdrachten later in de cursus.

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/uvapl/installer/main/run.sh)"

Dit script werkt niet op Linux.

Het script installeert de tools [pup](https://github.com/ericchiang/pup) en [SQLite](https://www.sqlite.org/index.html) zodat je deze in de terminal kunt gebruiken.

Als het script is afgelopen zou je `sqlite3` moeten kunnen opstarten door dit commando te geven:

    sqlite3

Dan verschijnt zo'n soort melding:

    SQLite version 3.39.5 2022-10-14 20:58:05
    Enter ".help" for usage hints.
    Connected to a transient in-memory database.
    Use ".open FILENAME" to reopen on a persistent database.
    sqlite> 

Je bent dan "in" sqlite waarmee je databases kunt openen en queries schrijven (maar daarover veel meer in een volgende module!).

Geef het commando `.quit` om uit SQLite te gaan (vergeet de `.` niet!).
