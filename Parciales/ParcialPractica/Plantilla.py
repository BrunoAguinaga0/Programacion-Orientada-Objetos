

class Plantilla():
    def __init__(self, usuario, paisfavorito, equipofavorito):
        self.__plantilla = []
        self.__propietario = usuario
        self.__paisfavorito = paisfavorito
        self.__equipofavorito = equipofavorito
    
    
    def imprimirPlantilla(self):
        print(f"=== Plantilla de: {self.__propietario} ===")
        print(f"Pais Favorito: {self.__paisfavorito} - Equipo Favorito: {self.__equipofavorito}")
        print(f"Quimica del Equipo: {self.__quimicaTotal()}")
        for carta in self.__plantilla:
            carta.imprimirCarta(self.__paisfavorito,self.__equipofavorito)
    
    
    def __quimicaTotal(self):
        quimica = 0
        for carta in self.__plantilla:
            quimica += carta.calcularQuimica(self.__paisfavorito, self.__equipofavorito)
        return int(quimica / len(self.__plantilla))
    
    def agregarPlantilla(self,plantilla):
        self.__plantilla = plantilla