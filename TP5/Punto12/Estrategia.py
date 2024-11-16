from abc import ABC, abstractmethod


class Estrategia(ABC):
    @abstractmethod
    def listar_peliculas(self, peliculas):
        pass
