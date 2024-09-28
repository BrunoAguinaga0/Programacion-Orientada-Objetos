from pokemon import Pokemon
import random


class Hierba(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre,"hierba","fuego")


    def defender(self,ataque=int(0)):
        if ataque > self._defensa:
            if self._velocidad > 50:
                numeroRandom = random.randint(1,2)
                match numeroRandom:
                    case 1:
                        print(f"{self._nombre} evadio el ataque, quedando con {self._vida} de vida")
                    case 2: 
                        self._vida -= (int(ataque) - int(self._defensa))
                        if self._vida <= 0:
                            print(f"{self._nombre} se defiende y recibe {int(ataque)} de daño, quedando con 0 de vida")
                        else:
                            print(f"{self._nombre} se defiende y recibe {(int(ataque) - int(self._defensa))} de daño, quedando con {self._vida} de vida")
            else:
                self._vida -= (int(ataque) - int(self._defensa))
                if self._vida <= 0:
                    print(f"{self._nombre} se defiende y recibe {(int(ataque) - int(self._defensa))} de daño, quedando con 0 de vida")
                else:
                    print(f"{self._nombre} se defiende y recibe {(int(ataque) - int(self._defensa))} de daño, quedando con {self._vida} de vida")
        else:
            print(f"{self._nombre} se defiende y recibe 0 de daño, quedando con {self._vida} de vida")
