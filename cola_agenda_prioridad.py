'''
agenda con cola de proridad para los eventos

'''

import os
import queue

AGENDAR = 1
ATENDER = 2
SALIR = 0

def mostrar_menu():
    os.system('cls')
    print(f'''              mi agender
    {AGENDAR}) AGENDAR EVENTO
    {ATENDER}) ATENDER EVENTO
    {SALIR})   SALIR''')

def agendar_evento(ag):
    print('agendar evento')
    evento = input('Evento: ')
    ag.put(evento)

def atender_evento(ag):
    print('atender evento')
    if ag.empty():
        print('no hay eventos por atender')
    else:
        evento = ag.get()
        print(f'evento: {evento}')

def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        mostrar_menu()
        opc = int(input('Selecciona una opción: '))
        os.system('cls')
        if opc == AGENDAR:
            agendar_evento(agenda)
        elif opc == ATENDER:
            atender_evento(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('opc n valida')
        input('presiona enter para contnuar')
print('nos vemos')

if __name__ == '__main__':
    main()