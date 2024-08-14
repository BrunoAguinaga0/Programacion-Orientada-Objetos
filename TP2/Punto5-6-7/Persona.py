from datetime import datetime


class Persona:
    def __init__(self, nombre: str, apellido: str, fechaNacimiento: datetime.strptime):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = datetime.strptime(fechaNacimiento, '%d/%m/%Y')
        

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido
    
    def setApellido(self,apellido):
        self.__apellido = apellido
        
    def getfecha(self):
        return self.__fechaNacimiento
    
    def setFecha(self,fecha):
        self.__fechaNacimiento = datetime.strptime(fecha, '%d/%m/%Y')
        
    def __str__(self):
        return f'Nombre: {self.__apellido}, {self.__nombre} - Fecha de Nacimiento: {self.__fechaNacimiento.strftime('%d-%m-%Y')}'
    
    def calculoEdad(self):
        edad = datetime.now()
        edadfinal = int(edad.year) - int(self.__fechaNacimiento.year)
        return edadfinal
