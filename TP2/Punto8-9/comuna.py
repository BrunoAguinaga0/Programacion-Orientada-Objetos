

class Comuna:
    def __init__(self):
        self.__comuna = []
    
    def cantidadfamilias(self):
        cantiFamilias = len(self.__comuna)
        return int(cantiFamilias)
    
    def agregarComuna(self,familia):
        self.__comuna.append(familia)
    
    def imprimirComuna(self):
        print("-- COMUNA --")
        i = 1
        for comuna in self.__comuna:
            print("Familia",i,": ")
            comuna.imprimirFamilia()
            i = i+1
    
    def cantidadPersonasFamilia(self): #esta funcion utiliza funciones de la clase familia para devolver la cantidad de personas
        cantiPersonasTotal = 0         #tambien devuelve el promedio de edad de las personas senadas, y cuantas personas trabajan
        edad = 0
        cantiEdades = 0
        personasTrabajando = 0
        for comuna in self.__comuna: #bucle que recorre las familias ya censadas
            cantiPersonasTotal = cantiPersonasTotal + comuna.cantidadPersonasFamilia()
            edad = edad + comuna.trabajoYedad()[0]
            cantiEdades = cantiEdades + comuna.trabajoYedad()[1]
            personasTrabajando = personasTrabajando + comuna.trabajoYedad()[2]
            #edad,cantiEdades,personasTrabajando = edad + comuna.trabajoYedad()
        promedioEdad = edad/cantiEdades
        return cantiPersonasTotal,promedioEdad,personasTrabajando