from abc import ABC,abstractmethod

class TarifaProvedor(ABC):
    
    def __init__(self,nombre,cantidadMensajes,cantidadMinutosLlamadas,cantidadGigas):
        self._nombre = nombre
        self._cantidadMensajes = cantidadMensajes
        self._mensajeTexto = 1
        self._cantidadMinutosLlamadas = cantidadMinutosLlamadas
        self._minutoLlamada = 15
        self._cantidadGigas = cantidadGigas
        self._gigas = 20
        
    def calcularSMS(self):
        return self._cantidadMensajes * self._mensajeTexto
    
    def calcularConsumoLlamada(self):
        return self._cantidadMinutosLlamadas * self._minutoLlamada
    
    def calcularGigas(self):
        return self._gigas + self._cantidadGigas    
    @abstractmethod
    def getNombre(self):
        return self._nombre