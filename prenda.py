'''
definicion pra la clase prenda con los atributos

tipo 
talla
'''

class Prenda:
    def __init__(self):
        self._tipo = ''
        self._talla = ''
    def __str__(self):
        return f'''Tipo: {self.tipo}
Talla: {self.talla}'''

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,valor):
        self._tipo = valor
    @tipo.deleter
    def tipo(self):
        del self._tipo

    @property
    def talla(self):
        return self._talla
    @talla.setter
    def talla(self,valor):
        self._talla = valor
    @talla.deleter
    def talla(self):
        del self._talla
