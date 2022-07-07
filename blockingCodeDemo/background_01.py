import asyncio
import time


"""
Ahora el problema es el while True del main

por mas que tengamos a las dos tareas concurrentes (task1 y task2) correctamente creadas
con asyncio.create_task(), el codigo no concurrente del while tomo el control y
termina bloqueando todo

Tenemos dos soluciones posibles:

background_02.py
transformamos el codigo en que bloquea en concurrente

background_03.py
si no es posible transformar el codigo en concurrente debemos
recurrir a los Executors
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
    asyncio.create_task(keep_alive("Task_1!", keep_alive_time))
    asyncio.create_task(keep_alive("Task_2!", keep_alive_time))

    # bloking code
    while True:
        time.sleep(block_time)
        print("Done main bloquing Job ", str(block_time))
        long_blocking_job(block_time)


asyncio.run(main_task())
