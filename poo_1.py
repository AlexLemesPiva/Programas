'''
script que importe la clase prenda para después crear dos objetos e imprimir su información en pantalla.
'''
from prenda import Prenda

def main():
    playera = Prenda()
    
    playera.tipo = 'Playera con estampado.'
    playera.talla = 'M'

    print(playera)

if __name__ == '__main__':
    main()