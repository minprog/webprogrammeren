# Oefeningen

Deze vragen zijn goede oefeningen voor toetsje en tentamen. Je hebt parate kennis nodig van Pandas en de operaties die je kunt uitvoeren op Dataframes en Series. Als je merkt dat je deze kennis nog niet echt paraat hebt, dan kun je extra studeren met hulp van de Notebook of externe bronnen over Pandas.

Onderstaande vragen zijn *grotendeels* representatief voor de vragen die je op het tentamen tegen zou kunnen komen. Je zult DataFrames en Series moeten produceren met hulp van Pandas-functionaliteit.

## Vragen

1.  De Dataframe `grades` ziet er zo uit:

             student_name    course_name  grade
        0          Pascal  Programming 2    7.0
        1           Morty  Programming 1    5.5
        2  Slartibartfast  Programming 1    6.5
        3          Ursula  Programming 1    9.5
        4           Morty  Programming 2    3.5
        5           Marge  Programming 1    8.0
        6          Ursula  Programming 2    9.0

    Geef een statement om het gemiddelde cijfer van alle studenten uit te rekenen en in aflopende volgorde te sorteren. De gewenste uitvoer:

        student_name
        Ursula            9.25
        Marge             8.00
        Pascal            7.00
        Slartibartfast    6.50
        Morty             4.50

2.  De variabele `groups` bevat een gegroepeerde versie van dezelfde data:

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

    Geef een statement om op basis van de variabele `groups` het gemiddelde cijfer uit te rekenen voor elk van beide vakken. De gewenste uitvoer:

        course_name
        Programming 1    7.375
        Programming 2    6.500

3.  We geven een variabele `series_a` met de cijfers van Programmeren 1, geindexeerd op naam.

        student_name
        Morty             5.5
        Slartibartfast    6.5
        Ursula            9.5
        Marge             8.0

    En een variabele `series_b` met de cijfers van Programmeren 2, geindexeerd op naam.

        student_name
        Pascal    7.0
        Morty     3.5
        Ursula    9.0

    Geef een statement om `series_a` af te trekken van `series_b`, om het verschil in cijfers te zien. Zorg ervoor dat alleen die studenten blijven staan die voor beide vakken een cijfer hebben. Er mogen dus geen NaN-waarden in het resultaat overblijven. De gewenste uitvoer:

        student_name
        Morty     2.0
        Ursula    0.5

4.  Schrijf een statement op basis van `series_a` dat de studenten selecteert die een cijfer hebben gehaald van 7.0 of hoger. De gewenste uitvoer:

        student_name
        Ursula            9.5
        Marge             8.0

(Deze oefening is **niet** gegenereerd met ChatGPT.)
