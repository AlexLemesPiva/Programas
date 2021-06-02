'''
Agenda con archivos abierto para recurrir a la base de datos
'''
import pathlib
import os

AGREGAR = 1
BUSCAR = 2
MOSTRAR = 3
SALIR = 4

def menu():
    os.system('cls')
    print(f'''            AGENDA PERSONALZIADA
    {AGREGAR})  AGREGAR CONTACTO
    {BUSCAR})   BUSCAR CONTACTO
    {MOSTRAR})  MOSTRAR CONTACTO
    {SALIR})   SALIR''')

def cargar_agenda(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contacto, telefono, email = linea.strip().split(',')
                agenda.setdefault(contacto, (telefono, email))
    else:
        with open(nombre_archivo, 'w') as archivo:
            pass

def agregar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('         Agregar Contacto\n')
    nombre = input('Nombre: ')
    if agenda.get(nombre):
        print('El contacto ya existe')
    else:
        telefono = input('Telefono: ')
        correo = input('Email: ')
        agenda.setdefault(nombre, (telefono, correo))
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f'{nombre}, {telefono}, {correo}\n')
        print('Contacto agregado con éxito.')
    input('Presiona enter para continuar')


def buscar_contacto(agenda):
    os.system('cls')
    print('         Buscar contacto\n')
    nombre = input('Nombre: ')
    if len(agenda) > 0:
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'E-mail: {datos[1]}')
                print('~~'*40)
                encontrados += 1
        if encontrados == 0:
            print('No se encontró el contacto.')
        else:
            print(f'Se encontraron {encontrados} contactos.')
    else:
        print('No se encontraron contactos.')
    input('Presiona enter para continuar')
        
def mostrar_contacto(agenda):
    os.system('cls')
    print('     Contactos de tu agenda\n')
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f'Nombe: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'E-mail: {datos[1]}')
            print('~~'*40)
    else:
        print('No se encontraron contactos')
    input('Presiona enter para continuar')

def main():
    continuar = True
    agenda = dict()
    nombre_archivo = 'agenda.txt'
    cargar_agenda(agenda, nombre_archivo)

    while continuar:
        menu()
        opc = int(input('Elija una opción: '))

        if opc == AGREGAR:
            agregar_contacto(agenda, nombre_archivo)
        elif opc == MOSTRAR:
            mostrar_contacto(agenda)
        elif opc == BUSCAR:
            buscar_contacto(agenda)
        elif opc == SALIR:
            continuar = False
    else:
        print('Opción no válida')
    input('Press enter to continue')
print('Nos vemos')

if __name__ == '__main__':
    main()