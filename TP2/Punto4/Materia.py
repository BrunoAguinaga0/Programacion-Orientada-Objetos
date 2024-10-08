

class Materia:
    def __init__(self,nombre,codigo):
        self.__nombre = codigo
        self.__codigo = nombre

    @classmethod
    def inicio_con_materia(cls, nombre):
        materia = cls.__new__(cls)
        materia.__nombre = nombre
        materia.__codigo = None
        return materia
    
    @property
    def nombremateria(self):
        return self.__nombre
    
    @nombremateria.setter
    def nombremateria(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo