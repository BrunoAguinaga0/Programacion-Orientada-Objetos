

class Capitulos:
    def __init__(self,nombreCapitulo,nroCapitulo) -> None:
        self.__nombreCapitulo = nombreCapitulo
        self.__nroCapitulo = nroCapitulo
        self.__reproducido = False
    
    def getReproducido(self):
        return self.__reproducido
    
    def getNro(self):
        return self.__nroCapitulo
    
    def setReproducido(self):
        self.__reproducido = True
