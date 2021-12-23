from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

import requests

from helpers import apology, login_required

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
db = SQL("sqlite:///photo_sharing.db")


@app.route("/")
def index():
    """ Display all posts from all users """

    posts = db.execute("SELECT * FROM posts")
    return render_template("index.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """ Create a new post """

    if request.method == "POST":
        # Ensure an image was included
        if not request.files["image"]:
            return apology("must provide an image", 403)

        # Collect user input
        file = request.files["image"]
        filename = file.filename
        text = request.form.get("text")

        # Create new post in database
        # The image is stored in the database through saving its name
        post = db.execute("INSERT INTO posts (image_name, text, user_id) VALUES (:image, :text, :user_id)", image=filename, text=text, user_id=session["user_id"])

        # Save image file in images folder
        request.files["image"].save(f"static/images/{filename}")

        return redirect("/")
    else:
        return render_template("create.html")


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