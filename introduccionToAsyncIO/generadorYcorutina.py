"""
Aprovechando las pausas q ofrecen los genereadores podemos utilizarlas para
manejar una serie de tareas concurrentes'

yield
  mete un pausa y regrea a la ejecucion principal
  
yield from
  mete una pausa e indica expresamente por donde debe continuar la ejecuacion
"""

"""
esto es un generador y supongamos q cada print es un codigo muy muy muy lento
en esta cado el yield pausa y retorna la ejecuacion al codigo principal
"""
def coRutinaAsyncSuperLenta():
    print('coRutinaAsyncSuperLenta --> subiendo 100GB')
    yield
    print('coRutinaAsyncSuperLenta --> subiendo 200GB')
    yield
    print('coRutinaAsyncSuperLenta --> subiendo 300GB')

"""
esto es otro generador y tambien vamos a suponer que cada linea es lenta
"""
def leerTwitter():
    print('leerTwitter --> t01')
    yield
    print('leerTwitter --> t02')
    yield
    print('leerTwitter --> t03')
    yield
    print('leerTwitter --> t04')


"""
otro generador mas con lineas lentas
"""
def leerFacebook():
    print('leerFacebook --> f01')
    yield
    print('leerFacebook --> f02')
    yield from coRutinaAsyncSuperLenta()
    print('leerFacebook --> f03')
    yield
    print('leerFacebook --> f04')


"""
El objetivo es ejecutar todas las corutinas de manera concurrentemente para aprovechar al maximo los tiempos
de nuestro cpu.

el loop q tenemos acontinuacion se vale de la pausa generada por cada yield para ir saltando entreo todas las 
corutinas y ejecutar todo en forma concurrente.


el try del loop no hace otra cosa que controlar que todas las tareas teminaron y ya no hay mas nada
por ejecutar
"""


# este es el loop
# recibe una lista de tareas a ejecutar
# el loop trabaja con colas, sacando y poniendo la tarea de la cola
def concurrenciaAsync(tareas):
    while (tareas):
        # traemos la primer taread de la cola y la ejecutamos
        tarea = tareas.pop(0)

        try:
            # ejecutamos la tarea
            next(tarea)
            # agregamos nuevamente la tarea a la cola
            tareas.append(tarea)

        except StopIteration:
            # si la ejecutamos la tarea y no tiene nada mas por hacer entra en este error
            pass


# Run loop
concurrenciaAsync([leerTwitter(), coRutinaAsyncSuperLenta()])

