from Creator import Creator
from JuegoDigital import JuegoDigital


class ConcretJuegoDigital(Creator):
    def factory_method(self, id, nombre, importe) -> None:
        return JuegoDigital(id, nombre, importe)
