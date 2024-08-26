from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self, nombre, vida, nivelAtaque, nivelDefensa):
        self._nombre = nombre
        self._vida = vida
        self._nivelAtaque = nivelAtaque
        self._nivelDefensa = nivelDefensa

    
    @abstractmethod
    def defender(self, ataque):
        pass
    
    
    def atacar(self) -> int:
        if self._vida > 0:
            print(f"{self._nombre} ataca con un daño de {self._nivelAtaque}")
            return self._nivelAtaque
        else:
            return 0


    def get_nivel_ataque(self):
        return self._nivelAtaque
    
    
    def get_nivel_defensa(self):
        return self._nivelDefensa

