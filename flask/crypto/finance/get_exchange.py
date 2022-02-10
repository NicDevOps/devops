import os
import time
import pandas as pd
from binance.client import Client


api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")

client = Client(api_key, api_secret)


exchange_info = client.get_exchange_info()

# print(exchange_info)

symbols = []

for s in exchange_info['symbols']:
    symbols.append(s['symbol'])
# print(symbols)

start="2020.10.1"
end="2022.23.1"
timeframe="1d"

    
try:
    for s in symbols:
        print(s)
        df = pd.DataFrame(client.get_historical_klines(s, timeframe,start,end))
        if df.empty:
            print('Your df is empty...')
            continue
        print(df)
        df=df.iloc[:,:6]
        df.columns=["Date","Open","High","Low","Close","Volume"]
        df=df.set_index("Date")
        df.index=pd.to_datetime(df.index,unit="ms")
        df=df.astype("float")
        # df.to_csv('data/daily_year/{}'.format(s))
except:
    pass