from abc import ABC, abstractmethod


class Component(ABC):
    def add(self, component):
        pass

    def remove(self, component):
        pass

    def es_carpeta(self):
        pass

    @abstractmethod
    def operacion(self):
        pass
