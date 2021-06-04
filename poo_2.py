'''
crear un objeto tipo ingrediente. los ingredientes serán modelados dentro de una clase en un modulo separado y tendran los siguientes
atibutos:
- nombre
- cantidad
- unidad de medida
además la clase Ingrediente podrá recibir como argumentos los vcalores iniciales para sus atributos a través del método constructor
'''
from ingrediente import Ingrediente

def main():
    ingrediente = Ingrediente('Papa', 3, 'Kilos')

    print(ingrediente)

if __name__ == '__main__':
    main()