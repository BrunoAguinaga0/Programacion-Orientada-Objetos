from Animal import Animal


class Reptil(Animal):
    def __init__(self, nombre, edad, alimento, tipoPiel):
        super().__init__(nombre, edad, alimento)
        self._tipoPiel = tipoPiel
        
    
    
    def mudar_piel(self, tipoPiel):
        print(f"{self._nombre} ha cambiado de piel.")
