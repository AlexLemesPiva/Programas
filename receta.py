'''
receta.py
modelo sencillo de una receta de cocina
atributos:
    ingrediente -- lista
    pasos  -- lista
    nombre -- nombre de la receta
comportamientos:
    Menu   -- menu de operaciones
    agregar_ingrediente
    Consultar_ingredientes
    agregar_pasos
    consultar_pasos
'''
from ingrediente import Ingrediente
import os

class Receta:
    OPC_AGREGAR_INGREDIENTE = 1
    OPC_CONSULTAR_INGREDIENTES = 2
    OPC_AGREGAR_PASO = 3
    OPC_CONSULTAR_PASO = 4
    OPC_SALIR = 0

    def __init__(self, nombre=''):
        self._nombre = nombre
        self._ingredientes = []
        self._pasos = []

    def __str__(self):
        s = f'''          {self.nombre}\n'''
        s += ' Ingredientes: \n'
        for ingredientes in self.ingredientes:
            s += f'''{ingredientes}\n'''
        s += '\n Pasos: \n'
        for i, paso in enumerate(self.pasos):
            s += f''' {i+1}. {paso}\n'''
        return s


    @property
    def nombre(self):
        return  self._nombre
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def ingredientes(self):
        return  self._ingredientes
    @ingredientes.setter
    def ingredientes(self, valor):
        self._ingredientes = valor
    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes

    @property
    def pasos(self):
        return  self._pasos
    @pasos.setter
    def pasos(self, valor):
        self._pasos = valor
    @pasos.deleter
    def pasos(self):
        del self._pasos

    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f'''          {self.nombre}
            {self.OPC_AGREGAR_INGREDIENTE}) Agregar ingrediente
            {self.OPC_CONSULTAR_INGREDIENTES}) Consultar ingredintes
            {self.OPC_AGREGAR_PASO}) Agregar Paso
            {self.OPC_CONSULTAR_PASO}) Consultar Pasos
            {self.OPC_SALIR}) Salir''')

            opc = int(input('Selecciona una opción: '))
            if opc == self.OPC_AGREGAR_INGREDIENTE:
                self.agregar_ingrediente()
            elif opc == self.OPC_CONSULTAR_INGREDIENTES:
                self.consultar_ingredientes()
            elif opc == self.OPC_AGREGAR_PASO:
                self.agregar_paso()
            elif opc == self.OPC_CONSULTAR_PASO:
                self.consultar_pasos()
            elif opc == self.OPC_SALIR:
                continuar = False
            else:
                print('Opción no válida')
            input('Press enter to continue...')



    def agregar_ingrediente(self):
        continuar = True

        while continuar:

            os.system('cls')
            print('         Agregar ingrediente')
            nombre = input('Nombre: ')
            cantidad = -1
            while cantidad <= 0:
                cantidad = input('Cantidad: ')
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0
            unidad = input('Unidad de medida: ')
            ingrediente = Ingrediente(nombre, cantidad, unidad)
            self.ingredientes.append(ingrediente)

            respuesta = input('Deseas agregar otro ingrediente? (s/n)')
            if respuesta != 's' and respuesta != 'S':
                continuar = False


    def consultar_ingredientes(self):

        os.system

        print('         Ingredientes')
        if len(self.ingredientes) == 0:
            print('No hay ingredintes registrados')
        else:
            for ingrediente in self.ingredientes:
                print(f'{ingrediente}')
    
    def agregar_paso(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('         Agrear Paso')
            paso = input('Paso: ')
            self.pasos.append(paso)
            respuesta = input('Deseas agregar otro paso? (s/n)')
            if respuesta != 's' and respuesta != 'S':
                continuar = False

    def consultar_pasos(self):
        os.system('cls')
        print('     Consultar Pasos')
        if len(self.pasos) == 0:
            print('No hay pasos registrados.')
        else:
            for i, paso in enumerate(self.pasos):
                print(f'{i+1}. {paso}')
