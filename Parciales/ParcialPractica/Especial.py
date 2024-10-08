from Carta import Carta
import random

class Especial(Carta):
    def __init__(self, nombre, club, pais,habilidadesEspeciales):
        super().__init__(nombre, club, pais, habilidadesEspeciales)
    
    def _generarAtributos(self):
        atributo = int(random.randint(89,99) * 1.02)
        if atributo <= 99:
            return atributo
        else:
            return 99
    
    
    def imprimirCarta(self,pais,club):
        super().imprimirCarta(pais,club)
        print("Habilidades Especiales: " + "-".join(self._habilidadesEspeciales))
    
    
    def calcularQumica(self, paisFavorito, clubFavorito):
        return 100