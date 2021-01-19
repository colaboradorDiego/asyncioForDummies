from threading import Thread
from time import time, sleep
import asyncio


"""
Pero que pasa con las tareas o librerias q no estan programadas con asyncio
En este caso seria todo codigo bloqueante que frenaria drasticamente el loop
Afortunadamente ya hay muchas migradas a async pero para las que no afortunadamente
tenemos una  solucion conbinando threads de una forma mas prodfesional que la
que vimos en el ejemplo1

"""



# coRutina async
async def leerTwitter():
    print('Twitter --> t01')
    print('Twitter --> t02')
    await asyncio.sleep(0)
    print('Twitter --> t03')
    print('Twitter --> t04')
    return 'fin Twitter'

# coRutina async
async def leerFacebookThread():
    print('Facebook --> f01')
    print('Facebook --> f02')
    await asyncio.sleep(0)
    print('Facebook --> f03')
    print('Facebook --> f04')
    print('Facebook --> f05')
    await asyncio.sleep(0)
    print('Facebook --> f06')
    print('Facebook --> f07')
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
