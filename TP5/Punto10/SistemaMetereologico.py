from Observador import Observador


class SistemaMetereologico:
    def __init__(self):
        self._observadores: list[Observador] = []
        self._clima = None

    def set_clima(self, clima):
        self._clima = clima
        self.notificar()

    def get_clima(self):
        return self._clima

    def notificar(self):
        for observador in self._observadores:
            observador.actualizar(self._clima)

    def suscribirse(self, observador):
        self._observadores.append(observador)

    def desuscribirse(self, observador):
        self._observadores.remove(observador)
