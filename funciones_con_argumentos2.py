'''

script que retorne conversión de horas a minutos e segundos. deve retornar o equivalente em segndos e segundos

'''
def hor_segundo(horas):
    return h * 3600
def hor_minuto(minuto):
    return h * 60

print('Conversor de Horas a minutos e segundos')

h = int(input('Ingrese a quantidade de horas: '))

print(f'El equivalente de {h} horas en segundos es: {hor_segundo(h)}')
print(f'El equivalente de {h} horas en minutos es: {hor_minuto(h)}')
