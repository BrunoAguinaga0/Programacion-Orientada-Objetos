from abc import ABC, abstractmethod

class Multimedia(ABC):
    def __init__(self, nombre, anioEmision, calificacion):
        self._nombre = nombre
        self._anioEmision = anioEmision
        self._calificacion = calificacion
    
    def reproducir(self):
        print(f"Reproduciendo {self._nombre}")
    
    def imprimirMultimedia(self):
        print(f"Multimedia: {self._nombre} - Anio Emision: {self._anioEmision} - Calificacion: {self._calificacion}")
        
