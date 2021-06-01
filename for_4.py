'''
Calcular un promedio, solicitamos valores, mostramos os valores y retornamos o promedio
'''

acumulador = 0

print('Vamos a calcular un promedio')
numerototal = int(input('Ingrese un valor '))
    
for valor in range(numerototal):
    numero = int(input(f'Ingrese el valor {valor+1}: '))
    acumulador += numero

promedio = acumulador / numerototal

print(f'tu promedio es: {promedio}')
