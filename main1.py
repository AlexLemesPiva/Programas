'''
conversiones:
segundos a minutos: devolve minutos e segundos
segundos a horas: de volvie horas minutos e segundos
minuto a segundos: recebe minutos e segundos e devolve segundos
minutos a horas: recebe minutos e segundos e devolve hora minuto e segundo

'''
import os
SEGXMIN = 60
MINXHORA = 60
SEGUNDOSAMINUTOS = 1
SEGUNDOSAHORA = 2
MINUTOSASEGUNDOS = 3
MINUTOSAHORAS = 4
SALIR = 5

def segundos_a_min(segundos):
    mins = segundos // SEGXMIN
    segs = segundos % SEGXMIN

    return mins, segs

def minutos_a_seg(minutos, segundos):
    segs = minutos * SEGXMIN + segundos

    return segs

def minutos_a_horas(minutos, segundos):
    hrs = minutos // MINXHORA
    mins = minutos % MINXHORA
    segs = segundos

    return hrs, mins, segs

def segundos_a_horas(segundos):
    mins, segs = segundos_a_min(segundos)
    hrs, mins, segs = minutos_a_horas(mins, segs)

    return hrs, mins, segs

def menu():
    print(f'''          menU

    1) SEGUNDOSAMINUTOS
    2) SEGUNDOSAHORA
    {MINUTOSASEGUNDOS}) MINUTOSASEGUNDOS
    4) MINUTOSAHORAS
    5) SALIR
    ''')

def main():
    continuar = True
    while continuar:
        os.system('cls')
        menu()
        opc = int(input('selecciona una opción: '))
        os.system('cls')
        if opc == SEGUNDOSAMINUTOS:
            s = -1
            while 0 > s:
                s = int(input('Cantida de segundos a convertir: '))
            mins, segs = segundos_a_min(s)
            print(f'el equivalente es {mins}: {segs}')
        elif opc == SEGUNDOSAHORA:
            s = -1
            while 0 > s:
                s = int(input('Cantida de seugndos a convertir: '))
            hrs, mins, segs = segundos_a_horas(s)
            print(f'el equivalente es {hrs}:{mins}:{segs}')
        elif opc == MINUTOSASEGUNDOS:
            m = -1 
            while 0 > m:
                m = int(input('cantidad de minutos a convertir: '))
            s = -1
            while 0 > s or s >= SEGXMIN:
                s = int(input('cnatida de seg a convertir: '))
            segs = minutos_a_seg(m, s)
            print(f'el equivalente es {segs}')
        elif opc == MINUTOSAHORAS:
            m = -1
            while 0 > m:
                m = int(input('cantida de minutos a converitr: '))
            s = -1
            while 0 > s and s >= SEGUNDOSAMINUTOS:
                s = int(input(f'ingrese segundos a convertir: '))
            hrs, mins, segs = minutos_a_horas(m, s)
            print(f'el equivalente es {hrs}:{mins};{segs}')
        elif opc == SALIR:
            continuar = False
        else:
            print('Opción no válida')
        input('Presiona enter para continuar')
if __name__ == '__main__':
    main()
           