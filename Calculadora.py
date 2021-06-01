#Calculadoraaaa

SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISIONENTERA = 4
POTENCIA = 5
RESTODIVISION = 6

print('''           Calculadora
1) Suma
2) Resta
3) Multiplicacion
4) Division entera
5) Potencia
6) Resto de una Division
''')

opc = int(input('Elija una operacion: '))
if SUMA <= opc <= RESTODIVISION:

    valor1 = int(input('Ingrese un valor '))
    valor2 = int(input('Ingrese el otro valor '))

if opc == SUMA:
    print(f'{valor1} + {valor2} = {valor1+valor2}')
elif opc == RESTA:
    print(f'{valor1} - {valor2} = {valor1-valor2}')
elif opc == MULTIPLICACION:
    print(f'{valor1} * {valor2} = {valor1*valor2}')
elif opc == DIVISIONENTERA and valor2 != 0:
    print(f'{valor1} / {valor2} = {valor1/valor2}')
elif opc == POTENCIA:
    print(f'{valor1} ** {valor2} = {valor1**valor2}')
elif opc == RESTODIVISION:
    print(f'{valor1} % {valor2} = {valor1%valor2}')
else: print('Comando Inválido!')
