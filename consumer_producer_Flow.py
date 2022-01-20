import asyncio
import random

log = []

"""
produce a token and send it to a consumer

Por cada vuelta del while:
1. genera un token
2. lo mete en la cola y lo muestra
Asi continua generando tokens hasta la condicion (token < .05:) y hace el break
"""
async def producer(queue, name):
    while True:
        token = random.random()
        txt = f'produced {token} by {name}'
        log.append(txt)
        print(txt)
        if token < .05:
            break
        await queue.put(token)
        await asyncio.sleep(0)


"""
process the token received from a producer

Por cada vuelta del while:
1. se queda esperando a que aparesca un nuevo item
2. lo toma de la cola y lo muestra
3. task_done() si no lo usamos funciona igual pero corresponde usarlo
Luego va a la proxima iteracion y asi se queda haciendo lo mismo por siempre
"""
async def consumer(queue, name):
    while True:
        token = await queue.get()
        await asyncio.sleep(0)
        txt = f'consumed {token} by {name}'
        queue.task_done()
        log.append(txt)
        print(txt)


# fire up the both producers and consumers
async def main():
    queue = asyncio.Queue()

    consumidores = []
    for x in range(10):
        consumidores.append(asyncio.create_task(consumer(queue, f'consumer {x}'), name=f'consumer {x}'))

    productores = []
    for i in range(3):
        productores.append(asyncio.create_task(producer(queue, f'producer {i}'), name=f'producer {i}'))

    for p in productores:
        await p

    await queue.join()

    print('---- done!!!!!')

    # Write Line by Line
    with open('data/ordenDeEjecucion.txt', 'w') as fHandle:
        for l in log:
            fHandle.write(l + "\n")


asyncio.run(main())
