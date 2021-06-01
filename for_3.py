'''

Countdown

'''

import os
import time

for numero in range (10, -1, -1): #esto es para ir hacia atrás
    os.system('cls')
    print(f'{numero}')
    time.sleep(1) #timer de 1 segundo para seguir leyendo el código.
