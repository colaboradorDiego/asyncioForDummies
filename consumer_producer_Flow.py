from random import randint

import asyncio

import keyboard
import msvcrt



"""
Mi productor genera enteros entre 1 y 10 hasta generar el nro 5.
Ahi termina su tarea y se va a la casa
Y como es FATIGATI va a descansar 1 segundos cada trabajo
"""

flag = True
async def detectar_tecla():
    global flag

    while flag:
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode("utf-8")
            if tecla == "q":
                flag = False
            else:
                print("Presinaste", tecla, " Para finalizar preciona q")


        await asyncio.sleep(2)


async def producir_hasta_dar_con5(q):
    while True:
        entero = randint(1, 10)
        print(f'Fatigati trabajando: {entero}')
        await q.put(entero)
        if entero == 5:
            print(f'A casa negro puto, generaste {q.qsize()} nros.')
            break
        await asyncio.sleep(1)

async def producir_hasta_keypress(q):
    global flag

    while flag:
        entero = randint(1, 10)
        print(f'Fatigati trabajando: {entero}')
        await q.put(entero)
        await asyncio.sleep(1)


"""
Este consumidor va a laburar hasta dejar el deposito vacio.
Ahora si luego entra algo, bueno q se jodan xq el ya de rajo.
"""


async def consumir_todo(q):
    while True:
        entero = await q.get()
        print(f'Consumiento el trabajo de Fatigati {entero} restan {q.qsize()}')
        q.task_done()
        if q.qsize() == 0:
            print(f'Vacie el deposito. Me rajo. FIN')
            break


"""
Este consumidor va a laburar hasta morir o hasta
que alguin superior le diga bastaaaa negro.
"""


async def consumir(q):
    while True:
        entero = await q.get()
        print(f'--> Consumiento el trabajo de Fatigati {entero}')
        q.task_done()
        await asyncio.sleep(2)


# testing productor
async def solo_producir():
    deposito_de_enteros = asyncio.Queue()
    await producir_hasta_dar_con5(deposito_de_enteros)


# testing productor y luego consumidor
async def producir_consumir():
    deposito_de_enteros = asyncio.Queue()
    await producir_hasta_dar_con5(deposito_de_enteros)
    print()
    await consumir_todo(deposito_de_enteros)


# testing productor y consumidor en paralelo
async def producir_consumir_task():
    deposito_de_enteros = asyncio.Queue()

    # hay un solo productor pero podriamos tener mas
    productores = []
    task = asyncio.create_task(producir_hasta_dar_con5(deposito_de_enteros))
    productores.append(task)

    # hay un solo consumidor pero podriamos tener mas
    consumidores = []
    task = asyncio.create_task(consumir(deposito_de_enteros))
    consumidores.append(task)

    # esperamos a que todos los productores terminen su trabajo
    await asyncio.gather(*productores)

    # bloqueamos la el deposito y esperamos por el fin de todas las tareas pendientes
    await deposito_de_enteros.join()
    print("Se procesaron todo los nro enteros. Bien Fatigati!!")

    # cerramos todos los consimidores
    for c in consumidores:
        c.cancel()



async def producir_consumir_teclas():
    deposito_de_enteros = asyncio.Queue()

    # hay un solo productor pero podriamos tener mas
    productores = []
    task = asyncio.create_task(producir_hasta_keypress(deposito_de_enteros))
    productores.append(task)

    task = asyncio.create_task(detectar_tecla())
    productores.append(task)

    consumidores = []
    task = asyncio.create_task(consumir(deposito_de_enteros))
    consumidores.append(task)


    # esperamos a que todos los productores terminen su trabajo
    print("Esperamos que los productores terminen")
    await asyncio.gather(*productores)
    print("Todos los productores detenidos, bloqueamos las colas")

    # bloqueamos la el deposito y esperamos por el fin de todas las tareas pendientes
    await deposito_de_enteros.join()
    print("Se procesaron todo los nro enteros. Bien Fatigati!!")

    # cerramos todos los consimidores
    for c in consumidores:
        c.cancel()

    print("Done!")


asyncio.run(producir_consumir_teclas())
