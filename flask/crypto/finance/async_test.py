import asyncio
import json
import time

from binance import AsyncClient, DepthCacheManager, BinanceSocketManager


def wrapper(func):
    async def wrapped():
             
        start = time.perf_counter()
        x = await func()
        end = time.perf_counter()
        print("\u001b[0m" + func.__name__ + " " + str(end - start))
        return x
    return wrapped

@wrapper
async def listener():

    client = await AsyncClient.create()
    bsm = BinanceSocketManager(client)

    async with bsm.trade_socket('BTCUSDT') as ts:
        for _ in range(7):
            res = await ts.recv()
            print(f'\033[91mrecv {res}')

    await client.close_connection()


@wrapper
async def ask_bid():

    client = await AsyncClient.create()
    bsm = BinanceSocketManager(client)

    async with DepthCacheManager(client, symbol='BTCUSDT') as dcm_socket:
        for _ in range(5):
            depth_cache = await dcm_socket.recv()
            print(f"\033[36msymbol {depth_cache.symbol} updated:{depth_cache.update_time}")
            print("Top 5 asks:")
            print(depth_cache.get_asks()[:5])
            print("Top 5 bids:")
            print(depth_cache.get_bids()[:5])

    await client.close_connection()

@wrapper
async def klines():
    client = await AsyncClient.create()
    klines = client.get_historical_klines("BNBBTC", AsyncClient.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")
    
    async for kline in await client.get_historical_klines_generator("BNBBTC", AsyncClient.KLINE_INTERVAL_5MINUTE, "1 day ago UTC"):
        print(kline)
    
    await asyncio.sleep(2)

    await client.close_connection()




async def main():

    task1 = asyncio.create_task(listener())
    task2 = asyncio.create_task(ask_bid())
    task3 = asyncio.create_task(klines())

    await task1
    await task2
    await task3

    

if __name__ == "__main__":

    while True:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())