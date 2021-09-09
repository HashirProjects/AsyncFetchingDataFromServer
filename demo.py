import asyncio
import random
import time

async def getData():
	delay = random.randint(1,10)
	await asyncio.sleep(delay)
	return delay

async def processData(number):
	print(f"starting coroutine {number}")
	delay = await getData()
	return f"Delay for coroutine {number} was {delay}s. "

async def main():
	print("start")
	r1 = asyncio.create_task(processData(1))
	r2 = asyncio.create_task(processData(2))
	r3 = asyncio.create_task(processData(3))
	value = await r1
	value += await r2
	value += await r3
	print(value)


asyncio.run(main())