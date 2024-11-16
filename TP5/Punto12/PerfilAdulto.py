from Estrategia import Estrategia


class PerfilAdulto(Estrategia):
    def __init__(self, nombre, edad):
        self._edad = edad
        self._nombre = nombre

    def listar_peliculas(self, peliculas):
        for pelicula in peliculas:
            print("Pelicula:", pelicula[0])
