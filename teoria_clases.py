'''
Creando clases

declaremos una clase figura  que digura como atributo la cantidad de lados
una vez creada la clase crear dos figuras objetos) y mostrar su cantidad de lados

'''
class Figura:
    def __init__(self): # en otros lenguajes se conoce como Constructor
       self._lados = None # ._lados atributos privados.

    @property #equivalente a un #getter: Rregresa el valor asociado a la cantidad de lados
    def lados(self):
        return self._lados
    
    @lados.setter #Permite asignarle valor al atriburo lados
    def lados(self, valor):
        self._lados = valor

    @lados.deleter
    def lados(self):
        del self._lados

def main():
    triangulo = Figura() # Creo una figura y lo guardo en la variable triangulo
    cuadrado = Figura()

    triangulo.lados = 3
    cuadrado.lados = 4

    print(f'El triángulo tiene: {triangulo.lados} lados.')
    print(f'El cuadrado tiene: {cuadrado.lados} lados')

if __name__ == '__main__':
    main()
