


'''
Tabla de multiplicación
'''
numero = int(input('Que numero queres multiplicar' ))
limite = int(input('Hasta que numero queres ver' ))

for multiplo in range (0, limite+1):
    print(f'{numero} x {multiplo} = {numero * multiplo}')


''' Tabla de multiplicacion
que aparecen todas las listas juntas
'''

import os

for numero in range(1,11):
    os.system('cls')
    print('Tabla de multi del {numero} ')
    for multiplo in range (1,11):
        print(f'{numero} x {multiplo} = {numero * multiplo}')
    input('presiona enter para continuar')

