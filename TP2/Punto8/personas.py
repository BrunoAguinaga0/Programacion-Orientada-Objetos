

class Persona:
    def __init__(self,nombre,apellido,edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__trabajo = None
        self.__estudio = None
        
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEdad(self):
        return self.__edad
    
    def getTrabajo(self):
        return self.__trabajo
    
    def setTrabajo(self,trabajo):
        self.__trabajo = trabajo
        
    def getEstudio(self):
        return self.__estudio
    
    def setEstudio(self,estudio):
        self.__estudio = estudio
    
    def __str__(self):
        return f'Nombre: {self.__apellido}, {self.__nombre} - Edad: {self.__edad} - Estudia: {self.__estudio} - Trabajo: {self.__trabajo}'