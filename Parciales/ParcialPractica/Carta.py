from abc import ABC, abstractmethod

class Carta(ABC):

    def __init__(self, nombre, club, pais, habilidadesEspeciales):
        self._nombre = nombre
        self._club = club
        self._habilidadesEspeciales = habilidadesEspeciales
        self._pais = pais
        self._velocidad = self._generarAtributos()
        self._tiro = self._generarAtributos()
        self._regate = self._generarAtributos()
        self._defensa = self._generarAtributos()
        self._pase = self._generarAtributos()
        self._fisico = self._generarAtributos()
        
    @abstractmethod
    def _generarAtributos(self):
        pass
    
    def imprimirCarta(self):
        print(f"Nombre: {self._nombre} - Club: {self._club} - Pais: {self._pais}")
        print(f"Velocidad: {self._velocidad} - Tiro: {self._tiro}")
        print(f"Regate: {self._regate} - Defensa: {self._defensa}")
        print(f"Pase: {self._pase} - Fisico: {self._fisico}")
    
    def calcularQumica(self,paisFavorito,clubFavorito):
        if self._club == clubFavorito and self._pais == paisFavorito:
            return 100
        elif self._club == clubFavorito or self._pais == paisFavorito:
            return 80
        else:
            return 0
    
