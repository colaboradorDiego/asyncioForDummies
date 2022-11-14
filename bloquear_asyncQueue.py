import asyncio

productores = []


async def poner(q, counter):
    await q.put(counter)


async def producir(q):
    counter = 0
    while True:
        counter = counter + 1
        print(f'Fatigati trabajando: {counter}')
        productores.append(asyncio.create_task(poner(q, counter)))
        if counter == 10:
            productores.append(asyncio.create_task(q.join()))
            #await q.join()

        if counter == 20:
            print(f'A casa negro puto, generaste {counter} nros.')
            break

        await asyncio.sleep(1)


async def consumir(q):
    while True:
        nro = await q.get()
        print(f'Consumiento el trabajo de Fatigati {nro} restan {q.qsize()}')
        q.task_done()
        await asyncio.sleep(2)


async def producir_consumir_task():
    global productores

    deposito_de_enteros = asyncio.Queue()

    productores.append(asyncio.create_task(producir(deposito_de_enteros)))

    consumidores = []
    task = asyncio.create_task(consumir(deposito_de_enteros))
    consumidores.append(task)

    await asyncio.gather(*productores)

    await deposito_de_enteros.join()
    print("Se procesaron todo los nro enteros. Bien Fatigati!!")

    for c in consumidores:
        c.cancel()


asyncio.run(producir_consumir_task())
