from Personaje import Personaje


VIDA_CABALLERO: int = 120

class Caballero(Personaje):
    def __init__(self, nombre, nivelAtaque, nivelDefensa):
        super().__init__(nombre,VIDA_CABALLERO, nivelAtaque, nivelDefensa)
        
    def defender(self, ataque):
        self.__vida = self.__vida - ataque + self.__nivelDefensa
        print("El personaje {} tiene {} de vida".format(self._nombre, self.__vida))
        if self.__vida < 1:
            print("El personaje {} ha muerto".format(self._nombre))
        
    def atacar(self):
        bonusdano = 25
        atacar2 = super().atacar() + bonusdano
        return atacar2

# defender(pj1.getNivelAtaque())
# defender(ataque)