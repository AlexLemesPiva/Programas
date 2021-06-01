'''
menu cíclicos

'''
import os
ESP = 1
ING = 2
NO_SUBS = 3
SALIR = 4

def mostrar_menu():
    print(F'''           Subtitulos
    {ESP}) ESPAÑOL
    {ING}) INGLÉS
    {NO_SUBS}) NO SUBS
    {SALIR}) SALIR
    ''')

continuar = True
while continuar:
    os.system('cls')
    mostrar_menu()
    opc = int(input('Elige una opción '))
    os.system('cls')
    if opc == ESP:
        print('Subtitulos en esp')
    elif opc == ING:
        print('Subs en ingles')
    elif opc == NO_SUBS:
        print('No subs selecionado')
    elif opc == SALIR:
        print('Saliste de menu')
    else: 
        print('opc no valida')
    input('Presiona enter para volver')