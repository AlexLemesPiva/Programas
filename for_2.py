#imprimir numeros del 2 al 20 usando for

print('prigramas que muestra los numeros pares desde el 2 hasta el 20')

print ('Metodo 1')

for numero in range (11): #este el programador no utilizó pero también está bien.
    print(f'Numeros: {numero*2}')
    print('*'*20)

print('Metodo 2')

for numero in range (2, 21):
    if numero %2 == 0:
        print(f'Numero: {numero}')

print('Metodo 3')

for par in range(2, 21, 2): #Aca se usa el incremental de 2 al final
    print(f'par: {par}')
