import os
import requests
import pprint
# from binance.client import Client
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")

client = Client(api_key, api_secret)
client.API_URL = 'https://api.binance.com/api'

response = client.get_symbol_ticker(symbol="BTCUSDT")

prices = client.get_all_tickers()

klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# pprint.pprint(klines)
# pprint.pprint(prices)

# socket manager using threads
twm = ThreadedWebsocketManager()
twm.start()

# depth cache manager using threads
dcm = ThreadedDepthCacheManager()
dcm.start()

def handle_socket_message(msg):
    print(f"message type: {msg['e']}")
    print(msg)

def handle_dcm_message(depth_cache):
    print(f"symbol {depth_cache.symbol}")
    print("top 5 bids")
    print(depth_cache.get_bids()[:5])
    print("top 5 asks")
    print(depth_cache.get_asks()[:5])
    print("last update time {}".format(depth_cache.update_time))

twm.start_kline_socket(callback=handle_socket_message, symbol='BTCUSDT')

dcm.start_depth_cache(callback=handle_dcm_message, symbol='BTCUSDT')