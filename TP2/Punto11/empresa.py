from personas import Persona

class Empresa:
    def __init__(self,nombre,direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__empleado = []
    
    def agregoEmpleado(self,persona):
        self.__empleado.append(persona)
    
    def getNombre (self):
        return self.__nombre
    
    def setNombre (self,nombre):
        self.__nombre = nombre
    
    def getDireccion (self):
        return self.__direccion
    
    def setDireccion(self,direccion):
        self.__direccion = direccion
