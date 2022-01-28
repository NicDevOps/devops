import websocket, json, pprint, talib, numpy

SOCKET = "wss://stream.binance.us:9443/ws/btcusdt@kline_1m"
closes = []

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'BTCUSDT'
TRADE_QTY = 0.05
in_position = False

def on_open(ws):
    print('opened connetion')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print('candle closed at: {}'.format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print('All RSIs are calculated so far')
            # print(rsi)
            last_rsi = rsi[-1]
            print("The last RSI is: {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Sell! Sell! Sell!")
                    # Put sell logic here.
                    in_position = False
                else:
                    print("It is overbought but, you dont own any, nothing to do.")

            elif last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("It is oversold, but you already own it, nothing to do.")
                else:
                    print("Oversold! Buy! Buy! Buy!")
                    # Put buy order logic here.
                    in_position = True



ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)

ws.run_forever()