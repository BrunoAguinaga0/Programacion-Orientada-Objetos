from Transporte import Transporte


class Furgoneta(Transporte):
    def __init__(self, tipoTransporte, velocidadPromedio, valorKm):
        super().__init__(tipoTransporte, velocidadPromedio, valorKm)
    
    
    def transportarPaquete(self, distancia, peso):
        if peso > 5 and peso <= 100:
            return (0.7 * (distancia / self._velocidadPromedio) + 0.3 * (self._valorKm * distancia))
        else:
            return -1