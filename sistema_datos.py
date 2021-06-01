
BRASIL = 1
ARGENTINA = 2
PERU = 3
BOLIVIA = 4
MEXICO = 5

print('''         Capitales de América
1) Brasil
2) Argentina
3) Peru
4) Bolivia
5) Mexico
''')

opc = int(input('Escolha uma capital da lista '))

if opc == BRASIL:
    print('Brasilia')
elif opc == ARGENTINA:
    print('Buenos aires')
elif opc == PERU:
    print('Cusco')
elif opc == BOLIVIA:
    print('La Paz')
elif opc == MEXICO:
    print('Ciudad de México')
else: 
    print('Error')
