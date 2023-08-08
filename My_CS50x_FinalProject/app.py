import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import error, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

@app.route("/")
def home():
    """Homepage"""

    return render_template("home.html")

@app.route("/jobs")
def jobs():
    """Show available jobs"""
    # (we only use default get method here)

    # get info from DBs for our table
    dbinfo = db.execute("SELECT company, position, contact, date, location FROM jobs ORDER BY date DESC")

    return render_template("jobs.html", dbinfo=dbinfo)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return error("You must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return error("You must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return error("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username, password & confirmation was submitted
        if not username:
            return error("You must provide username")
        if not password:
            return error("You must provide password")
        if not confirmation:
            return error("Please confirm password")

        # Check if password contains uppercase, lowercase letter and digit
        if not any(char.islower() for char in password):
            return error("The password must contain at least one UPPERCASE LETTER, one LOWERCASE LETTER, and one DIGIT")
        if not any(char.isupper() for char in password):
            return error("The password must contain at least one UPPERCASE LETTER, one LOWERCASE LETTER, and one DIGIT")
        if not any(char.isdigit() for char in password):
            return error("The password must contain at least one UPPERCASE LETTER, one LOWERCASE LETTER, and one DIGIT")

        # Ensure confirmation matches password
        if password != confirmation:
            return error("The passwords do not match")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # If username already exists return error
        if len(rows) == 1:
            return error("This username is already used")

        # Create password hash and add new user to DB
        hash = generate_password_hash(password)

        new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

        # Log in user
        session["user_id"] = new_user

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("register.html")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """add new job"""
    # User reached route via POST
    if request.method == "POST":
        company = request.form.get("company")
        position = request.form.get("position")
        contact = request.form.get("contact")
        location = request.form.get("location")

        # get user id of actual user so we can work with user data in DB
        user_id = session["user_id"]

            # Ensure fields are not blank
        if not company:
            return error("Company field is blank")
        if not position:
            return error("Position field is blank")
        if not contact:
            return error("Contact field is blank")
        if not location:
            return error("Location field is blank")

        # Add job to DB
        db.execute("INSERT INTO jobs (user_id, company, position, contact, location, date) VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)", user_id, company, position, contact, location)

        # job added notification
        flash("Job successfully added!")

        # Redirect user to home page
        return redirect("/jobs")

    # User reached route via GET
    else:
        return render_template("add.html")

@app.route("/posted", methods=["GET", "POST"])
@login_required
def posted():
    """aposted jobs"""
     # get user id of actual user so we can work with user data in DB
    user_id = session["user_id"]

    if request.method == "POST":
        id = request.form.get('id')

        db.execute("DELETE FROM jobs WHERE id = ?", (id,))

        return redirect("/jobs")

    else:
        # get info from DBs for our table
        dbinfo = db.execute("SELECT company, position, contact, date, location, id FROM jobs WHERE user_id = ? ORDER BY date DESC", user_id)

        return render_template("posted.html", dbinfo=dbinfo)
