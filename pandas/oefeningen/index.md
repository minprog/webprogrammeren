# Oefeningen

Deze vragen zijn goede oefeningen voor het tentamen. Onderstaande vragen zijn representatief voor de vragen die je op het tentamen tegen zou kunnen komen. De verwachting is dat je alle vragen op het tentamen correct beantwoordt, foutjes daargelaten. Je hebt dus parate kennis nodig van Pandas en de operaties die je kunt uitvoeren op Dataframes en Series. Als je merkt dat je deze kennis nog niet echt paraat hebt, dan kun je extra studeren met hulp van het de Notebook of externe bronnen over Pandas.

Je kunt onderstaande oefeningen niet inleveren en ze horen dus ook niet bij de deadline voor de Pandas-module.

## Database

Voor deze vragen gebruiken we een Dataframe uit de Pandas-notebook:

    grades = pd.DataFrame([["Pascal", "Programming 2", 7.0], ["Morty", "Programming 1", 5.5], 
                           ["Slartibartfast", "Programming 1", 6.5], ["Ursula", "Programming 1", 9.5],
                           ["Morty", "Programming 2", 3.5], ["Marge", "Programming 1", 8.0],
                           ["Ursula", "Programming 2", 9.0]], 
                           columns = ["student_name", "course_name", "grade"])

De Dataframe ziet er dan zo uit:

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

## Vragen

1. Maak een series-object waarin je het gemiddelde cijfer voor beide vakken weergeeft.
2. Morty en Ursula hebben beide vakken gevolgd, en gehaald. Maak een series-object waarin de gemiddelde cijfers van Morty en Ursula in aflopende volgorde staan.
3. Twee stappen:
    - Maak een series object waarin series_a = programming 1, series_b  = programming 2 series_c is None
    - Trek series_a af van series_b en sla de serie op als series_c, zorg ervoor dat alleen die studenten worden genomen die voor beide vakken een cijfer hebben. Er mogen geen NaN waarden staan in series_c

(Deze oefening is **niet** gegenereerd met ChatGPT.)
