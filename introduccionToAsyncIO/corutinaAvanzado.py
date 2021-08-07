from threading import Thread
from time import sleep, time

"""
De aqui en mas a las tareas que hoy son los generadores los vamos a llamar coRutinas.

Como programadores vamos chocar con librerias y codigo que son sync (SINCRONICAS).
Por ejemplo si utilizo una lib para sql y la query tarda, el codigo sync de la query 
bloquEa el resto de las coRutinas hasta el fin de la query.
Es recomendable siempre utilizar librerias compatibles con async

Pero si no estan disponibles aplicamos una solucion no tan bonita utilizando Threads.
Asi podemos llamar a la coRutina sync utilizando Threads, la metemos
dentro de un while y vamos preguntando por el estado del thread y si no termino mandamos
un yield asi hasta que termine.
De esta forma vamos pasando a otras corrutinas hasta que la thread termine

Veamos el siguiente ejemplo
"""


# sync, no tiene yields
# sleep() suspends(bloquea) execution of the current thread for a given number of seconds.
def tareaSuperLenta():
    print(time())
    print('coRutinaSyncSuperLenta --> subiendo 400GB')
    sleep(0.001)
    print(time())
    print('coRutinaSyncSuperLenta --> subiendo 500GB')
    sleep(0.001)
    print()
    print(time())
    print('coRutinaSyncSuperLenta --> subiendo 600GB')


# coRutina asynsc
def leerTwitter():
    print('leerTwitter --> t01')
    yield
    print('leerTwitter --> t02')
    yield
    print('leerTwitter --> t03')
    yield
    print('leerTwitter --> t04')


# coRutina asynsc
def leerFacebookThread():
    # workArround
    print('workArround')
    yield from verySimpleWorkArround()

    print('leerFacebookThread --> f01')
    yield
    print('leerFacebookThread --> f02')
    yield
    print('leerFacebookThread --> f03')
    yield
    print('leerFacebookThread --> f04')


# loop
def concurrenciaSync(tareas):

    while (tareas):
        tarea = tareas.pop(0)

        try:
            next(tarea)
            tareas.append(tarea)

        except StopIteration:
            pass


#workArround para coRutina sync
def verySimpleWorkArround():
    x = Thread(target=tareaSuperLenta)
    x.start()
    while x.is_alive():
        tareaSuperLenta()
        yield


# run loop
concurrenciaSync([leerTwitter(), leerFacebookThread()])





