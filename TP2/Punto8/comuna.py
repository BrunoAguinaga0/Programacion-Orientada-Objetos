

class Comuna:
    def __init__(self):
        self.__comuna = []
    
    def agregarComuna(self,familia):
        self.__comuna.append(familia)
    
    def imprimirComuna(self):
        print("-- COMUNA --")
        i = 1
        for comuna in self.__comuna:
            print("Familia",i,": ")
            comuna.imprimirFamilia()
            i = i+1