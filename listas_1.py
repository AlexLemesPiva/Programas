'''
menu de frutas

'''

import os

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 8

frutas = []

def menu():
        os.system('cls')
        print(f'''
    {AGREGAR}) AGREGAR
    {INSERTAR}) INSERTAR
    {MOSTRAR}) MOSTRAR
    {BUSCAR}) BUSCAR
    {ELIMINAR}) ELIMINAR
    {ORDENAR}) ORDENAR
    {LIMPIAR}) LIMPIAR
    {SALIR}) SALIR''')

def agregar_registro():
    print('         Agregar registro')
    nombre = input('Nombre: ')
    frutas.append(nombre)
    print('agregado con exito')

def insertar_registro():
    print('         insertar registro')
    nombre = input('nombre: ')
    pos = int(input('Posición: '))
    frutas.insert(pos, nombre)
    print('exitoso')

def mostrar_registros():
    print('         mostrar registro')
    if len(frutas) > 0:
        for fruta in frutas:
            print(fruta)
    else:
        print('No hay registros')

def buscar_registro():
    print('         buscar registro')
    if len(frutas) > 0:
        nombre = input('nombre que queres buscar: ')
        if nombre in frutas:
            cantidad = frutas.count(nombre)
            inicio = 0
            for i in range(cantidad):
                pos = frutas.index(nombre, inicio)
                print(f'{nombre} se encuentra en la pos: {pos+1}')
                incio = pos + 1
        else:
            print(f'{nombre} no se ha registrado')
    else: 
        print('no se han agregado frutas')

def eliminar_registro():
    print('eliminar registro')
    if len(frutas) > 0:
        for i in range(len(frutas)):
            print(f'{i+1}. {frutas[i]}')
        print('0. Cancelar')
        pos = int(input(f'posicion a eliminar (1- {len(frutas)})'))
        if 0 < pos <= len(frutas):
            frutas.pop(pos-1)
            print('eliminado con exito')
        else: 
            print('no se eliminara ningun registro')
    else:
        print('no se han afregado frutas')

def ordenar_registros():
    print('         ordenar frutas')
    if len(frutas) > 0:
        frutas.sort()
        print('registros ordenados alfabeticamente')
    else: 
        print(' no sehan agregado frutas')

def limpiar_registros():
    print(' limpiar frutas')
    frutas.clear()
    print('los registros han sido borrados.')

def main():
    continuar = True
    while continuar:
        menu()
        opc = int(input('selecciona una opción: '))
        os.system('cls')
        if opc == AGREGAR:
            agregar_registro()
        elif opc == INSERTAR:
            insertar_registro()
        elif opc == MOSTRAR:
            mostrar_registros()
        elif opc == BUSCAR:
            buscar_registro()
        elif opc == ELIMINAR:
            eliminar_registro()
        elif opc == ORDENAR:
            ordenar_registros()
        elif opc == LIMPIAR:
            limpiar_registros()
        elif opc == SALIR: 
            print('nos vemos..')
            continuar = False
        else:
            print('Opción no valida')
        input('Presiona enter para continuar')

if __name__ == '__main__':
    main()