from abc import ABC,abstractmethod

class Personaje(ABC):
    
    def __init__(self,vida,nivel_ataque,nivel_defensa):
        self._vida = vida
        self._nivel_ataque = nivel_ataque
        self._nivel_defensa = nivel_defensa
        
    def atacar(self) -> int:
        dano: int = 10
        return dano
    
    @abstractmethod
    def defender(self,ataque):
        pass