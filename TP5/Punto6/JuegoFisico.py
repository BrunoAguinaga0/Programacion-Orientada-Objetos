from Juego import Juego


class JuegoFisico(Juego):
    def __init__(self, id_juego: int, nombre: str, importe: float) -> None:
        super().__init__(id_juego, nombre, importe)
        self.__traslado = 300.0

    def get_precio(self):
        return self._importe + self.__traslado
