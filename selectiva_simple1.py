'''
perguntar idade ao usuario e se for maior que 18 dizer que ele é maior de idade
'''

import random

secreto = random.randint(1,10)
numero = int(input('que numero vc acha que é?: '))
if numero == secreto:
    print('acertou miseravi')
