from pokemon import Pokemon
import random

class Fuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre,"fuego","agua")	
        #self._tipo = "fuego"
        #self._debilidad = "agua"
        

    def defender(self,ataque):
        if ataque > self._defensa:
            self._vida -= int(ataque - self._defensa)
            if self._vida <= 0:
                print(f"{self._nombre} se defiende y recibe {int(ataque - self._defensa)} de daño, quedando con 0 de vida")
            else:
                print(f"{self._nombre} se defiende y recibe {int(ataque - self._defensa)} de daño, quedando con {self._vida} de vida")
        else:
            print(f"{self._nombre} se defiende y recibe 0 de daño, quedando con {self._vida} de vida")