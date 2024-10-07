from Transporte import Transporte


class Cartero(Transporte):
    def __init__(self, tipoTransporte, velocidadPromedio, valorKm):
        super().__init__(tipoTransporte, velocidadPromedio, valorKm)

    def transportarPaquete(self, distancia, peso):
        if peso <= 5:
            return (0.2 * (distancia / self._velocidadPromedio) + 0.8 * (self._valorKm * distancia))
        else:
            return -1