'''
Cronometro em formato de 24 horas limpiando la pantalla entre cada parte que muda el cronometro
'''

import os
import time


for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system('cls')
            print(f'{hora}:{minuto}:{segundo}')
            time.sleep(1)

