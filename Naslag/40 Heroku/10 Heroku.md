# Zet je website online met Heroku

Nu je zelf een webite gemaakt wil je die ook met de rest van de wereld delen. Gelukkig hoef je hiervoor niet zelf een server neer te zetten. De webapplicatie kan gehost worden op Heroku!

Heroku is een cloudplatform waarop je zelf een webapplicatie kan hosten.   Alternatieven zijn [Google Cloud Platform's App Engine](https://cloud.google.com/appengine), [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) of [Azure App Service](https://azure.microsoft.com/en-us/services/app-service/)

### Wat werkt niet op Heroku

- File uploads (bestanden en afbeeldingen opslaan in een map)

## Flask app klaarmaken voor Heroku

Voordat we onze applicatie op Heroku kunnen zetten moeten we onze applicatie geschikt maken voor Heroku.


### `requirements.txt`

Heroku moet weten welke Python-packages nodig zijn voor het draaien van jouw applicatie, je moet er voor zorgen dat alle packages die nodig zijn in `requirements.txt` staan.

> Het is belangrijk dat je packages noemt bij de naam die je gebruik bij het installeren en niet bij het importeren. _Flask Session_ importeer je bijvoorbeeld met `import flask_session`, maar installeer je met `pip install flask-session`. In dit geval voeg je dus `flask-session` toe aan `requirements.txt`.

Naast alle packages die je zelf al gebruikt hebt voeg je de volgende twee packages toe aan `requirements.txt`:

    gunicorn
    psycopg2

[Gunicorn](https://azure.microsoft.com/en-us/services/app-service/) is een "Python WSGI HTTP Server". Omdat `flask run` alleen geschikt is voor gebruik tijdens ontwikkeling gebruiken we voor het echt online zetten een andere server.

[Psycopg](https://www.psycopg.org) is een PostgreSQL adapter. Flask heeft dit nodig zodat het met een PostgreSQL-database kan communiceren.


### `Procfile` aanmaken

Vervolgens moeten we aan Heroku vertellen wat er uitgevoerd moet worden bij het om jouw applicatie te kunnen draaien, de informatie hierover staat in `Procfile`.

Begin met het aanmaken van een `Procfile`, dit kan vanuit de terminal bijvoorbeeld met `touch Procfile`.

In de `Procfile` zet je de volgende regel:

    web: gunicorn -w 1 application:app


### Aanpassingen in `application.py`

In `application.py` moeten we een aantal dingen aanpassen.

Voeg `import os` toe aan de imports bovenaan.

Verander de regel:

    db = SQL("sqlite:///finance.db")

naar:

    db = SQL(os.env.getenv("DATABASE_URL", "sqlite:///finance.db"))

Dit zorgt ervoor dat Heroku de juiste database kan vinden.

Het stuk:

    # Ensure templates are auto-reloaded
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # Ensure responses aren't cached
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

Kan je weghalen.


#### Secret Key

Voor extra veiligheid moet je een secretkey toevoegen aan je applicatie.
Met:

    python -c 'import os; print(os.urandom(16))'

Kan je die genereren. Vervolgens kan je deze toevoegen aan `application.py`:

    app.config["SECRET_KEY"] = <key>

Zet deze regel onder `app = Flask(__name__)`.


## Heroku-app en Database

Begin met het maken van een account op [Heroku](https://signup.heroku.com). Maak vervolgens een [nieuwe app](https://dashboard.heroku.com/new-app) aan. Bij app-naam vul je de naam van je app in. Bij region kies je voor _Europe_.

> Je app is later bereikbaar via app-name.herokuapp.com

Op het tabblad _Resources_ kan je de add-on _Heroku Postgres_ toevoegen aan de app. Kies voor het _Hobby Dev - Free_ plan.

> PostgreSQL is een databaseserver. We kunnen op Heroku geen gebruik meer maken van SQLite zoals we lokaal wel konden.

Open de add-on, navigeer naar het tabblad _Settings_ en klik op _View Credentials…_, met deze gegeven kan je op je database inloggen op [Adminer](https://adminer.cs50.net).

> Wat phpLiteAdmin is voor SQLite is Adminer voor PostgreSQL, het werkt vrijwel op dezelfde manier.

De database is nog helemaal leeg, nu kan je alle tabellen opnieuw aanmaken. Weet je niet meer wat welke tabellen je had aangemaakt? Open met `sqlite3 finance.db` je database. Met `.schema` kan je vervolgens printen hoe de database aangemaakt kan worden.

## Uitrollen naar Heroku

Je gaat je applicatie nu uitrollen naar Heroku, hiervoor heb je de Heroku CLI nodig. Installatie-instructies vind je [hier](https://devcenter.heroku.com/articles/heroku-cli).

Na het installeren kan je inloggen met `heroku login`. Werkt dit niet? Start de terminal dan even opnieuw op.

Ga vervolgens naar jouw applicatie op het [Heroku Dashbord](https://dashboard.heroku.com). Ga naar het tabblad _Deploy_ en scrol helemaal naar onder. Onder het kopje _Existing Git repository_ vindt je terug hoe je jouw git-repository kan koppelen aan Heroku.

Nu kan je met:

    git push heroku main

Pushen naar heroku, je ziet hier het hele uitrolprocess. Kijk goed of je hier foutmeldingen langs ziet komen!

> Zorg er wel voor dat je de laatste wijzigingen gecommit hebt!

Als alles goed is gegaan kan je jouw webapplicatie nu vinden op `https://<app-name>.herokuapp.com/`.

## Problemen oplossen

Lukt het niet in één keer? Geen zorgen, het lukt bijna nooit de éérste keer!
Met `heroku logs --tail` kan je de Python logs inzien. Vaak mis je een package, deze kan je dan toevoegen aan `requirements.txt`.
Vervolgens maak je een nieuwe commit en push je opnieuw.

### API-keys

Heb je API-keys die je eerst invoerde met `export`? Op het Dashboard kan je deze toevoegen onder Settings -> Config Vars.
