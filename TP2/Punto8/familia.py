

class Familia:
    def __init__(self):
        self.__familia = []
    
    def agregarFamilia(self,familia):
        self.__familia.append(familia)
        
    def imprimirFamilia(self):
        for family in self.__familia:
            print(family)