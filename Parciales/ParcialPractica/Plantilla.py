

class Plantilla():
    def __init__(self, usuario, paisfavorito, equipofavorito):
        self._plantilla = []
        self._propietario = usuario
        self._paisfavorito = paisfavorito
        self._equipofavorito = equipofavorito
        
    def imprimirPlantilla(self):
        print(f"=== Plantilla de: {self._propietario} ===")
        for carta in self._plantilla:
            carta.imprimirCarta()
        print(f"Quimica del equipo: ")
        
    def quimicaTotal(self):
        quimica = 0
        for carta in self._plantilla:
            quimica += carta.calcularQuimica(self._paisfavorito, self._equipofavorito)