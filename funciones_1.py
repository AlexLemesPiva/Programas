'''
Funciones como estruturar

def identificador():
    instrucciones
    return valor_retorno
luego,
print (descri´ción del programa)
calculo de la funcion
print (f'con el valor de lafuncion')

'''

def calcular_imc():
    peso = float(input('Ingrese su peso: '))
    altura = float(input('Su altura: '))
    imc = peso / (altura ** 2)
    return imc

print('calcular masa corporal')
imc = calcular_imc()
print(f'tu indice de masa corporal es: {imc :.2f}')