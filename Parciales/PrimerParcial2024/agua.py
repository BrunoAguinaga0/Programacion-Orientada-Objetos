from pokemon import Pokemon
import random


class Agua(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre,"agua","hierba")
        #self._tipo = "agua"
        #self._debilidad = "hierba"

    def atacar(self, pokemonAtacado):
        if pokemonAtacado.debilidad() == self._tipo:
            return self._ataque * 1.7
        else:
            return self._ataque

    def defender(self,ataque):
        if ataque > self._defensa:
            numeroRandom = random.randint(1,10)
            if numeroRandom < 8:
                self._vida -= int(ataque - self._defensa)
                if self._vida <= 0:
                    print(f"{self._nombre} se defiende y recibe {int(ataque - self._defensa)} de daño, quedando con 0 de vida")
                else:
                    print(f"{self._nombre} se defiende y recibe {int(ataque - self._defensa)} de daño, quedando con {self._vida} de vida")
            else:
                if (ataque * 0.5) > self._defensa:
                    self._vida -= int((ataque * 0.5) - self._defensa)
                    if self._vida <= 0:
                        print(f"{self._nombre} se defiende y recibe {int(ataque - self._defensa)} de daño, quedando con 0 de vida")
                    else:
                        print(f"{self._nombre} se defiende y recibe {int(ataque - self._defensa)} de daño, quedando con {self._vida} de vida")
                else:
                    print(f"{self._nombre} se defiende y recibe 0 de daño, quedando con {self._vida} de vida")
        else:
            print(f"{self._nombre} se defiende y recibe 0 de daño, quedando con {self._vida} de vida")