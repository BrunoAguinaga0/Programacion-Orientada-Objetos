from Multimedia import Multimedia

class Pelicula(Multimedia):
    def __init__(self, nombre, anioEmision, calificacion):
        super().__init__(nombre, anioEmision, calificacion)
        self.__visto = False
    
    def reproducir(self):
        super().reproducir()
        self.__visto = True
        
    def visto(self):
        return self.__visto
