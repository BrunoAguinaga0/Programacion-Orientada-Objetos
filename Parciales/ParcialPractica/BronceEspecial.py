from Carta import Carta
import random

class BronceEspecial(Carta):
    def __init__(self,nombre,club,pais,habilidadEspecial):
        super().__init__(nombre,club,pais,habilidadEspecial)

    def _generarAtributos(self):
        return int(random.randint(49,65) + 2)
    
    def imprimirCarta(self,pais,club):
        super().imprimirCarta(pais,club)
        print(f'Habilidad Especial: {self._habilidadesEspeciales}')
