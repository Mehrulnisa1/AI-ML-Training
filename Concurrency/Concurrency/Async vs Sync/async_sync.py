import asyncio
import time


def synchronous():
    time.sleep(2)
    print("Synchronous task completed")


async def asynchronous():
    await asyncio.sleep(2)
    print("Asynchronous task completed")


synchronous()

asyncio.run(asynchronous())

#async and await
import asyncio


async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(hello())

#Event Loop
import asyncio


async def task():
    print("Task is running")
    await asyncio.sleep(1)
    print("Task completed")


async def main():
    await task()


asyncio.run(main())

#asyncio.gather()

import asyncio


async def task(name):
    print(name, "started")
    await asyncio.sleep(2)
    print(name, "finished")


async def main():
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )


asyncio.run(main())

#time.sleep() vs asyncio.sleep()
import asyncio
import time


def sync_sleep():
    print("Before time.sleep")
    time.sleep(2)
    print("After time.sleep")


async def async_sleep():
    print("Before asyncio.sleep")
    await asyncio.sleep(2)
    print("After asyncio.sleep")


sync_sleep()
asyncio.run(async_sleep())

#Asyncio vs Threading
import asyncio
import threading


def thread_work():
    print("Running using thread")


async def async_work():
    print("Running using asyncio")


thread = threading.Thread(target=thread_work)
thread.start()
thread.join()

asyncio.run(async_work())

#GIL
import threading


def work():
    total = 0

    for i in range(1_000_000):
        total += i

    print(total)


t1 = threading.Thread(target=work)
t2 = threading.Thread(target=work)

t1.start()
t2.start()

t1.join()
t2.join()