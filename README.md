# asyncioForDummies
learning asyncio by examples
asyncio python standar lib and we use for write concurrent code using the async/await syntax.

# Lecturas super recomendadas
Algunos le resulta mas facil mirar los videos y luego las notas mas el codido que dejamos a continuacin.
A otros al reves, por lo tanto lo dejamos a su criterio.
	
[Entendiendo asyncio sin usar asyncio, por Juan Pedro Fisanotti](https://www.youtube.com/watch?v=u_NDCBdHhzc)

[asyncIO: póngase a la cola por favor - Miguel Araujo y Jose Ignacio Galarza](https://www.youtube.com/watch?v=nhD5Pz4mGhg)

[Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)

# Python 3.5 + asyncio

[asyncio docs](https://docs.python.org/3/library/asyncio.html)
	
Asyncio ahora forma parte del paquete standar de python y gano mucha relevancio para el manejor de tareas concurrentes.
Incluso hoy dia sigue creciendo y fortaleciendose sin dudas como la libreria para la concurrencia en python.
	
# Carpeta introduccionToAsyncIO	
[Siguiente lectura](https://docs.python.org/3/library/asyncio-task.html)
	
Para enenter lo que es asyncio tenemos que entender que son los generadores y como evolucionamos hasta asyncio.
Dentro de introduccionToAsyncIO encontramos 4 archivos con mucho detalle al respecto
	
Arrancar codeando los archivos para comprender el concepto de asyncio
```
generadores.py 			--> explica que son los generadores
generadoresYcorutina.py --> explica la utilizacion principal de los generadores
corutinaAvanzado.py 	--> combina corutinas sync mas async (aun sigue bloqueando todo)
genTOasyncio.py 		--> dejamos de escribir codigo con generadores para pasar 100% a asyncio
asynioPuro.py 			--> alternativas para manejar los loops
asynIO-threads.py 		--> threads
```
		
# Carpeta introToLopps
[create and manage event loops, which provide asynchronous APIs for networking](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop)

Particularmente solo vi estas 3 nomas:
- loop.run_until_complete(future)
- loop.run_forever()
- loop.stop()
	
	
# Carpeta networking (pero esto es mas avanzado, queda para mas adelante)

- Streams are high-level async/await-ready primitives to work with network connections.
- Streams allow sending and receiving data without using callbacks or low-level protocols and transports.
- [siguiente lectura](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server)


# Unas palabras sobre CONCURRENCIA:

Hacer varias tareas a la vez aprovechando los tiempos ociosos de cada tarea. No ES PARALELISMO.
Con la concurrancia podemos arrancar otra tarea (CoRutina) sin esperar a que termine la actual.
Vamos haciendo un poco de cada una, entendiendo que si tomo una foto en un instante N solo hay una tarea (CoRutina) ejecutandose en ese momento N
Si pensamos a cada tarea (CoRutina) como una funcion y cada funcion la hacemos pausable, podemos ir ejecutnado varias funciones de manera concurrente.
Asyncio provee a high/low level APIs, pero aqui vamos a utilizar claramente high-level

	
	
	
	
	
