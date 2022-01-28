import os
import pandas as pd

def is_consolidating(df, percentage=3):

    recent_candlesticks = df[-15:]

    max_close = recent_candlesticks['Close'].max()
    min_close = recent_candlesticks['Close'].min()

    # print(max_close)
    # print(min_close)
    threshold = 1 - (percentage / 100)
    if min_close > (max_close * threshold):
        return True
    else:
        return False

def is_breakingout(df):
    last_close = df[-1:]['Close'].values[0]
    # print(last_close)
    if is_consolidating(df[:-1]):
        recent_closes = df[-16:-1]

        if last_close > recent_closes['Close'].max():
            return True
    else:
        return False

for filename in os.listdir('data/daily_year'):
    df = pd.read_csv('data/daily_year/{}'.format(filename))

    if is_consolidating(df, percentage=2.5):
        print('{} is consolidating...'.format(filename))
    
    if is_breakingout(df):
        print('{} is breaking out!!'.format(filename))
    
