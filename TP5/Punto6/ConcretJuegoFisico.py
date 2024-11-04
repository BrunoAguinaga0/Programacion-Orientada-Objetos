from Creator import Creator
from JuegoFisico import JuegoFisico


class ConcretJuegoFisico(Creator):
    def factory_method(self, id, nombre, importe) -> None:
        return JuegoFisico(id, nombre, importe)
