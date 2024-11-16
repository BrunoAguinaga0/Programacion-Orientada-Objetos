class Multimedia:
    def __init__(self, peliculas, estrategia):
        self._peliculas = peliculas
        self._estrategia = estrategia

    def set_estrategia(self, estrategia):
        self._estrategia = estrategia

    def consultar_catalogo(self):
        self._estrategia.listar_peliculas(self._peliculas)
