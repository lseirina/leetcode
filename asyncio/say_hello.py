import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f'Hello, {name}')


async def main():
    task1 = asyncio.create_task(say_hello('Mary', 3))
    task2 = asyncio.create_task(say_hello('Sara', 2))

    await task1
    await task2

asyncio.run(main())
