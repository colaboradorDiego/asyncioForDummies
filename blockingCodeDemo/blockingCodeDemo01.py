import asyncio
import time


"""
Ver:
https://stackoverflow.com/questions/52484087/long-delay-in-using-asyncio-and-websockets-in-python-3

main_task se ejecuta hasta el primer await keep_alive()
el while del keep_alive toma el control del event loop y no lo larga mas.

La solicion a este problema esta en background_01.py
"""


async def keep_alive(msg, segundos):
    while True:
        await asyncio.sleep(segundos)
        print("Mensaje:", msg)


# bloking code
def long_blocking_job(segundos):
    time.sleep(segundos)
    print("Done long task bloquing: ", str(segundos))


async def main_task():
    print("Runnung now ...")

    block_time = 5
    keep_alive_time = 3
    await keep_alive("Task_1!", keep_alive_time)
    await keep_alive("Task_2!", keep_alive_time)

    # bloking code
    while True:
        time.sleep(block_time)
        print("Done main bloquing Job ", str(block_time))
        long_blocking_job(block_time)


asyncio.run(main_task())
