'''
implementar una clase persona con las siguientes propriedades:

nombre, edad

Ademas se deberan agrear los comportamientos:
hablar(mensaje) - mensaje: el mensaje que dirá la persona.
comer(alimento) - alimento: el alimento que consume la persona.
'''


from typing import Awaitable


class Persona:

    def __init__(self):
        self._nombre =''
        self._edad =None

    @property
    def nombre(self):
        return self._nombre #regresa lo que hay en el atributo privado
    
    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor

    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def edad(self):
        return self._edad #regresa lo que hay en el atributo privado
    
    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @edad.deleter
    def edad(self):
        del self._edad

    def hablar(self, mensaje):
        print(f'{self.nombre}: {mensaje}')

    def __str__(self):
        return f'''Nombre: {self.nombre}
Edad: {self.edad}'''

def main():
    persona1 = Persona()
    persona2 = Persona()

    persona1.nombre = 'Brasu'
    persona1.edad = 20
    persona2.nombre = 'Ale'
    persona2.edad = 50

    print(f'Nombre {persona1.nombre}')
    print(f'Edad: {persona1.edad}')

    persona1.hablar(f'Hola {persona2.nombre}')
    persona2.hablar(f'hola {persona1.nombre}')

if __name__ == '__main__':
    main()
