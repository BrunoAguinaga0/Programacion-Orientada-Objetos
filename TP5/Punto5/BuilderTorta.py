from abc import ABC, abstractmethod

class BuilderTorta(ABC):

    @property
    @abstractmethod
    def get_torta(self) -> None:
        pass
    
    @abstractmethod
    def produce_relleno(self) -> None:
        pass
    
    @abstractmethod
    def produce_masa(self) -> None:
        pass
    
    @abstractmethod
    def produce_decoracion(self) -> None:
        pass