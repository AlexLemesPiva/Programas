

#jogo de usuario contra maquina

import os
import random

inferior = 1
superior = 100
secreto = random.randint(1,100)
usuario = -1
maquina = -1

while usuario != secreto and maquina != secreto:
    os.system('cls')
    maquina = random.randint(inferior, superior)
    print('Maquina, cuál es tu valor?')
    print(f'Maquina: {maquina}')

    if maquina > secreto:
        print('Su numero es mayor')
        superior = maquina - 1
    elif maquina < secreto:
        print('Su numero es menor')
        inferior = maquina + 1
    else:
        print('La maquina ha adivinado')
    if maquina != secreto:
        usuario = int(input('Insira um numero '))
        if usuario < secreto:
            print('su numero es menor')
            if usuario > inferior:
             inferior = usuario + 1
        elif usuario > secreto:
            print('tu numero es mayor')
            if usuario < superior:
                superior = usuario - 1
        else: 
            print('Has ganado')
    input('presiona enter para continuar')
input('Nos vemos...')
