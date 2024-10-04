from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad, alimento):
        self._nombre = nombre
        self._edad = edad
        self._tipoAlimento = alimento
    
    
    def alimentarse(self):
        print(f"{self._nombre} esta comiendo {self._tipoAlimento}.")
    
    
    def dormir(self):
        print(f"{self._nombre} esta durmiendo.")
    
    
    def imprimirAnimal(self):
        print(f"Nombre: {self._nombre} - Edad: {self._edad} - Alimento: {self._tipoAlimento}")
