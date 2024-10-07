

class biblioteca:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._libros = []

    def getLibros(self):
        return self._libros

    def setLibros(self, libro):
        self._libros.append(libro)