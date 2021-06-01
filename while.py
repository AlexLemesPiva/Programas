
#Multipicadores

print('         Multiplicadores')

suma = 0
multiplicacion = 1
numero = -1

while numero != 0:
    numero = int(input('Enter a number: '))
    if numero % 2 == 0:
        suma = suma + numero
    else: multiplicacion = multiplicacion * numero
    print(f'suma: {suma}')
    print(f' multiplicacion: {multiplicacion}')
