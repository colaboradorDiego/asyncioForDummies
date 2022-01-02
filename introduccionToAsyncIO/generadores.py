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
print("los generadores no son una lista, son un generador", n)

#como vemos solo tiene uno
print()
print('next : ', next(n))
print('next : ', next(n))
print()

#todos
for numero in numeros():
    print(numero)

