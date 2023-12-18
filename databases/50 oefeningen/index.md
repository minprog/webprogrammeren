# Oefeningen SQL

Bij het toetsje en het tentamen kun je vragen verwachten op basis van de jou al bekende Movies-database. Je schrijft je antwoorden op papier en hebt verder geen toegang tot naslagwerken.

Je hebt dus kennis nodig van SQL en wat de verschillende clausules (JOIN, WHERE, enzovoort) betekenen en waarvoor je ze gebruikt. Als je merkt dat je deze kennis nog niet echt paraat hebt, dan kun je extra studeren met hulp van het videocollege of externe bronnen over SQL.

Onderstaande vragen zijn *grotendeels* representatief voor de vragen die je op het tentamen tegen zou kunnen komen, maar je zou ook vragen tegen kunnen komen die meer lijken op de vragen bij de [Movies-opdracht](/databases/movies) of varianten.

## Database

Voor de vragen gebruiken we de movies-database die je al kent. Hier is het schema:

    CREATE TABLE movies (
                        id INTEGER,
                        title TEXT NOT NULL,
                        year NUMERIC,
                        PRIMARY KEY(id)
                    );
    CREATE TABLE stars (
                    movie_id INTEGER NOT NULL,
                    person_id INTEGER NOT NULL,
                    FOREIGN KEY(movie_id) REFERENCES movies(id),
                    FOREIGN KEY(person_id) REFERENCES people(id)
                );
    CREATE TABLE directors (
                    movie_id INTEGER NOT NULL,
                    person_id INTEGER NOT NULL,
                    FOREIGN KEY(movie_id) REFERENCES movies(id),
                    FOREIGN KEY(person_id) REFERENCES people(id)
                );
    CREATE TABLE ratings (
                    movie_id INTEGER NOT NULL,
                    rating REAL NOT NULL,
                    votes INTEGER NOT NULL,
                    FOREIGN KEY(movie_id) REFERENCES movies(id)
                );
    CREATE TABLE people (
                    id INTEGER,
                    name TEXT NOT NULL,
                    birth NUMERIC,
                    PRIMARY KEY(id)
                );

## Vragen

1. Schrijf een SQL-query die de titel en het jaar van elke film geeft.

2. Schrijf een SQL-query die de namen geeft van alle acteurs in de film "Titanic" uit 1997.

3. Schrijf een SQL-query die de gemiddelde rating van alle films uit 2005 geeft. Gebruik JOINs en geen subquery.

4. Schrijf een SQL-query die de titels geeft van alle films gemaakt door een regisseur die geboren is in 1984.

5. Schrijf een SQL-query die het aantal films geeft waarin "Sandra Oh" speelt. Gebruik een subquery en geen JOINs.

6. Schrijf een SQL-query om de namen te selecteren van alle regisseurs die betrokken zijn bij de film "The Matrix" uit 1999. Gebruik een subquery en geen joins.

7. Schrijf een SQL-query die het aantal films selecteert die een rating hoger dan 8.5 hebben en meer dan 100 stemmen hebben ontvangen.

8. Schrijf een SQL-query om naam en de rating te selecteren van alle films waarin "Marouane Meftah" speelt (de rating is `ratings.rating`).

9. Schrijf een SQL-query om de namen van alle mensen te selecteren, gesorteerd op geboortejaar, die speelden in een film uit het jaar 2005. Gebruik JOINs en geen subquery.
