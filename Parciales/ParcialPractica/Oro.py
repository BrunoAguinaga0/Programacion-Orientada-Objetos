from Carta import Carta
import random

class Oro(Carta):
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais," ")
        
    def _generarAtributos(self):
        return int(random.randint(74,90) * 1.05)