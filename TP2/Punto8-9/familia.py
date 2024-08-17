

class Familia:
    def __init__(self):
        self.__familia = []
        
    def cantidadPersonasFamilia(self): #funcion que devuelve la cantidad de personas que hay en una familia
        cantiPersonas = len(self.__familia)
        return cantiPersonas
    
    def trabajoYedad (self): #esta funcion recorre las familias ingresadas, acumula las edades y cuenta cuantas personas hay
        edad = 0             #tambien cuenta cuantas personas trabajan
        cantiEdades = 0
        personasTrabajando = 0
        for familia in self.__familia:
            cantiEdades = cantiEdades + 1
            edad = edad + familia.getEdad()
            if familia.getTrabajo() == "Si":
                personasTrabajando = personasTrabajando + 1
        return edad,cantiEdades,personasTrabajando
    
    def agregarFamilia(self,familia):
        self.__familia.append(familia)
        
    def imprimirFamilia(self):
        for family in self.__familia:
            print(family)