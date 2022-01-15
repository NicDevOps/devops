import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get('API_KEY'):
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
    user_id = session.get("user_id")

    stocks = db.execute("SELECT stocks.symbol, stocks.shares_qty FROM users JOIN stocks ON users.id = stocks.user_id;")
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    balance = cash[0]["cash"]

    return render_template("index.html", stocks=stocks, balance=balance)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide a valid Symbol", 403)

        elif not request.form.get("quantity"):
            return apology("must provide a quantity", 403)

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("Symbol not found", 404)

        p = quote["price"]
        s = quote["symbol"]

        symbol = request.form.get("symbol")
        quantity = request.form.get("quantity")

        user_id = session.get("user_id")
       
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        price = p * float(quantity)
        balance = float(cash[0]["cash"]) - price 

        if balance >= 0:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, user_id)
        else:
            return apology("Not enough money")

        stocks = db.execute("SELECT * FROM stocks WHERE symbol = ?", symbol)

        if not stocks:
            db.execute("INSERT INTO stocks (user_id, symbol, shares_qty) VALUES (?, ?, ?)",user_id, symbol, quantity)
        else:
            shares = db.execute("SELECT shares_qty FROM stocks WHERE user_id = ?", user_id)
            new_quantity = int(quantity) + int(shares[0]["shares_qty"])
            db.execute("UPDATE stocks SET shares_qty = ? WHERE symbol = ?", new_quantity, symbol)

        order_type = 'buy'
        date = datetime.datetime.now()
        db.execute("INSERT INTO orders (user_id, order_type, symbol, shares_num, share_price, total, date) VALUES (?, ?, ?, ?, ?, ?, ?)", user_id, order_type, symbol, quantity, p, price, date)

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session.get("user_id")
    orders = db.execute("SELECT orders.order_type, orders.symbol, orders.shares_num, orders.share_price, orders.total, orders.date FROM users JOIN orders ON users.id = orders.user_id;")

    return render_template("history.html", orders=orders)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
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
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide a valid Symbol", 403)

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("Symbol not found", 404)

        n = quote["name"]
        p = quote["price"]
        s = quote["symbol"]
        c = quote["change"]

        return render_template("quoted.html", get_name=n, get_price=p, get_symbol=s, get_change=c)

    else:
        return render_template("quote.html")
    # return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        if request.form.get("password") != request.form.get("confirm"):
            return apology("Password does not match!", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) == 1:
            return apology("username already exist!", 403)
        
        username = request.form.get("username")
        password = request.form.get("password")
        genhash = generate_password_hash(password)
        
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, genhash)

        return render_template("registered.html")
    
    else:
        return render_template("register.html")

    
    # return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide a valid Symbol", 403)

        elif not request.form.get("quantity"):
            return apology("must provide a quantity", 403)

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("Symbol not found", 404)

        p = quote["price"]
        s = quote["symbol"]

        symbol = request.form.get("symbol")
        quantity = request.form.get("quantity")

        user_id = session.get("user_id")
       
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        price = p * float(quantity)
        balance = float(cash[0]["cash"]) + price

        shares = db.execute("SELECT shares_qty FROM stocks WHERE user_id = ?", user_id)
        new_quantity = int(shares[0]["shares_qty"]) - int(quantity)

        if new_quantity >= 0:
            db.execute("UPDATE stocks SET shares_qty = ? WHERE symbol = ?", new_quantity, symbol)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, user_id)
        else:
            return apology("Not enough share", 404)
        
        if new_quantity == 0:
            db.execute("DELETE FROM stocks WHERE symbol = ? AND user_id = ?", symbol, user_id)

        order_type = 'sell'
        date = datetime.datetime.now()
        db.execute("INSERT INTO orders (user_id, order_type, symbol, shares_num, share_price, total, date) VALUES (?, ?, ?, ?, ?, ?, ?)", user_id, order_type, symbol, quantity, p, price, date)

        return redirect("/")

    else:
        return render_template("sell.html")
