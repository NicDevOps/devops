import csv
import os
from flask import jsonify
from binance.client import Client
import json

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")

client = Client(api_key, api_secret)
# client.API_URL = 'https://api.binance.com/api'

# status = client.get_account_status()

# fees = client.get_trade_fee()
# info = client.get_account()

# print(fees)

# prices = client.get_all_tickers()

# candles = client.get_klines(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_5MINUTE)

# klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# print(klines)



# csvfile = open('15min.csv', 'w', newline='')
# candlestick_writer = csv.writer(csvfile, delimiter=',')
    

# for candlestick in candles:
#     candlestick_writer.writerow(candlestick)
#     print(candlestick)





candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")

processed_candles = []

for data in candles:
        
    candle = {

        "time": data[0] / 1000, 
        "open": data[1], 
        "high": data[2], 
        "low": data[3], 
        "close": data[4] 
    }
    # print(candle)
    processed_candles.append(candle)

    # y = json.loads(candle)

    # print(y["close"])

# print(processed_candles)

y = json.dumps(processed_candles)

print(y)
# jsonify(processed_candles)


