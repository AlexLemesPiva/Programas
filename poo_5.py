''' 
deportista utilizando herencia 
'''
from persona import Persona
from poo_4 import Deportista

def main():
    per1 = Persona()
    deportista = Deportista()

    print(f'''Datos de la persona: {per1}''')
    print(f'''Datos del deportists : {deportista}''')

if __name__ == '__main__':
    main()