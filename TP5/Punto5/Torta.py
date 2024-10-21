

class Torta:
    def __init__(self):
        self.partesTorta = []
        self.__masa = str
        self.__relleno = str
    
    def add(self,parte):
        self.partesTorta.append(parte)
    
    def lista_partes(self):
        print(f"Partes de la torta: {', '.join(self.partesTorta)}", end="")
    
    def set_relleno(self,relleno):
        self.__relleno = relleno
    
    def set_masa(self,masa):
        self.__masa = masa