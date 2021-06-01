'''

saludo personalizado que dice aparte si tenes o no mas de 18 años

'''

def saludo(nombre):
    if edad >= 18:
        print(f'hola {usuario}, ya sos mayor a 18')
    else:
        print(f'hola {usuario}, todavia sos menor de edad')

usuario = input('Como te llamas? ')
edad = int(input('Que edad tenes? '))

saludo(usuario)