'''
calcular el área de un triangulo. dicha funcion debera recibir como argumento el valor de la base y la altura
y regresara el área calculada.
'''

def calcular_area(base, altura):
    area = (base * altura) / 2
    return area
print('calcular base triangulo')
base = float(input('ingrese el valor de la base: '))
altura = float(input('ingrese el valor de la altura: '))

print(f'el area es: {calcular_area(base, altura)}')