'''
programa de calificación
para aprobar: 60
Assitencia para aprobar: 60
'''
calificacion = int(input('Cual fue tu calificación? '))
asistencia = int(input('Cuantas asistencias tuviste? '))
if calificacion >= 60 and asistencia >= 30:
    print('Felicitaciones!!! estás aprobado')
if calificacion <= 60 and asistencia <= 30:
    print('Desaprobado!')