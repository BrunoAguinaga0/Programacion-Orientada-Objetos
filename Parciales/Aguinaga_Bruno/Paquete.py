

class Paquete:
    def __init__(self,idPaquete,tipoArticulo, distancia, ancho, alto, longitud):
        self.__tipoArticulo = tipoArticulo
        self.__idPaquete = idPaquete
        self.__distancia = distancia
        self.__ancho = ancho
        self.__alto =  alto
        self.__longitud =  longitud
    
    def getDistancia(self):
        return self.__distancia
    
    def getPesoVolumetrico(self):
        return (self.__ancho * self.__alto * self.__longitud) / 5000
    
    def __str__(self):
        return f"Articulo: {self.__tipoArticulo} ID: {self.__idPaquete} \nDistancia: {self._distancia} \nPeso: {self.pesoVolumetrico()} \nAncho: {self._ancho} \nAlto: {self._alto} \nLongitud: {self._longitud}"