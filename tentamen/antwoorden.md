# Tentamen

Webprogrammeren en Databases IK  
vrijdag 3 februari 2022 12:00–14:00  

## 1. UNIX

**Basisvragen**

1.1. Welk commando kun je gebruiken om de inhoud van de map `/Downloads` te tonen met alle attributen erbij zoals de grootte van de bestanden?

    ls -l

1.2. Hoe kun je een bestand `logfile.txt` aanmaken met een enkel commando?

    touch logfile.txt  (nano is niet echt een correct antwoord)

1.3. Hoe kun je een bestand `logfile.txt` kopiëren naar de map `/Downloads` met een enkel commando?

    cp logfile.txt /Downloads

**Tekstmanipulatie**

Gegeven is de tekstfile `namen.txt` (deze naam moet terugkomen in de commando's hieronder):

    John Smith
    Jane Doe
    Bob Johnson
    John Smith
    Mary Johnson
    Jane Doe

1.4. Schrijf een one-liner om de eerste drie regels van het bestand te selecteren.

    head -n 3 namen.txt  OF  head -3 namen.txt  OF  cat namen.txt | head -n3

1.5. Schrijf een one-liner om het aantal regels in het tekstbestand te tellen en weer te geven (en niks anders).

    wc -l namen.txt

1.6. Schrijf een one-liner om de namen uniek te maken en die op te slaan in `unieke_namen.txt`.

    cat namen.txt | sort | uniq > unieke_namen.txt

1.7. Schrijf een one-liner die de namen sorteert en dan de laatste (onderste) naam geeft.

    cat namen.txt | sort | tail -n 1

1.8. Schrijf een one-liner die alleen de voornamen geeft, maar elke voornaam wel maximaal 1x. Gebruik het feit dat voor- en achternaam gescheiden zijn door een enkele spatie. Als je een spatie wil opgeven in een commando kun je `" "` gebruiken.

    cat namen.txt | cut -d" " -f1 | sort | uniq

## 2. Regexes

Gegeven is de volgende ChatGPT-poëzie:

    0 Winter, een tijd van stilte en verdriet,
    1 Met sneeuw bedekte bomen, als een doodskleed geweven.
    2 De koude wind die blaast door de straten,
    3 Een bevroren wereld, verstild en verlaten.
    4 De zon verdwijnt vroeg achter de horizon,
    5 De nacht wordt langer, het daglicht verdwijnt.
    6 In deze stille tijd, wordt het hart geroerd,
    7 Door de herinneringen aan de zomer, voorbij en verloren.
    8 Maar de winter heeft ook schoonheid,
    9 In de besneeuwde bossen en de heldere nachten.

Geef hieronder UNIX-onliners gebaseerd op een variant van `grep`.

2.1. Geef een commando om alle **regels** te selecteren waarin het woord "winter" staat, onafhankelijk van hoofdlettergebruik. De uitvoer bestaat uit regels 0 en 8.

    grep -wi "winter" poezie.txt

2.2. Geef een commando om alle **regels** te selecteren waarin het woord "de" staat, onafhankelijk van hoofdlettergebruik. Het woord "deze" mag niet gematcht worden. De uitvoer bestaat uit regels 2, 4, 5, 7, 8, 9 maar niet regel 6. (Op tentamen stond regel 5 er niet bij, dit zal geen invloed hebben gehad op de juiste interpretatie.)

    cat poezie.txt | grep -wi "de"

2.3. Geef een commando om alle **woorden** te selecteren die eindigen op een komma. De uitvoer begint met:

    Winter,
    verdriet,
    bomen,

    cat poezie.txt | grep -wo "\w*,"

2.4. Geef een commando om alle **woorden** te selecteren die aan het begin van de regel staan (de regelnummers horen niet tot het bestand, dus die mag je negeren!). De uitvoer begint met:

    Winter
    Met
    De

    cat poezie.txt | grep -o "^\w*"

2.5. Geef een commando om alle **woorden** te selecteren die beginnen met een letter "v", daarna een klinker (a, e, i, o, u, y). De rest van het woord maakt niet uit. De uitvoer begint met:

    van
    verdriet
    verstild

    cat poezie.txt | grep -o "v[aeiouy]\w*"

## 3. SQL

Gegeven is de movies-database uit de opdracht. Dit is het database-schema:

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

Voor de volgende vragen moet je SQL-queries schrijven. De queries moeten precies zo specifiek zijn als wordt gevraagd, dus je mag geen shortcuts nemen op basis van jouw kennis van films en antwoorden.

Vergeet ook niet om te laten zien dat je een JOIN kunt schrijven.

3.1. Schrijf een SQL-query om de namen te selecteren van alle regisseurs die betrokken zijn bij de film 'The Matrix' uit 1999.

    select name from people
    inner join directors on people.id = directors.person_id
    inner join movies on movies.id = directors.movie_id
    where title = "The Matrix";

3.2. Schrijf een SQL-query die het aantal films selecteert die een rating hoger dan 8.5 hebben en meer dan 100 stemmen hebben ontvangen.

    select count(movies.id) from movies
    inner join ratings on movies.id = ratings.movie_id
    where ratings.votes > 100 and ratings.rating > 8.5;

3.3. Schrijf een SQL-query om naam en de rating te selecteren van alle films waarin 'Marouane Meftah' speelt (de rating is `ratings.rating`).

    select name, rating from movies
    inner join stars on movies.id = stars.movie_id
    inner join people on people.id = stars.person_id
    inner join ratings on movies.id = ratings.movie_id
    where people.name = "Marouane Meftah";

3.4. Schrijf een SQL-query om de namen van alle mensen te selecteren, gesorteerd op geboortejaar, die speelden in een film uit het jaar 2005.

    select name from people
    inner join stars on people.id = stars.person_id
    inner join movies on movies.id = stars.movie_id
    where year = 2005
    order by birth;

    (Er stond niet bij of het oplopend of aflopend gesorteerd moet worden, dus alleen "order by" is de oplossing.)

## 4. Pandas

Bij deze opgaven zijn we op zoek naar aanwijzingen dat je de basis van Pandas goed beheerst. Gebruik dus geen standaard Python-constructies zoals for-loops.

Gegeven is de Skittles-dataframe die er zo uitziet (de variabelenaam is `skittles`):

![](skittles.png)

4.1. Schrijf een regel code om een kolom toe te voegen met de naam `score` waarvan de waarde steeds de `amount` x de `rating` is.

    skittles['score'] = skittles['amount'] * skittles['rating']

4.2. Schrijf een regel code die de totale `score` van de collectie uitrekent.

    skittles['worth'].sum()

4.3. Schrijf een regel code die alleen de rijen `red` en `green` opslaat in een nieuwe dataframe.

    nieuwe_df = skittles.loc[['red', 'green']]

4.4. Schrijf een regel code die de data sorteert op rating en opslaat in een nieuwe dataframe.

    skittles_sorted = skittles.sort_values(['rating'])

Gegeven is:

    words = Series(["foo", "Bar", "baz", "QUX", "QuUuX"])

4.5. Schrijf een regel code die met hulp van `str.isupper` de series `words` mapt naar een series van boolean waarden: 

    0    False
    1    False
    2    False
    3     True
    4    False
    dtype: bool

    words.map(str.isupper)

## 5. Scraping

Gegeven is het volgende HTML-document in `sample.html`:

    <!DOCTYPE html>
    <html>
    <head>
      <title>Sample HTML Document</title>
    </head>
    <body>
      <h1>Welcome to my website</h1>
      <div class="container">
        <p>Here is some text in a paragraph.</p>
        <ul>
          <li>Item 1</li>
          <li>Item 2</li>
          <li>Item 3</li>
        </ul>
        <div class="highlight">
            <p>Here is some highlighted text in a paragraph.</p>
            <p>Here is some more highlighted text in a paragraph.</p>
        </div>
      </div>
      <div class="footer">
        <p>Copyright © 2021</p>
      </div>
    </body>
    </html>

Geef **complete pup-commando's** om de volgende vragen te beantwoorden. Het document hierboven is vooral ter illustratie, om een goed beeld te vormen. Gebruik wel altijd selectors die net zo specifiek zijn als de vraag zegt!

5.1. Welke tekst staat in de eerste `<p>` tag in de eerste `<div>`?

    cat sample.html | pup "body > div:first-of-type > p:first-of-type text{}"

5.2. Welke tekst staat in de tweede `<li>` tag in de `<ul>`?

    cat sample.html | pup "ul li:nth-of-type(2) text{}"

5.3. Welke tekst staat in de `<p>` tags in de `<div class="highlight">`?

    cat sample.html | pup "div.highlight p text{}"

5.4. Welke tekst staat in de laatste `<p>` tag in de `<div class="footer">`?

    cat sample.html | pup "div.footer p:last-of-type text{}"

5.5. Welke tekst staat in de `<title>` tag?
    
    cat sample.html | pup "title text{}"
