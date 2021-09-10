import aiohttp
import asyncio
import time

start_time = time.time()

async def getdata(session,url):
    async with session.get(url) as resp:
        r = await resp.json()
        print(r['delay'])

async def main():
    url = 'http://127.0.0.1:5000/demo'
    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 15):
            tasks.append(asyncio.create_task(getdata(session, url)))

        for task in tasks:
            await task


asyncio.run(main())
print(f"{(time.time() - start_time)} seconds")