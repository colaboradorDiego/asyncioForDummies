# asyncioForDummies
learning asyncio by examples

# Python 3.5 + asyncio
	https://docs.python.org/3/library/asyncio.html
	
	Asyncio ahora forma parte del paquete standar de python y gano mucha relevancio para el manejor de tareas concurrentes.
	Incluso hoy dia sigue creciendo y fortaleciendose sin dudas como la libreria para la concurrencia en python.
	
	Para enenter lo que es asyncio tenemos que entender que son los generadores y como evolucionamos hasta asyncio.
	Dentro de introduccionToAsyncIO encontramos dos archivos con mucho detalle al respecto
	Sugiero arrancar con la lectura de ambos archivos que son ejecutames para comprender el concepto de asycio
		. arrancar con el codigo de --> generadores.py
		. para luego continuar con --> generadoresToAsyncio.py

	assyncio is at python standar lib and we use for write concurrent code using the async/await syntax.

# Unas palabras sobre CONCURRENCIA:
	Hacer varias tareas a la vez aprovechando los tiempos ociosos de cada tarea. No ES PARALELISMO.
	Con la concurrancia podemos arrancar otra tarea (CoRutina) sin esperar a que termine la actual.
	Vamos haciendo un poco de cada una, entendiendo que si tomo una foto en un instante N solo
	hay una tarea (CoRutina) ejecutandose en ese momento N
	Si pensamos a cada tarea (CoRutina) como una funcion y cada funcion la hacemos pausable, podemos ir ejecutnado varias funciones 
	de manera concurrente.
	asyncio provee a high/low level APIs, pero aqui vamos a utilizar claramente high-level
	
	Siguiente lectura --> https://docs.python.org/3/library/asyncio-task.html
	
	https://pymotw.com/3/asyncio/executors.html
	
