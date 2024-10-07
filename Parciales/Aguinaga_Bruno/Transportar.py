from abc import ABC, abstractmethod

class Transportar(ABC):
    @abstractmethod
    def transportarPaquete(self):
        pass