import asyncio

# async def main():
#     print('tim')
#     task = asyncio.create_task(foo('hello'))
#     await asyncio.sleep(2)
#     print('finished')

# async def foo(text):
#     print(text)
#     await asyncio.sleep(10)

# asyncio.run(main())

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.10)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await(task1)
    print(value)
    await task2

asyncio.run(main())

