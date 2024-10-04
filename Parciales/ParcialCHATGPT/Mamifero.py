from Animal import Animal


class Mamifero(Animal):
    def __init__(self, nombre, edad, alimento, cantidadPelo):
        super().__init__(nombre, edad, alimento)
        self._cantidadPelo = cantidadPelo
    
    def amamantar(self):
        print(f"{self._nombre} esta amamantando.")
