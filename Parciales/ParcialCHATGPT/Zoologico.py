

class Zoologico:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__animales = []
    
    
    def agregar_animal(self, animal):
        self.__animales.append(animal)
    
    
    def alimentar_animales(self):
        print("====== Alimentando animales... ======")
        for animal in self.__animales:
            animal.alimentarse()
    
    
    def hacer_invetario(self):
        print(f"============ Inventario del Zoologico: {self.__nombre} ============")
        for animal in self.__animales:
            animal.imprimirAnimal()