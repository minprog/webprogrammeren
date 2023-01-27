# Oefeningen

Deze vragen zijn goede oefeningen voor het tentamen. De verwachting is dat je alle vragen op het tentamen correct beantwoordt, foutjes daargelaten. Je hebt dus parate kennis nodig van Pandas en de operaties die je kunt uitvoeren op Dataframes en Series. Als je merkt dat je deze kennis nog niet echt paraat hebt, dan kun je extra studeren met hulp van het de Notebook of externe bronnen over Pandas.

Je kunt onderstaande oefeningen niet inleveren en ze horen dus ook niet bij de deadline voor de Pandas-module.

Onderstaande vragen zijn *grotendeels* representatief voor de vragen die je op het tentamen tegen zou kunnen komen. Je zult DataFrames en Series moeten produceren met hulp van Panda's-functionaliteit.

## Database

Voor deze vragen gebruiken we een Dataframe uit de Pandas-notebook:

    grades = pd.DataFrame([["Pascal", "Programming 2", 7.0], ["Morty", "Programming 1", 5.5], 
                           ["Slartibartfast", "Programming 1", 6.5], ["Ursula", "Programming 1", 9.5],
                           ["Morty", "Programming 2", 3.5], ["Marge", "Programming 1", 8.0],
                           ["Ursula", "Programming 2", 9.0]], 
                           columns = ["student_name", "course_name", "grade"])

De Dataframe `grades` ziet er dan zo uit:

         student_name    course_name  grade
    0          Pascal  Programming 2    7.0
    1           Morty  Programming 1    5.5
    2  Slartibartfast  Programming 1    6.5
    3          Ursula  Programming 1    9.5
    4           Morty  Programming 2    3.5
    5           Marge  Programming 1    8.0
    6          Ursula  Programming 2    9.0

En de variabele `groups` bevat een gegroepeerde versie:

    Programming 1
         student_name    course_name  grade
    1           Morty  Programming 1    5.5
    2  Slartibartfast  Programming 1    6.5
    3          Ursula  Programming 1    9.5
    5           Marge  Programming 1    8.0

    Programming 2
      student_name    course_name  grade
    0       Pascal  Programming 2    7.0
    4        Morty  Programming 2    3.5
    6       Ursula  Programming 2    9.0

Een variabele `series_a` met de cijfers van Programmeren 1, geindexeerd op naam.

    student_name
    Morty             5.5
    Slartibartfast    6.5
    Ursula            9.5
    Marge             8.0

En een `series_b` met de cijfers van Programmeren 2, geindexeerd op naam.

    student_name
    Pascal    7.0
    Morty     3.5
    Ursula    9.0


## Vragen

Gebruik bij deze vragen de bovenstaande variabelen `grades` en `groups`.

1.  Schrijf een statement om een `DataFrame`-object te maken met het gemiddelde cijfer voor elk van beide vakken.

        course_name
        Programming 1    7.375
        Programming 2    6.500

2.  Morty en Ursula hebben beide vakken gevolgd, en gehaald. Maak een `Series`-object waarin het gemiddelde cijfer van elk van deze twee studenten in aflopende volgorde staat.

        student_name
        Ursula    9.25
        Morty     4.50

3.  Trek `series_a` af van `series_b` om het verschil in cijfers te zien. Zorg ervoor dat alleen die studenten blijven staan die voor beide vakken een cijfer hebben. Er mogen dus geen NaN-waarden in het resultaat overblijven.

        student_name
        Morty     2.0
        Ursula    0.5

4.  Schrijf een statement op basis van `series_b` om het hoogste cijfer voor Programmeren 2 te berekenen (9.0).

5.  Schrijf een statement op basis van `series_a` dat de studenten geeft die een cijfer hebben gehaald van 7.0.

        student_name
        Ursula            9.5
        Marge             8.0

(Deze oefening is **niet** gegenereerd met ChatGPT.)
