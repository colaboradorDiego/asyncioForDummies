# Asyncio

[Asyncio](https://docs.python.org/3/library/asyncio.html) es una libreria for write concurrent code using the async/await syntax.
Forma parte del paquete standar de python para manejar tareas concurrentes o concurrencia.

Asyncio provides a set of high-level APIs to run Python [coroutines](https://docs.python.org/3/library/asyncio-task.html#coroutine) concurrently and have full control over their execution

[Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)


Videos super recomendadas

[Entendiendo asyncio sin usar asyncio](https://www.youtube.com/watch?v=u_NDCBdHhzc) por Juan Pedro Fisanotti

[Pongase a la cola por favor](https://www.youtube.com/watch?v=nhD5Pz4mGhg) por Miguel Araujo y Jose Ignacio Galarza

## Unas palabras sobre CONCURRENCIA:

Hacer varias tareas a la vez aprovechando los tiempos ociosos de cada tarea. No es ni paralelismo ni threading ni multiprocessing ni tampoco es una solucion magica a [Python Global Interpreter Lock (GIL)](https://realpython.com/python-gil/)

Asyncio esta para aprovechar los tiempos libres del procesador que generan todas las tareas de I/O esperando ya sea una respuesta de red o una accion por parte del usuario. Asyncio al igual que NODE.js solo puede ejecutar una sola CoRutina en un instante N tambien conocidas como *GREEN THREADS*

Asyncio no puede utilizar los multicores ni acelerar los procesos de cargas de trabajo pesadas para el procesador. Si este es el caso, olvidese de asyncio.

## Introduccion

Pero porque meternos con asyncio si tenemos por ejemplo frameworks como flask, Websokects y otros que nos hacen la vida un poco mas facil. La primera respuesta es muy obvia, estos utilizan asyncio, por lo q entendiendo mejor asyncio nos va a resultar mas simple cualquier otra libreria que se base en asyncio.

La segunda respuesta, que ya es un poco mas avanzadar, es salir del loop tipico de ejecucion para manejar tareas concurrentes *loop.run_until_complete()*. NO esta mal pero si vamos por ahi perdemos todas las ventajas de asynchronous, event-based code.



## Carpeta introduccionToAsyncIO	

Para enenter lo que es asyncio tenemos que entender que son los generadores y como evolucionamos hasta asyncio.
En la carpeta introduccionToAsyncIO encontramos 4 archivos con mucho detalle al respecto. Sujiero arrancar codeando los archivos para comprender el concepto de asyncio

| python code | detalle |
| ----------- | ------- |
| generadores.py | Primer concepto importante, el generador no es una lista ni un array, llamar a un generador como llamamos a cualquier funcion no va a ejecutarlo, solo nos va a devolver su objeto. |
| generadoresYcorutina.py | Ampliamos el concepto anterior y vemos que si en lugar de llamar a la next(CoRutina) llamamos directamente coRutina, el programa no hace nada |
| genTOasyncio.py | 100% de codigo asyncio. Basandonos en los conceptos previos de los generadores si llamamos a una coRutina sin await esta no hace nada. await nos permite llamar a la siguietne coRutina de manera indirecta o explicitamente indicando el nombre de la coRutina. Lo que no podemos hacer es llamar coRutinas por fuera de otra corutina |
| asynioPuro.py | ver Event loops |
| asynIO-threads.py | threads |

		
# Event loops

El "Event loop" es un scheduler que va administrando tareas de una lista y que cuando encuentra un await pasa el el control del flujo a la siguiente coRutina para que ejecute su tarea. Y asi va ejecuando concurrentemente cada coRutina

Para ejecutar una coRutira podemos hacerlo de 3 maneras diferentes, teniendo todas los siguientes puntos en comun.

Codigo para iniciarlizar el **EVENT LOOP**. This function cannot be called when another asyncio event loop is running in the same thread.
> asyncio.run(main())

### Loop secuncial

Secuencial, una coRutina detras de otra. En este caso primero corre leerTwitter y luego leerFacebook

```
async def main():
    await leerTwitter()
    await leerFacebook()


asyncio.run(main())
```

### Loop CONCURRENCIA

Aprovecha el await de una coRutina para ejecutar codigo de otra. Va saltando de una a otra ganando tiempo de espera (generalmente operacions de IO)

```
async def main():
    task1 = asyncio.create_task(leerTwitter())
    task2 = asyncio.create_task(leerFacebook())
    
    await task1
    await task2


asyncio.run(main())
```

### Loop Awaitables

An object is awaitable if it can be used in an await expression. There are three main types of awaitable objects:

1. coroutines
2. Tasks
3. Futures.

Future objects in asyncio are needed to allow callback-based code to be used with async/await.

```
async def main():
    await asyncio.gather(
        leerTwitter(),
        leerFacebook()
    )

asyncio.run(main())
```

### Loop Manager

[Manager with asyncio.Queue](https://stackoverflow.com/questions/66292395/am-i-managing-asyncio-tasks-python-3-9-in-a-proper-way)

	
### Event Loop low-level functions 

[Lower-level code control over the event loop behavior](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop)

AsyncIO for the working PyGame programmer

[Capitulo I](https://blubbervision.neocities.org/asyncio.html)

[Capitulo II](https://blubberquark.tumblr.com/post/177942351040/asyncio-for-the-working-pygame-programmer-part)


	
# Networking (pero esto es mas avanzado, queda para mas adelante)
Streams are high-level async/await-ready primitives to work with network connections. Streams allow sending and receiving data without using callbacks or low-level protocols and transports.

[Streams](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server)



