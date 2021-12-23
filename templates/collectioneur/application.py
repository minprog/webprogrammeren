from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from os import environ

import requests

from helpers import apology

# Configure application
app = Flask(__name__)

if __name__ == "__main__":
    app.run()

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///collectioneur.db")


@app.route("/")
def index():
    """ Display artwork page for The Night Watch """

    return redirect("/The+Night+Watch")


@app.route("/<artwork_title>", methods=["GET"])
def artwork(artwork_title):
    """ Retrieve information about an artwork, of which the title is given,
        display the information to the user """

    # Retrieve data from API
    # To use this API you need a key, you can learn how to get your key at https://data.rijksmuseum.nl/object-metadata/api/#access-to-apis
    # You can then set the API_KEY environment variable
    # DO NOT PUT YOUR API KEY IN THIS CODE
    api_key = environ['API_KEY']
    res = requests.get(f"https://www.rijksmuseum.nl/api/en/collection?key={api_key}&title={artwork_title}")
    data = res.json()

    # Check if any artwork with this name exists
    if not data["artObjects"]:
        return apology("there is no artwork with this name", 403)

    # Extract relevant information about the artwork
    image_url = data["artObjects"][0]["webImage"]["url"]
    title = data["artObjects"][0]["title"]
    artist = data["artObjects"][0]["principalOrFirstMaker"]

    return render_template("index.html", image_url=image_url, title=title, artist=artist)


@app.route("/search", methods=["POST"])
def search():
    """ Redirect to page that matches the artwork that the user searched for """

    title = request.form.get("query")
    return redirect(f"/{title}")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log user in """

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], (request.form.get("password"))):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register new user """

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")

        # Ensure password matches confirmation
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if password != confirmation:
            return apology("passwords don\'t match", 403)

        # Hash the password
        hash = generate_password_hash(password)

        # Attempt to create a new user
        try:
            user = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=username, hash=hash)
        except:
            return apology("username is already taken.", 403)

        # Remember user that is now logged in
        session["user_id"] = user

        return redirect("/")

    else:
        return render_template("register.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")