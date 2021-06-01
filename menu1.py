#Menu guerreros e suas habildiades

import os

GUERRERO = 1
MAGO = 2
ELFO = 3
SAIR = 4

continuar = True

while continuar:
    os.system ('cls')

    print('''
    1) Guerreiro.
    2) Mago.
    3) Elfo.
    4) Sair.
    ''')
    opc = int(input('Escolha seu guerreiro '))

    if opc == GUERRERO:
        print('''
        Fuerza: 25
        Agilidade: 16
        Mana: 10
        ''')
    elif opc == MAGO:
        print('''
        Fuerza: 18
        Agilidade: 18
        Mana: 26
        ''')
    elif opc == ELFO:
        print('''
        Fuerza: 10
        Agilidade: 10
        Mana: 20
        ''')
    elif opc == SAIR:
        continuar = False
    else:
        print('Valor Inválido')
    input('Press enter para continuar')

print('nos vemos')
