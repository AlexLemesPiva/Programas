'''
script que calcula y muestra la suma de dos matrices cuadradas 
generadas aleatoriamente.
usar la comprensión de listas para generar las matrices de forma aleatoria
'''
import random


CALCMATRIZ = 1
SALIR = 2
N = 3

m1 = [[random.randint(1,20) for j in range(N)] for i in range(N)]
m2 = [[random.randint(1,20) for j in range(N)] for i in range(N)]
resultado = [[0]*N for i in range(N)]

for renglon in range(N):
    for columna in range(N):
        resultado[renglon][columna] = m1[renglon][columna] + m2[renglon][columna]

for i in range(N):
    if i == N//2:
        print(f'{m1[i]} + {m2[i]} = {resultado[i]}')
    else:
        print(f'{m1[i]} {m2[i]} {resultado[i]}')





