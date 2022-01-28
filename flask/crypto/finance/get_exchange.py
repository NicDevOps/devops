import os

from binance.client import Client


api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")

client = Client(api_key, api_secret)


exchange_info = client.get_exchange_info()
for s in exchange_info['symbols']:
    print(s['symbol'])