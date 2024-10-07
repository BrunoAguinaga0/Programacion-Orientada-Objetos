from abc import ABC, abstractmethod

class Publicacion(ABC):
    def __init__(self, nombre, anioPublicacion, ISBN):
        self._nombre = nombre
        self._anioPublicacion = anioPublicacion
        self._ISBN = ISBN