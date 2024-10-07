from abc import ABC, abstractmethod
from Transportar import Transportar


class Transporte(Transportar, ABC):
    def __init__(self, tipoTransporte, velocidadPromedio, valorKm):
        self._tipoTransporte = tipoTransporte
        self._velocidadPromedio = velocidadPromedio
        self._valorKm = valorKm
    
    def getVelocidadPromedio(self):
        return self._velocidadPromedio
    
    @abstractmethod
    def transportarPaquete(self,distancia,peso):
        pass
    
    def getTipoTransporte(self):
        return self._tipoTransporte