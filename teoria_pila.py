'''

critério: LIFO

el ultimo dato entrar es el primero en salir.

script que valida se una operación aritmética es balanceada

'''
def validar_expresion(expresion):
    pila = []
    for simbolo in expresion:
        if simbolo == '(':
            pila.append('(')
        elif simbolo == ')':
            if len(pila) > 0:
                pila.pop()
            else:
                return False
    return len(pila) == 0

def main():
    e = input('escribe una expresion: ')
    valida = validar_expresion(e)
    if valida:
        print('la expresión está balanceada')
    else:
        print('no está balanceada')

if __name__ == '__main__':
    main()
    