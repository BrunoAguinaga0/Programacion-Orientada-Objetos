from Publicacion import Publicacion
from Prestable import Prestable


class Libro(Publicacion, Prestable):
    def __init__(self, nombre, anioPublicacion, ISBN):
        super().__init__(nombre, anioPublicacion, ISBN)
        self._prestado = False

    def prestar(self):
        self._prestado = True
    
    def devolver(self):
        self._prestado = False
    
    def estaPrestado(self):
        if self._prestado:
            print("El libro se encuentra prestado")
            return True
        else:
            print("El libro no se encuentra prestado")
            return False