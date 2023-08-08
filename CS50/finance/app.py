import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # (we only use default get method here)
    # get user id of actual user so we can work with user data in DB
    user_id = session["user_id"]

    # get info from DBs for our table
    dbinfo = db.execute("SELECT symbol, SUM(shares) AS shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", user_id)
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    return render_template("index.html", dbinfo=dbinfo, user_cash=user_cash, lookup=lookup)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")
        input_shares = request.form.get("shares")

        # Ensure symbol field is not blank
        if not symbol:
            return apology("Missing symbol")

        # Ensure shares field is not blank
        if input_shares.strip() == "":
            return apology("Please enter number of shares")

        # Ensure symbol is integer
        if "." in input_shares:
            return apology("Please insert only whole numbers")
        if not input_shares.isdigit():
            return apology("Please insert only whole numbers")

        # convert shares into integer
        shares = int(input_shares)

        # Create variable for lookup function and ensure our symbol exists
        stock = lookup(symbol)

        if not stock:
            return apology("Invalid symbol")

        # shares cannot be negative value
        if int(shares) < 0:
            return apology("You cannot buy negative amount of shares")

        # get user id of actual user so we can work with user data in DB
        user_id = session["user_id"]
        # check amount of money user has and store it as variable
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        # Check the transaction value and determine if the transaction is possible, if not return apology
        transaction = shares * stock["price"]
        if transaction > user_cash:
            return apology("Insufficient funds")

        # update user cash amount if transaction was executed
        updated_cash = user_cash - transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, user_id)

        # update rest of data
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)", user_id, stock["symbol"], shares, stock["price"])

        # add message of stock bought
        flash("Succesfully bought %d shares of %s worth %s" % (shares, stock["symbol"], usd(shares * stock["price"])))

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # (we only use default get method here)
    # get user id of actual user so we can work with user data in DB
    user_id = session["user_id"]

    # get info from DBs for our table
    dbinfo = db.execute("SELECT * FROM transactions WHERE user_id = ?", user_id)

    return render_template("history.html", dbinfo=dbinfo)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("You must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("You must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Ensure symbol field is not blank
        if not symbol:
            return apology("Missing symbol")

        # Create variable for lookup function and ensure our symbol exists
        stock = lookup(symbol)

        if not stock:
            return apology("Invalid symbol")

        return render_template("quoted.html", name=stock["name"], price=stock["price"], symbol=stock["symbol"])

    # User reached route via GET
    else:
        return render_template("quote.html")


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
            return apology("You must provide username")
        if not password:
            return apology("You must provide password")
        if not confirmation:
            return apology("Please confirm password")

        # Check if password contains uppercase, lowercase letter and digit
        if not any(char.islower() for char in password):
            return apology("The password must contain at least one UPPERCASE LETTER, one LOWERCASE LETTER, and one DIGIT")
        if not any(char.isupper() for char in password):
            return apology("The password must contain at least one UPPERCASE LETTER, one LOWERCASE LETTER, and one DIGIT")
        if not any(char.isdigit() for char in password):
            return apology("The password must contain at least one UPPERCASE LETTER, one LOWERCASE LETTER, and one DIGIT")

        # Ensure confirmation matches password
        if password != confirmation:
            return apology("The passwords do not match")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # If username already exists return apology
        if len(rows) == 1:
            return apology("This username is already used")

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


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")
        input_shares = request.form.get("shares")

        # Ensure symbol field is not blank
        if not symbol:
            return apology("Missing symbol")

        # Ensure shares field is not blank
        if input_shares.strip() == "":
            return apology("Please enter number of shares")

        # Ensure symbol is integer
        if "." in input_shares:
            return apology("Please insert only whole numbers")
        if not input_shares.isdigit():
            return apology("Please insert only whole numbers")

        # convert shares into integer
        shares = int(input_shares)

        # Create variable for lookup function and ensure our symbol exists
        stock = lookup(symbol)

        if not stock:
            return apology("Invalid symbol")

        # shares cannot be negative value
        if int(shares) < 0:
            return apology("You cannot sell negative amount of shares")

        # get user id of actual user so we can work with user data in DB
        user_id = session["user_id"]

        # check amount of money user has and store it as variable
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # check amount of shares user has and retur appology if user is trying to sell more than is own
        user_shares = db.execute("SELECT shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol",
                                 user_id, symbol)[0]["shares"]
        if shares > user_shares:
            return apology("You cannot sell more shares than you currently have")

        # calculate transaction value
        transaction = shares * stock["price"]

        # update user cash amount if transaction was executed
        updated_cash = user_cash + transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, user_id)

        # update rest of data
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)",
                   user_id, stock["symbol"], (-1)*shares, stock["price"])

        # add message of stock bought
        flash("Succesfully sold %d shares of %s worth %s" % (shares, stock["symbol"], usd(shares * stock["price"])))

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET
    else:
        # get user id of actual user so we can create select menu in base of owned stocks
        user_id = session["user_id"]
        # get owned symbols from DB
        owned = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", user_id)
        # render template and pass in currently owned symbols
        return render_template("sell.html", symbols=[row["symbol"] for row in owned])
