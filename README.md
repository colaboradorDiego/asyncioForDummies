# Asyncio

[Asyncio](https://docs.python.org/3/library/asyncio.html) es una libreria for write concurrent code using the async/await syntax.
Forma parte del paquete standar de python para manejar tareas concurrentes o concurrencia.

Asyncio provides a set of high-level APIs to run Python [coroutines](https://docs.python.org/3/library/asyncio-task.html#coroutine) concurrently and have full control over their execution

[Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)


Videos super recomendadas

[Entendiendo asyncio sin usar asyncio](https://www.youtube.com/watch?v=u_NDCBdHhzc) por Juan Pedro Fisanotti

[Pongase a la cola por favor](https://www.youtube.com/watch?v=nhD5Pz4mGhg) por Miguel Araujo y Jose Ignacio Galarza

Lectura super recomendada y muy interesante para profundizar Event loops [Async IO: A Complete Walkthrough](https://realpython.com/async-io-python/)

## Unas palabras sobre CONCURRENCIA:

Hacer varias tareas a la vez aprovechando los tiempos ociosos de cada tarea. No es ni paralelismo ni threading ni multiprocessing ni tampoco es una solucion magica a [Python Global Interpreter Lock (GIL)](https://realpython.com/python-gil/)

Asyncio esta para aprovechar los tiempos libres del procesador que generan todas las tareas de I/O esperando ya sea una respuesta de red o una accion por parte del usuario. Asyncio al igual que NODE.js solo puede ejecutar una sola CoRutina en un instante N tambien conocidas como *GREEN THREADS*

Asyncio no puede utilizar los multicores ni acelerar los procesos de cargas de trabajo pesadas para el procesador. Si este es el caso, olvidese de asyncio. By default, an async IO event loop runs in a single thread and on a single CPU core.

## Introduccion

Pero porque meternos con asyncio si tenemos por ejemplo frameworks como flask, Websokects y otros que nos hacen la vida un poco mas facil. La primera respuesta es muy obvia, estos utilizan asyncio, por lo q entendiendo mejor asyncio nos va a resultar mas simple cualquier otra libreria que se base en asyncio.

La segunda respuesta, que ya es un poco mas avanzadar, es salir del loop tipico de ejecucion para manejar tareas concurrentes *loop.run_until_complete()*. NO esta mal pero si vamos por ahi perdemos todas las ventajas de asynchronous, event-based code.



## Carpeta introduccionToAsyncIO	

Para enenter lo que es asyncio tenemos que entender que son los generadores y como evolucionamos hasta asyncio.
En la carpeta introduccionToAsyncIO encontramos 4 archivos con mucho detalle al respecto. Sujiero arrancar codeando los archivos para comprender el concepto de asyncio

| python code | detalle |
| ----------- | ------- |
| generadores.py | Primer concepto importante, el generador no es una lista ni un array, llamar a un generador como llamamos a cualquier funcion, tampoco va a  ejecutarlo. La forma correcta de trabajar con un generador es mediante algun mecanismo de iteracion como por ejemplo la funcion next(generador)|
| generadoresYcorutina.py | Los generadores son muy utiles para administrar la ejecucion de tareas. Si cargamos con una lista de tareas al generador y vamos iterando por cada una de ellas podemos ir ejecutando paso a paso un poco de cada una hasta completar todas. |
| genTOasyncio.py | asyncio toma los dos puntos anterires y transforma a los generadores en algo mas popente y facil de utilizar. Aqui aparece el concepto de awaitables tales como coroutines, task y futures que son objetos que debemos llamar obligatotiamente con await y esperar q realicen su trabajo. Ya veremos con mas detallle mas adelante. |
| asynioPuro.py | ver Event loops |
| asynIO-threads.py | threads |

		
# Event loops

El "Event loop" es un scheduler que va administrando tareas de una lista y que cuando encuentra un await pasa el control del flujo a la siguiente coRutina para que ejecute su tarea. Y asi va ejecuando concurrentemente cada coRutina

Podemos pensar al *Event loop* como un *while True loop* que controla las corutinas y que cuando termine de ejecutar la ultima sale del loop y asi termina la ejecucion del programa.

La magia de asynIO es que podemos crear el *Event Loop* con una sola linea de codigo , la cual se encarga inclusive de administrar todo lo nesesario para que este funcione sin problemas. Lo unico que debemos tener en cuenta es que this function cannot be called when another asyncio event loop is running in the same thread.

```
asyncio.run(main())
```

Claro que esta forma automatica nos quita un poco el control del Event Loop, que de ser necesario tener mas control e interactuar con el, podemos hacerlo de la forma tradicional con la siguientes lineas

```
loop = asyncio.get_event_loop()
try:
   loop.run_until_complete(main())
finally:
   loop.close()
```

y monitorearlo entre otras cosas con:

```	
loop.is_running()
loop.is_closed()
```

Aun si queremos ir mas finos podemos reemplazar al Event loop por completo con uno propio o con otra implementacion tal como lo muesta [uvLoop](https://github.com/MagicStack/uvloop)


## Ejecucion de los awaitables

An object is awaitable if it can be used in an await expression. There are three main types of awaitable objects:

1. coroutines
2. Tasks
3. Futures.

Podemos ejecutarlos de varias maneras

### Secuncial

await es la forma de ejecutar una corutina directamente. Como vemos en el siguiene codigo ejecutamos dos corutinas de manera secuencial. El primer await ejecuta y espera a que termine leerTwitter(), luego el segundo await ejecuta y espera a que termine leerFacebook(). Leer Twitter y Facebook son 2 awaitables, en este caso coroutines.

```
async def main():
    await leerTwitter()
    await leerFacebook()


asyncio.run(main())
```

### CONCURRENCIA

The [asyncio.create_task()](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task) function to run coroutines concurrently as asyncio [Tasks](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task).

craeate_task() Wrap a coroutine into a Task and schedule its execution.

El siguiente ejemplo crea las dos mismas corutinas anteriores pero ahora en forma de tareas de tal forma que se ejecuten concurrentemente, va saltando de una a otra ganando tiempo de espera (generalmente operacions de IO).

En primer lugar craeate_task crea y ejecuta leerTwitter y luego hace lo mismo con leerFacebook. En este caso como son tareas el Event Loop va a ejecutarlas alternando entre una y otra. Finalmente los dos await esperan a que se completen todas las tareas. Sin los await solo se ejecutan la primera accion de cada tarea y el Event Loop al no tener la orden de esperar termina finalizando el programa en este caso.


```
async def main():
    task1 = asyncio.create_task(leerTwitter())
    task2 = asyncio.create_task(leerFacebook())
    
    await task1
    await task2


asyncio.run(main())
```

### Future

Future objects in asyncio are needed to allow callback-based code to be used with async/await. Por ejemplo es el caso se los websockets

```
async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()
```

### Queues

Mediante el ejemplo consumer_producer_flow.py entendemos como funcionan las colas y las aplicamos en un flujo tipico de productor y consumidor.

[Not thread-safe FIFO queue](https://docs.python.org/3/library/asyncio-queue.html#asyncio-queues)

coroutine **get()**
Remove and return an item from the queue. If queue is empty, wait until an item is available.

coroutine **put(item)**
Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.

Tambien es conveniente utilizar el task_done() y el join()

Dejamos estos dos links como referencia para seguir profundizando

[Managing asyncio tasks](https://stackoverflow.com/questions/66292395/am-i-managing-asyncio-tasks-python-3-9-in-a-proper-way)

[Using asyncio.Queue for producer-consumer flow](https://stackoverflow.com/questions/52582685/using-asyncio-queue-for-producer-consumer-flow)

	
### Event Loop low-level functions 

[Lower-level code control over the event loop behavior](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop)

# AsyncIO for the working PyGame programmer

[Capitulo I](https://blubbervision.neocities.org/asyncio.html)

[Capitulo II](https://blubberquark.tumblr.com/post/177942351040/asyncio-for-the-working-pygame-programmer-part)


	
# Networking (pero esto es mas avanzado, queda para mas adelante)
Streams are high-level async/await-ready primitives to work with network connections. Streams allow sending and receiving data without using callbacks or low-level protocols and transports.

[Streams](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server)



# Avanzado

[How async/await works in Python](https://tenthousandmeters.com/blog/python-behind-the-scenes-12-how-asyncawait-works-in-python/)


# asyncio.Queue

[Producer - Consumer Flow](https://stackoverflow.com/questions/52582685/using-asyncio-queue-for-producer-consumer-flow)
