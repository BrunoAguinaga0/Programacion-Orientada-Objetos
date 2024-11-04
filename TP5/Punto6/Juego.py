from abc import ABC, abstractmethod


class Juego(ABC):  # Clase padre que podria ser una interfaz.
    def __init__(self, id_juego: int, nombre: str, importe: float) -> None:
        self._idJuego = id_juego
        self._nombre = nombre
        self._importe = importe

    @abstractmethod
    def get_precio(self) -> None:
        pass

    def get_nombre(self):
        return self._nombre
