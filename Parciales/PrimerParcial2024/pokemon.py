from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    def __init__(self, nombre, tipo, debilidad):
        self._nombre = nombre
        self._tipo = tipo
        self._vida = int(100)
        self._ataque = self._valorAleatorio()
        self._defensa = self._valorAleatorio()
        self._velocidad = self._valorAleatorio()
        self._debilidad = debilidad
        self._salvajismo = self._valorAleatorio()


    def _valorAleatorio(self):
        return int(random.randint(0, 100))

    @abstractmethod
    def defender(self, ataque):
        pass

    def atacar(self,pokemonAtacado):
        if pokemonAtacado.getDebilidad() == self._tipo:
            numeroRandom = random.randint(0,100)
            if numeroRandom < 70:
                return self._ataque * 1.5
            else:
                return self._ataque
        else:
            return self._ataque

    def imprimir(self):
        print(f"Nombre: {self._nombre} Tipo: {self._tipo}")
        print(f"Ataque: {self._ataque} Defensa: {self._defensa}")
        print(f"Velocidad: {self._velocidad} Salvajismo: {self._salvajismo}")
        
    def getNombre(self):
        return self._nombre
    
    def getTipo(self):
        return self._tipo
    
    def getDebilidad(self):
        return self._debilidad
    
    def getSalvajismo(self):
        return int(self._salvajismo)
    
    def setSalvajismo(self, valor):
        self._salvajismo = valor
    
    def getVida(self):
        return int(self._vida)
    