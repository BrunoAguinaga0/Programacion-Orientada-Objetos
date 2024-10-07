from Publicacion import Publicacion


class Revista(Publicacion):
    def __init__(self, nombre, anioPublicacion, ISBN, nro):
        super().__init__(nombre, anioPublicacion, ISBN)
        self._nro = nro
    
    
    def getNro(self):
        return self._nro