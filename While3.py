#programa que pide datos a los usuarios de manera constante ahsta uqe coincida con los datos

import os

USER = 'brasu'
CONTRASENA = 'rufi123'

user = ''
contrasena = ''

while USER != user or CONTRASENA != contrasena:
    os.system('cls')
    user = input('Insira seu usuario: ')
    contrasena = input('Insira sua senha ')

    if USER != user or CONTRASENA != contrasena:
        print('Credenciales inválidas')
        print('Tente de novo')
        input('Press enter to continue...')
else:
    print('Bem-vindo ao sistema!')

