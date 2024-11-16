from Estrategia import Estrategia


class PerfilAdolecente(Estrategia):
    def __init__(self, nombre, edad):
        self._edad = edad
        self._nombre = nombre

    def listar_peliculas(self, peliculas):
        for pelicula in peliculas:
            if pelicula[1] < 18:
                print("Pelicula:", pelicula[0], "Clasificacion: ADOLECENTE")
