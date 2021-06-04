'''
main para estudiante
'''

from estudiante import Estudante

def main():
    nombre = input('Nombre: ')
    edad = input('Edad: ')
    promedio = float(input('Promedio: '))
    codigo = int(input('Código: '))

    estudiante = Estudante(nombre, edad, promedio, codigo)

    print(f'''Los datos del estudiante son:
    {estudiante}''')
    print('*'*50)
    estudiante.estudiar('Python')
    estudiante.estudiar('Flak')

 
if __name__ == '__main__':
    main()
