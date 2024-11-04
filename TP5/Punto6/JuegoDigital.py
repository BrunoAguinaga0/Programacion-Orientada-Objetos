from Juego import Juego


class JuegoDigital(Juego):
    def __init__(self, id_juego: int, nombre: str, importe: float) -> None:
        super().__init__(id_juego, nombre, importe)
        self.__plataforma = 1.2

    def get_precio(self):
        return self._importe * self.__plataforma
