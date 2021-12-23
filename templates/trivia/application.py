from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

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
db = SQL("sqlite:///trivia.db")


@app.route("/")
def index():
    """ Prompt a random trivia question """

    # Random question are retrieved from the api powered by Jservice
    # Visit https://jservice.io/ for more details
    res = requests.get("http://jservice.io/api/random")
    data = res.json()

    # Retrieve all relevant information about the question
    question = data[0]["question"]
    question_id = data[0]["id"]
    answer = data[0]["answer"]

    # Add information about the question to the database
    if not db.execute(f"SELECT * FROM questions wHERE question_id={question_id}"):
        db.execute("INSERT INTO questions (question_id, question, answer) VALUES (:question_id, :question, :answer)", question_id=question_id, question=question, answer=answer)

    # Print the answer to the question in the terminal
    print(answer)

    return render_template("index.html", question_id=question_id, question=question)


@app.route("/answer/<question_id>", methods={"POST"})
def answer(question_id):
    """ Check answer to question """

    # Retrieve the answer given by the user
    given_answer = request.form.get("answer")

    # Use information from database the check the given answer
    question = db.execute(f"SELECT * FROM questions WHERE question_id={question_id}")

    # Let the user know whether they were right or wrong
    if question[0]["answer"] == given_answer:
        return render_template("answer.html", answer="Correct, well done!")
    else:
        return render_template("answer.html", answer="Wrong, better luck next time.")


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