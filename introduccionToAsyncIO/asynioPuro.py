import asyncio
import time


#Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications.
#sleep() always suspends the current task, allowing other tasks to run.
async def leerTwitter():
    print('Twitter --> t01')
    print('Twitter --> t02')
    await asyncio.sleep(1)
    print('Twitter --> t03')
    await asyncio.sleep(1)
    print('Twitter --> t04')
    return 'fin Twitter'

#Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications.
async def leerFacebook():
    print('Facebook --> f01')
    await asyncio.sleep(2)
    print('Facebook --> f02')
    await asyncio.sleep(2)
    print('Facebook --> f03')
    print('Facebook --> f04')
    return 'fin Facebook'



#algunos conceptos fundamantales

"""
si simplemente llamamos a la coRutina no solo que no se ejecutara sino
que ademas nos va a tirar el siguiente error:

RuntimeWarning: coroutine 'leerTwitter' was never awaited leerTwitter()
"""
leerTwitter()


print()
print()
print()
print()

"""
para ejecutar una coRutira podemos hacerlo de 3 maneras diferentes:
a continuacion vemos cada una de las 3 pero lo q debemos saber es que todas
comparten la misma manera de arrancar:

    asyncio.run(main())

de esta forma ejecutamos corutinas entendiendo q:
 1. runs the passed coroutine, taking care of managing the asyncio event loop
 2. finalizing asynchronous generators, and closing the threadpool.
 3. This function cannot be called when another asyncio event loop is running in the same thread.

    
"""

#Primer Manera: Secuencial, una coRutina detras de otra
# en este caso primero corre leerTwitter y luego leerFacebook
async def main():
    print(f"started at {time.strftime('%X')}")
    await leerTwitter()
    await leerFacebook()
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


print()
print()
print()
print()


#Segunda Manera: run coroutines concurrently 
# aprovecha el await de una coRutina para ejecutar codigo de otra
# va saltando de una a otra ganando tiempo de espera (generalmente operacions de IO)
async def main01():
    task1 = asyncio.create_task(leerTwitter())
    task2 = asyncio.create_task(leerFacebook())
    
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main01())

print()
print()
print()
print()


"""
Awaitables

. an object is awaitable if it can be used in an await expression.
. There are three main types of awaitable objects:
   1. coroutines (ya la vimos)
   2. Tasks (ya la vimos)
   3. Futures. Normally there is no need to create Future objects at the application level code.
"""


#Future
# Future objects in asyncio are needed to allow callback-based code to be used with async/await.
async def main02():

    print(f"started at {time.strftime('%X')}")
    await asyncio.gather(
        leerTwitter(),
        leerFacebook()
    )
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main02())

