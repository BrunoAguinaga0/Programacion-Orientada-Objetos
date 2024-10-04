from Animal import Animal


class Ave(Animal):
    def __init__(self, nombre, edad, alimento, envergaduraAlas):
        super().__init__(nombre, edad, alimento)
        self._envergaduraAlas = envergaduraAlas
    
    
    def volar(self):
        print(f"{self._nombre} esta volando.")