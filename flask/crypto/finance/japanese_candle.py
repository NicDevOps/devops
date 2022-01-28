import talib
import yfinance as yf


# data = yf.download("SPY", threads= False, start="2020-01-01", end="2020-08-01")


data = yf.download("SPY AAPL MSFT", threads= False, period="1y")


print(data)