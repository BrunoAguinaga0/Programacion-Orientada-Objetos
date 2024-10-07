from abc import ABC, abstractmethod


class Prestarable(ABC):
    @abstractmethod
    def prestar(self):
        pass
    
    @abstractmethod
    def devolver(self):
        pass