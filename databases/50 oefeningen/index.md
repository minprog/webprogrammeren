# Oefeningen

Deze vragen zijn goede oefeningen voor het tentamen.

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

3. Schrijf een SQL-query die de gemiddelde rating van alle films uit 2005 geeft.

4. Schrijf een SQL-query die de titels geeft van alle films gemaakt door een regisseur die geboren is in 1984.

5. Schrijf een SQL-query die het aantal films geeft waarin "Sandra Oh" speelt.
