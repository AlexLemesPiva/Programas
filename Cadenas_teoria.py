'''
JUEGO DEL AHORCADO

'''
import random
import os
MAXFALLO = 6

paises = ['Estados Unicos', 'Argentina', 'Brasil', 'Ecuador','Venezuela','México','Chile','Uruguay','Colombia','Bolivia','Peru',
 'Paraguay', 'Puerto Rico']

def crear_cadenas():
     pais = random.choice(paises)
     secreto = '_'*len(pais)
     return pais, secreto

def reemplazar_simbolo(original, secreto, simbolo):
    cantidad = original.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo + secreto[pos+1:]
        inicio = pos + 1
    return secreto

def ahorcado():
    print('jugar al ahorcado')
    input('Presiona enter para comenzar')
    original, secreto = crear_cadenas()
    fallos = 0
    while secreto != original and fallos < MAXFALLO:
        os.system('cls')
        print(f'Palabra: {secreto}')
        s = input('Ingrese una letra: ')
        if s in original:
            secreto = reemplazar_simbolo(original, secreto, s)
            print('Bien hecho')
        else:
            print('Errou!')
            fallos += 1
        input('Enter para continuar')
    if secreto == original:
        print(f'Has ganado, el pais es: {secreto}')
    else:
        print(f'lo siento, el paisera {original}')

def main():
    ahorcado()

if __name__ == '__main__':
    main()