def leerTwitter():
    print('leerTwitter --> t01')
    yield
    print('leerTwitter --> t02')
    yield
    print('leerTwitter --> t03')
    yield
    print('leerTwitter --> t04')

def leerFacebook():
    print('leerFacebook --> f01')
    yield
    print('leerFacebook --> f02')
    yield
    print('leerFacebook --> f03')
    yield
    print('leerFacebook --> f04')


# Event loop
def concurrenciaAsync(tareas):
    while (tareas):
        # traemos la primer taread de la cola y la ejecutamos
        tarea = tareas.pop(0)

        # ejecutamos la tarea
        try:
            next(tarea)
            tareas.append(tarea)

        except StopIteration:
            # si la ejecutamos la tarea y no tiene nada mas por hacer entra en este error
            pass


# Run loop
concurrenciaAsync([leerTwitter(), leerFacebook()])

