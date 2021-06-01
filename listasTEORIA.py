'''
coleccion de datos, en python podemos tener listas de distntos tipos de datos.
ejemplo:

lista = []
lista = [1,2,3]
agregar items en el final de la lista:
lista.append()

agregar mmas de un item a la vez:
lista += [valores]
lista.extend([valores])

Para agregar datos donde quiera:
lista.insert(1, 33) = (posicion, valor)
[3, 33, ...] las listas arrancan por el contaje 0, por eso el 33 está en el seugndo lugar (0, 1)

Podemos agregar elementos en cualquier posición, que python lo arregla

Consultar en la lista:
lista[valor a consultar]

eliminar valor de la lista:
lista.pop() (si está vacio elimina el último valor agregado)
lista.pop(2) (elimina el elemento de esa posición)
lista.remove(5) (elimina el valor específico)

assegurar que tenho valores na lista:
33 in lista
False or true

consultar posición del a lista:
linta.index(valor) devuelve la posición del primer elemento

cuantas veces aparece un valor en una lista:
lista.count(valor)

ordenar listas: (solo sirve si son ordenables y comparables entre si)

lista.sort()

Cuantos elementos hay en una lista:
len(lista)

menor y mayor de la lista:
min(lista)
max(lista)

-------------------------------------------------

lista que tenga mismo valor varias veces

l1 = [0] * 10

l2 = l1  la lista dos tendra todos lso elementos de l1

si después hago modificaciones en la LISTA 1, también se verá reflejado en la lista 2
pues l1 = l2 (el sistema trabaja por referencia, se refieren a la misma lista)
Para que no pase eso se utiliza el siguiente código
1) copias la lista: l2 = l1[:]

Consulta de valores
l2[3:] (buscaar valores apartir de la posición 3)
l2[:5] (acá al revés, busca del 0 hasta el 5)
l2[3:10] (busca desde la pos 3 a la 9)
l2[1:6:2]( desde la pos 1 hasta la 6, salteando de a 2)


lista compactacion
l4 = [i for i in range(7)]
l4 = [0,1,2,3,4,5,6]
l5 = [random.ranint(1, 10) for i in range (20)] (genera 20 numeros aleatorios)

Matriz = [1,2,3], [4,5,6], [7,8,9]

Para consultar valores en la matriz

matriz= [] []  (primer corchetes consulta linea, el otro colunma)
'''