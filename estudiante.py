'''
estudiante.py

script que solicite la información de un objeto de tipo Estudiande y posteriormente imprima en la pantalla sus datos.
Las clases Estudiante heredará de la clase Persona, osea un tipo particular de persona.
Atributos:
    Promedio
    Código de estudiante
Comportamiento: 
    Estudiar una materia
Finalmente hacer que el estudiante ejecute el Comportamiento "estudiar"

'''

from persona import Persona

class Estudante(Persona):
    def __init__(self, nombre ='', edad=None, promedio=None, codigo=''):
        self._nombre = nombre
        self._edad = edad
        self._promedio = promedio
        self._codigo = codigo
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, valor):
        self._edad = valor
    @edad.deleter
    def edad(self):
        del self._edad

    @property
    def promedio(self):
        return self._promedio
    @promedio.setter
    def promedio(self, valor):
        self._promedio = valor
    @promedio.deleter
    def promedio(self):
        del self._promedio

    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor
    @codigo.deleter
    def codigo(self):
        del self._codigo

    def estudiar(self, materia):
        print(f'{self.nombre} está estudiando {materia}')

    def __str__(self):
        return f'''{super().__str__()}
        Código: {self.codigo}
        Promedio: {self.promedio}'''