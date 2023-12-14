# Installatie

Tijdens dit vak ga je diverse opdrachten uitvoeren in een UNIX-omgeving.
UNIX is een systeem dat speciaal is bedacht voor het snel kunnen uitvoeren en combineren van allerlei tools die teksten verwerken. Dit hoeven niet per se geschreven teksten te zijn, maar het kan ook gaan om CSV-bestanden of andere datafiles.

Sommige besturingssystemen zijn direct gebaseerd op UNIX, namelijk Linux en macOS. Heb je zo'n systeem, dan hoef je alleen een "Terminal" te openen en je kunt UNIX-commando's invoeren.

Windows is juist niet gebaseerd op UNIX, maar op Windows is het mogelijk om "Git Bash" te installeren waarmee je eigenlijk precies zoals in UNIX kunt werken. Zo heb je dezelfde mogelijkheden als in Linux of macOS.

## macOS en Linux

1. Open de "Terminal". Deze staat tussen de programma's die al standaard geinstalleerd zijn. Weet je niet hoe dit moet, vraag dan om assistentie.

2. Je moet daarna nog de [bestanden van de tutorial](https://swcarpentry.github.io/shell-novice/data/shell-lesson-data.zip) downloaden. Zorg dat je deze zipfile uitpakt in een map in je homedirectory of "Documents"-directory.

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
