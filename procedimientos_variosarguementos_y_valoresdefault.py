'''
implementar procedimento en una tabla de multiplicacion donde muestre la tabla de un numero
que fue recibido como argumento.
debe contar con un segundo arguemnto que indique hasta donde tiene que multiplicar (limite)
y también un default indicando de donde arranca
'''

def tabla_multiplicar(numero, limite=10):
    print(f'tabla de multiplicar del {numero}')
    for i in range(1, limite+1):
        print(f'{i} x {numero} = {i*numero}')

tabla_multiplicar(1)
tabla_multiplicar(5,13)