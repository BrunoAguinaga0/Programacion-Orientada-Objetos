

class Profesor:
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__materia = []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def materia(self):
        return self.__materia
    
    @materia.setter
    def materia(self, materia):
        self.__materia = materia

    def agregar_materia(self, materia):
        self.__materia.append(materia)
    