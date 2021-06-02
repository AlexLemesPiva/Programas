'''
scrypt que implemente una agenda de contactos haciendo uso de diccionario
Para el diccionario, las llaves seran los nombres de los contactos, y como valor 
estara una tupla que contenta telefono y e-mail.
'''

import os

SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5

def menu():
    os.system('cls')
    print(f'''            AGENDA PERSONALZIADA
    {AGREGAR})  AGREGAR CONTACTO
    {MOSTRAR}) MOSTRAR CONTACTO
    {BUSCAR})  BUSCAR CONTACTO
    {MODIFICAR}) MODIFICAR CONTCTO
    {ELIMINAR}) ELIMINAR CONTACTO
    {SALIR})   SALIR''')

def agregar_contacto(agenda):
    os.system('cls')
    print('         Agregar contacto')
    nombre = input('Nombre: ')
    if agenda.get(nombre):
        print('Ya existe el contacto')
    else:
        telefono = input('Teléfono: ')
        correo = input('Correo: ')
        agenda.setdefault(nombre, (telefono, correo) )
        print('Contacto agendado con éxito')

def mostrar_contacto(agenda):
    os.system('cls')
    print('         Mis contactos')
    if len(agenda) > 0 :
        for contacto, datos in agenda.items():
            print(f'Nombe: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'E-mail: {datos[1]}')
            print('~~'*40)
    else:
        print('No se encontraron contactos')

def buscar_contacto(agenda):
    os.system('cls')
    print('         Buscar contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'E-mail: {datos[1]}')
                print('~~'*40)
                encontrados += 1
        if encontrados == 0:
            print('No se encontró el contacto')
        else:
            print(f'Se encontraron {encontrados} contactos.')
    else:
        print('No hay contactos registrados')

def modificar_contacto(agenda):
    os.system('cls')
    print('         Modificar contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            datos = agenda.get(nombre)
            print('Información actual: ')
            print(f'Nombre: {nombre}')
            print(f'Telefono: {datos[0]}')
            print(f'E-mail: {datos[1]}')
            print('*'*50)
            print('Ingresa los nuevos datos')
            telefono = input('Telefono: ')
            correo = input('Correo: ')
            agenda[nombre] = (telefono, correo) #Tengo que usar corchetes por que el setdefault solamente me regresa los valores.
            print('Datos actualizados con exito')
        else:
            print('No existe el contacto')
    else:
        print('no hay contactos registrados')

def eliminar_contacto(agenda):
    os.system('cls')
    print('             Eliminar contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            agenda.pop(nombre)
            print('Contacto eliminado con éxito')
        else:
            print('No existe el contacto')
    else:
        print('No hay contactos registrados.')

#todo Lo anterior era para definir funciones, ahora definimos como funciona todo.

def main():
    continuar = True
    mi_agenda = {} #Acá es donde se crea el diccionário, y el mismo arranca vacío
    while continuar:
        menu()
        opc = int(input('Selecciona una opción: '))

        if opc == AGREGAR:
            agregar_contacto(mi_agenda)
        elif opc == MOSTRAR:
            mostrar_contacto(mi_agenda)
        elif opc == BUSCAR:
            buscar_contacto(mi_agenda)
        elif opc == MODIFICAR:
            modificar_contacto(mi_agenda)
        elif opc == ELIMINAR:
            eliminar_contacto(mi_agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opción no válida')
        input('Press enter to continue')
    print('Nos vemos')

if __name__ == '__main__':
    main()