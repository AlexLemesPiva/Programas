'''
def indentificador (por_posición; *args, **kwargs):
    instrucciones


Menu genérico. El procedimiento debera recibir el titulo del menu como primer argumento
seguido de las opciones a imprimir y finalmente un parametro
con nombre para el mensaje de error en caso de la opción no valida.
    
'''

def menu(titulo, *args, **kwargs):
    print(f'                {titulo}')
    for i in range(len(args)):
        print(f'{i+1} {args[1]}')
    opc = int(input('Seleciona una opción: '))
    if 1 <= opc <= len(args):
        print(f'seleccionaste la opción {args[opc-1]}')
    else:
        print('Opcion no valida')
        if 'error' in kwargs:
            print(f'{kwargs["error"]}')

