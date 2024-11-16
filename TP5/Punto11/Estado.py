from abc import ABC, abstractmethod


class Estado(ABC):
    @abstractmethod
    def actividad(self):
        pass

    @abstractmethod
    def abrir_caja(self):
        pass

    @abstractmethod
    def cerrar_caja(self):
        pass

    @abstractmethod
    def suspender_caja(self):
        pass
