import asyncio


"""
AsyncIO en Python

. Python3 hace mas facil el manejo de la concurrencia mediante un excelente libreria: asyncIO
. asyncio facilita al 100% las tareas a la hora de programar
  
. con la keyword "async def" somos bien explicitos de estar frente a una coRutina y ademas
  trae mas propiedades que un simple generador

. en lugar de pausar con yield utilizamos await sleep(0)

. nada de FIFO ni whiles ahora con asyncio.run tenemos loops super profesionales

El siguiente codigo es una analogia del codigo anerior pero resulto con async
"""



# coRutina async
async def leerTwitter():
    print('Twitter --> t01')
    await asyncio.sleep(0)
    print('Twitter --> t02')
    await asyncio.sleep(0)
    print('Twitter --> t03')
    await asyncio.sleep(0)
    return 'fin Twitter'

# coRutina async
async def leerFacebookThread():
    print('Facebook --> f01')
    await asyncio.sleep(0)
    print('Facebook --> f02')
    await asyncio.sleep(0)
    print('Facebook --> f03')
    await asyncio.sleep(0)
    print('Facebook --> f04')
    await asyncio.sleep(0)
    return 'fin Facebook'


# main coRutine to run Tasks Concurrently
# If any awaitable in list is a coroutine, it is automatically scheduled as a Task.
async def main():
    resultList = await asyncio.gather(
        leerTwitter(),
        leerFacebookThread()
        )
    print()
    print(resultList)
    
    
#runs the passed coroutine, taking care of managing the asyncio event loop
#Solo puede haber un event loop running in the same thread.
asyncio.run(main())
