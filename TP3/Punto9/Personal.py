from TarifaProvedor import TarifaProvedor

class Personal(TarifaProvedor):
    def __init__(self,nombre,cantidadMensajes,cantidadMinutosLlamadas,cantidadGigas):
        super().__init__(nombre,cantidadMensajes,cantidadMinutosLlamadas,cantidadGigas)
        
    def calcularSMS(self):
        return super().calcularSMS
    
    def calcularConsumoLlamada(self):
        return super().calcularConsumoLlamada() * 1.20
    
    def calcularGigas(self):
        return super().calcularGigas() * 1.50
    
    def getNombre(self):
        return super().getNombre()