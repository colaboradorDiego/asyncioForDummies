import asyncio


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


async def sampleFuture01():
    resultList = await asyncio.gather(
        leerTwitter(),
        leerFacebook()
        )
    print()
    print(resultList)


async def sampleFuture02():
    loop = asyncio.get_event_loop()
    futures = [loop.create_task(leerTwitter()), loop.create_task(leerFacebook())]
    loop.run_forever()
    for f in futures:
        f.cancel()


async def main():
    print("Ejemplo 1")
    await sampleFuture01()
    print()
    print("Ejemplo 2")
    await sampleFuture02()


asyncio.run(main())

