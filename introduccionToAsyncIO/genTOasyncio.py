import asyncio

"""
CoRutinas:
. async def define la coRutina y ademas establece mas propiedades que un simple generador
. ya no pausamos mas con yield, ahora utilizamos await asyncio.sleep(0)
. nada de FIFO ni whiles ahora con asyncio.run tenemos loops super profesionales

"""

async def leerTwitter():
    print('Twitter --> t01')
    await asyncio.sleep(0)
    print('Twitter --> t02')
    await asyncio.sleep(0)
    print('Twitter --> t03')
    await asyncio.sleep(0)
    return 'fin Twitter'

async def leerFacebook():
    print('Facebook --> f01')
    await asyncio.sleep(0)
    print('Facebook --> f02')
    await asyncio.sleep(0)
    print('Facebook --> f03')
    await asyncio.sleep(0)
    print('Facebook --> f04')
    await asyncio.sleep(0)
    return 'fin Facebook'

async def leer():
    await leerFacebook()
    return 'fin leer'


# main coRutine to run Tasks Concurrently
# If any awaitable in list is a coroutine, it is automatically scheduled as a Task.
async def main():
    task1 = asyncio.create_task(leerTwitter())
    task2 = asyncio.create_task(leerFacebook())

    await task1
    await task2
    
#runs the passed coroutine, taking care of managing the asyncio event loop
#Solo puede haber un event loop running in the same thread.
asyncio.run(main())
