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
    #a una coRutina no la podemos llamar sin el await pero a una funcion normal si que podemos
    holaMundo()
    await asyncio.sleep(0)
    print('Facebook --> f04')
    await asyncio.sleep(0)
    return 'fin Facebook'

def holaMundo():
    print('Hola Mundo')


async def main():
    resultList = await asyncio.gather(
        leerTwitter(),
        leerFacebook()
        )
    print()
    print(resultList)

asyncio.run(main())

