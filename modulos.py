'''
conversiones:
segundos a minutos: devolve minutos e segundos
segundos a horas: de volvie horas minutos e segundos
minuto a segundos: recebe minutos e segundos e devolve segundos
minutos a horas: recebe minutos e segundos e devolve hora minuto e segundo

'''

SEGXMIN = 60
MINXHORA = 60

def segundos_a_min(segundos):
    mins = segundos // SEGXMIN
    segs = segundos % SEGXMIN

    return mins, segs

def minutos_a_seg(minutos, segundos):
    segs = minutos * SEGXMIN + segundos

    return segs

def minutos_a_horas(minutos, segundos):
    h = minutos // MINXHORA
    m = minutos % MINXHORA
    s = segundos

    return h, m, s

def segundos_a_horas(segundos):
    mins, segs = segundos_a_min(segundos)
    hrs, mins, segs = minutos_a_horas(mins, segs)

    return hrs, mins, segs



           