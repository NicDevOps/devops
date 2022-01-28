import talib
import pandas as pd
import os
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")

client = Client(api_key, api_secret)
# client.API_URL = 'https://api.binance.com/api'

asset="BTCUSDT"
start="2020.10.1"
end="2022.23.1"
timeframe="1d"


# df =pd.DataFrame(asset,timeframe,start,end)

df= pd.DataFrame(client.get_historical_klines(asset, timeframe,start,end))
df=df.iloc[:,:6]
df.columns=["Date","Open","High","Low","Close","Volume"]
df=df.set_index("Date")
df.index=pd.to_datetime(df.index,unit="ms")
df=df.astype("float")
print(df)

# morningstar = talib.CDLMORNINGSTAR(df["Open"], df["High"], df["Low"], df["Close"])
# engulfing = talib.CDLENGULFING(df["Open"], df["High"], df["Low"], df["Close"])

# df["Morning Star"] = morningstar
# df["Engulfing"] = engulfing

# morningstar_days = df[df["Morning Star"] != 0]

# engulfing_days = df[df["Engulfing"] != 0]

# # print(morningstar_days)
# print(engulfing_days)