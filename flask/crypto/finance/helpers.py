import os
import requests
# import urllib.parse
from binance.client import Client
from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    try:
        api_key = os.environ.get("api_key")
        api_secret = os.environ.get("api_secret")
        client = Client(api_key, api_secret)
        client.API_URL = 'https://api.binance.com/api'
        quote = client.get_symbol_ticker(symbol=symbol)

    except:
        return None
        
    try:
        return {
            "price": float(quote["price"]),
            "symbol": quote["symbol"],
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

def graph():

    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    client = Client(api_key, api_secret)

    candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

    processed_candles = []

    for data in candles:
        
        candle = {

            "time": data[0] / 1000, 
            "open": data[1], 
            "high": data[2], 
            "low": data[3], 
            "close": data[4] 
        }

    processed_candles.append(candle)

    return jsonify(processed_candles)