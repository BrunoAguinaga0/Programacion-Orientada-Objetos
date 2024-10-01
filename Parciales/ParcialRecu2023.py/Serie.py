from Multimedia import Multimedia
from Capitulos import Capitulos

class Serie(Multimedia):
    def __init__(self, nombre, anioEmision, calificacion):
        super().__init__(nombre, anioEmision, calificacion)
        self.__capitulos = []
    
    def reproducir(self):
        super().reproducir()
        nro = self.__ultimoCapitulo_reproducido()
        for capitulo in self.__capitulos:
            if capitulo.__getNro() == nro:
                capitulo.__setReproducido()
                break
    
    def agregar_capitulo(self, capitulo):
        self.__capitulos.append(capitulo)
    
    def ultimoCapitulo_reproducido(self):
        for capitulo in self.__capitulos:
            if capitulo.getReproducido() == False:
                return capitulo.getNro()
                break

    def imprimirMultimedia(self):
        super().imprimirMultimedia()
        print(f"Ultimo capitulo reproducido: {self.ultimoCapitulo_reproducido()}")