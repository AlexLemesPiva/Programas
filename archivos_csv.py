'''
Solicita al usuario registrar y almacenar peliculas usando .csv para posteriormente recuperarlos
'''

import os
import csv
from modulos import minutos_a_horas

def registrar_peliculas(nombre_archivo):
    cantidad = int(input('Cuantas pelis queres agregar?: '))
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=',')
        for i in range(cantidad):
            os.system('cls')
            titulo = input('Titulo: ')
            duracion = input('Duración: ')
            anio = input('Año: ')
            writer.writerow([titulo, duracion, anio])



def recuperar_peliculas(nombre_archivo):
    os.system('cls')
    print('Peliculas registradas')
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for linea in reader:
            print(f'Título: {linea[0]}')
            minutos = int(linea[1])
            h, m, s = minutos_a_horas(minutos, 0)
            print(f'Duración: {h}:{m}:{s}')
            print(f'Año: {linea[2]}')
            print('*'*50)

def main():
    archivo = 'peliculas.csv'
    registrar_peliculas(archivo)
    recuperar_peliculas(archivo)

if __name__ == '__main__':
    main()
