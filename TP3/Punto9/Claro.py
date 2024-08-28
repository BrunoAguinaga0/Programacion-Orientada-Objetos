from TarifaProvedor import TarifaProvedor

class Claro(TarifaProvedor):
    def __init__(self,nombre,cantidadMensajes,cantidadMinutosLlamadas,cantidadGigas):
        super().__init__(nombre,cantidadMensajes,cantidadMinutosLlamadas,cantidadGigas)
        
    def calcularSMS(self):
        return super().calcularSMS() * 1.20
    
    def calcularGigas(self):
        return super().calcularGigas() * 1.20
    
    def calcularConsumoLlamada(self):
        return super().calcularConsumoLlamada() * 1.20
    
    def getNombre(self):
        return super().getNombre()

