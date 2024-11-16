from Estrategia import Estrategia


class PerfilNiños(Estrategia):
    def __init__(self, nombre, edad):
        self._edad = edad
        self._nombre = nombre

    def listar_peliculas(self, peliculas):
        for pelicula in peliculas:
            if (
                pelicula[1] < 13
            ):  # Se supone que pelicula[1] es la edad minima para ver esa pelicula
                print("Pelicula:", pelicula[0], "Clasificacion: ATP")
