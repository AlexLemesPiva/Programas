'''
receta
'''

from receta import Receta

def main():
    receta = Receta('Pizza')
    
    receta.menu()
    print(receta)

if __name__ == '__main__':
    main()