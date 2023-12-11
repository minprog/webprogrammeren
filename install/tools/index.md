# Tools installeren voor de shell

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
