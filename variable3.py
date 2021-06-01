

nota = int(input('Cual fue tu nota? '))
resto = nota % 10
if resto >= 6:
    nota = nota + (10 - resto)
    print(f'{nota}')