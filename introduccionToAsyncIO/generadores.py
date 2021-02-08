from threading import Thread
from time import sleep, time


"""
Generadores en Python

Una lista de un millon de cosas ocuparia mucho en memoria, con un generador
podemos tener acceso a esa lista con la ventaja de NO tenerla en memoria. Es decir
no es una lista ya que no esta en memoria. Es un generador.
"""

print('Asi funcionan los generadores en Python')
print()

# esto es un generador
def numeros():
    yield '01'
    yield '02'
    yield '03'
    yield '04'
    yield '05'
    yield '06'

n = numeros()

#n no tiene todos los numeros en memoria
print(n)

#como vemos solo tiene uno
print()
print('next : ', next(n))
print('next : ', next(n))
print()

#todos
for numero in numeros():
    print(numero)

"""
Analizando el generador "def numeros()" vemos q es una funcion pausable e iterable, la pausa se da en cada
yield. Lo comprobamos metiendo un print entra cada yield
"""

print()
# esto es un generador
def numeros():
    yield '01'
    yield '02'
    print('Hola Mundo')
    yield '03'
    yield '04'
    print('Allo')
    yield '05'
    yield '06'

n = numeros()
print()
print('next : ', next(n))
print('next : ', next(n))
print('next : ', next(n))
print('next : ', next(n))
print('next : ', next(n))
print('next : ', next(n))


"""
Aprovechando estas pausas q ofrecen los genereadores podemos utilizarlas para
manejar una serie de tareas concurrente'
"""

print()
print('*************************************')
print()


"""
yield
-- mete un pausa y regrea a la ejecucion principal
yield from
-- mete una pausa e indica expresamente por donde debe continuar la ejecuacion
"""

# esto es un generador y supongamos q cada print es un codigo muy muy muy lento
# en esta cado el yield pausa y retorna la ejecuacion al codigo principal
def coRutinaAsyncSuperLenta():
    print('coRutinaAsyncSuperLenta --> subiendo 100GB')
    yield
    print('coRutinaAsyncSuperLenta --> subiendo 200GB')
    yield
    print('coRutinaAsyncSuperLenta --> subiendo 300GB')


# esto es un generador y supongamos q cada print es un codigo lento
# en esta caso el yield pausa y retorna la ejecuacion al codigo principal
def leerTwitter():
    print('Twitter --> t01')
    print('Twitter --> t02')
    yield
    print('Twitter --> t03')
    print('Twitter --> t04')

# esto es un generador y supongamos q cada print es un codigo lento
# en esta cado el yield pero indica por donde debe seguir la ejecucion.
def leerFacebook():
    print('Facebook --> f01')
    print('Facebook --> f02')
    print('Facebook --> f03')
    yield from coRutinaAsyncSuperLenta()
    print('Facebook --> f04')
    print('Facebook --> f05')
    yield
    print('Facebook --> f06')
    print('Facebook --> f07')


"""
Si pensamo a cada generador como una tarea, y sabemos que algunas duran mas que otras
y nuestra idea es ejecutarlas a todas concurrentemente para aprovechar al maximo los tiempos
de nuestro cpu es necesario hacer un loop que valla ejecutando un pedasito de cada una, asi
hasta terminalas todas.

Aprovechando la pausa de cada una al llegar al yield el loop continia con la siguiente hasta un nuevo
yield y asi susesivamente hasta terminar con cada una.

el try del loop no hace otra cosa que controlar que todas las tareas teminaron y ya no hay mas nada
por ejecutar
"""

#este es el loop
#arg tareas es simplemente la lista de tareas a ejecutar concurrentemente
#el loop trabaja con colas, sacando y poniendo la tarea de la cola
def concurrenciaAsync(tareas):
    while(tareas):
        #traemos la primer taread de la cola y la ejecutamos
        tarea = tareas.pop(0)

        try:
            #ejecutamos la tarea
            next(tarea)
            #agregamos nuevamente la tarea a la cola
            tareas.append(tarea)

        except StopIteration:
            #si la ejecutamos la tarea y no tiene nada mas por hacer entra en este error
            pass


#Run loop
concurrenciaAsync([leerTwitter(), leerFacebook()])


#espero haber sido claro hasta el momento y vamos a avanzar un poco mas

print()
print()
print('*****************************************')
print()


    
"""
De aqui en mas a las tareas que hoy son los generadores los vamos a llamar coRutinas.

En este caso la coRutinaSuperLenta() esta programada de manera async, es decir tiene
yield (pausas entre linea y linea q el programador puso a su criterio)

Como programadores vamos chocar con librerias y codigo que son sync. Por ejemplo si
utilizo una lib para sql y la query tarda, el codigo sync de la query bloqua el
resto de las coRutinas hasta el fin de la query.
Es recomendable siempre utilizar librerias compatibles con async

Pero si no estan disponibles aplicamos una solucion no tan bonita utilizando Threads.
Asi podemos llamar a la coRutina sync utilizando Threads, la metemos
dentro de un while y vamos preguntando por el estado del thread y si no termino mandamos
un yield asi hasta que termine.
De esta forma vamos pasando a otras corrutinas hasta que la thread termine

Veamos el siguiente ejemplo
"""



#coRutina sync, no tiene yields
#sleep() suspends(bloquea) execution of the current thread for a given number of seconds.
def coRutinaSyncSuperLenta():
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
def leerFacebookThread():
    print('Facebook --> f01')
    print('Facebook --> f02')
    print('Facebook --> f03')

    #workArround para coRutina sync
    x = Thread(target=coRutinaSyncSuperLenta)
    x.start()
    while x.is_alive():
        yield from leerTwitter()
    

    print('Facebook --> f04')
    print('Facebook --> f05')
    yield
    print('Facebook --> f06')
    print('Facebook --> f07')


# TODO: si bien el workArround funciona para entender el ejemplo quizas no esta del todo
# TODO: correcto ni en su forma ni en el orden que hace las cosas del loop
# TODO: any suggestion welcome


#loop
def concurrenciaSync(tareas):  
    while(tareas):
        #traemos la primer taread de la cola y la ejecutamos
        tarea = tareas.pop(0)

        try:
            next(tarea)
            #agregamos nuevamente la tarea a la cola
            tareas.append(tarea)
        except StopIteration:
            pass

#run loop
concurrenciaSync([leerTwitter(), leerFacebookThread()])
    
