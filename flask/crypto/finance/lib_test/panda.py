import pandas as pd
import os
import requests
import pprint
# from binance.client import Client
import mplfinance as mpl
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")

client = Client(api_key, api_secret)
client.API_URL = 'https://api.binance.com/api'

asset="BTCUSDT"
start="2021.10.1"
end="2021.11.1"
timeframe="1d"


# df =pd.DataFrame(asset,timeframe,start,end)

df= pd.DataFrame(client.get_historical_klines(asset, timeframe,start,end))
df=df.iloc[:,:6]
df.columns=["Date","Open","High","Low","Close","Volume"]
df=df.set_index("Date")
df.index=pd.to_datetime(df.index,unit="ms")
df=df.astype("float")
print(df)
mpl.plot(df, type='candle')