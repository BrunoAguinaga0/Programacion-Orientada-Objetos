

class Series:
    def __init__(self):
        self.__nombre = None
        self.__dia = None
        self.__imagen = None


    @property
    def nombresg(self):
        return self.__nombre


    @property
    def diasg(self):
        return self.__dia


    @property
    def imagensg(self):
        return self.__imagen


    @nombresg.setter
    def nombresg(self,nombre):
        self.__nombre = nombre


    @diasg.setter
    def diasg(self,dia):
        self.__dia = dia


    @imagensg.setter
    def imagensg(self,imagen):
        self.__imagen = imagen