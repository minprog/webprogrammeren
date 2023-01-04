# Fiftyville

Write SQL queries to solve a mystery.

## A Mystery in Fiftyville

The CS50 Duck has been stolen! The town of Fiftyville has called upon you to solve the mystery of the stolen duck. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. Your goal is to identify:

* Who the thief is,
* What city the thief escaped to, and
* Who the thief's accomplice is who helped them escape

All you know is that the theft **took place on July 28** and that it **took place on Chamberlin Street**.

How will you go about solving this mystery? The Fiftyville authorities have taken some of the town's records from around the time of the theft and prepared a SQLite database for you, `fiftyville.db`, which contains tables of data from around the town. You can query that table using SQL `SELECT` queries to access the data of interest to you. Using just the information in the database, your task is to solve the mystery.

## Getting Started

Download [fiftyville.zip](https://github.com/minprog/webprogrammeren/raw/2020/Problems/1%20Fiftyville/fiftyville.zip) and unzip.

## Specification

For this problem, equally as important as solving the mystery itself is the process that you use to solve the mystery. In `log.sql`, keep a log of all SQL queries that you run on the database. Above each query, label each with a comment (in SQL, comments are any lines that begin with `--`) describing why you're running the query and/or what information you're hoping to get out of that particular query.

You can use comments in the log file to add additional notes about your thought process as you solve the mystery: ultimately, this file should serve as evidence of the process you used to identify the thief!

In order to be able to assign points for your solution, make sure that you summarize in your own words the data that your collected and how your connected it to draw conclusions. Add this summary to the bottom of `log.sql`.

Once you solve the mystery, complete each of the lines in `answers.txt` by filling in the name of the thief, the city that the thief escaped to, and the name of the thief's accomplice who helped them escape town. (Be sure not to change any of the existing text in the file or to add any other lines to the file!)

Ultimately, you should submit both your `log.sql` (free-form and with summary of steps taken) and `answers.txt` (with exact solution).

## Database structure

    CREATE TABLE crime_scene_reports (
        id INTEGER,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        street TEXT,
        description TEXT,
        PRIMARY KEY(id)
    )
    CREATE TABLE interviews (
        id INTEGER,
        name TEXT,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        transcript TEXT,
        PRIMARY KEY(id)
    )
    CREATE TABLE courthouse_security_logs (
        id INTEGER,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        hour INTEGER,
        minute INTEGER,
        activity TEXT,
        license_plate TEXT,
        PRIMARY KEY(id)
    )
    CREATE TABLE atm_transactions (
        id INTEGER,
        account_number INTEGER,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        atm_location TEXT,
        transaction_type TEXT,
        amount INTEGER,
        PRIMARY KEY(id)
    )
    CREATE TABLE bank_accounts (
        account_number INTEGER,
        person_id INTEGER,
        creation_year INTEGER,
        FOREIGN KEY(person_id) REFERENCES people(id)
    )
    CREATE TABLE airports (
        id INTEGER,
        abbreviation TEXT,
        full_name TEXT,
        city TEXT,
        PRIMARY KEY(id)
    )
    CREATE TABLE flights (
        id INTEGER,
        origin_airport_id INTEGER,
        destination_airport_id INTEGER,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        hour INTEGER,
        minute INTEGER,
        PRIMARY KEY(id),
        FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
        FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
    )
    CREATE TABLE passengers (
        flight_id INTEGER,
        passport_number INTEGER,
        seat TEXT,
        FOREIGN KEY(flight_id) REFERENCES flights(id)
    )
    CREATE TABLE phone_calls (
        id INTEGER,
        caller TEXT,
        receiver TEXT,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        duration INTEGER,
        PRIMARY KEY(id)
    )
    CREATE TABLE people (
        id INTEGER,
        name TEXT,
        phone_number TEXT,
        passport_number INTEGER,
        license_plate TEXT,
        PRIMARY KEY(id)
    )

## Hints

*   You may find it helpful to start with the `crime_scene_reports` table. Start by looking for a crime scene report that matches the date and the location of the crime.

        SELECT description
        FROM crime_scene_reports
        WHERE month = 7 AND day = 28
        AND street = "Chamberlin Street";

*   See [this SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!

*   Then, as a strategy:

    *   Explore table schemas to understand what data is available and how tables connect to one another
    *   To query across multiple tables, nest queries together or join multiple tables together
    *   Maintain a list of suspects in your logfile
    *   Keep track of all queries in a log file, with notes

## Acknowledgements

Inspired by another case over at [SQL City](http://mystery.knightlab.com/).
