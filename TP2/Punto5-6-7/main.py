
from Persona import Persona

persona1 = Persona("Bruno","Aguinaga",'28/10/2001')
print(persona1)
print(f'Edad: {persona1.calculoEdad()} Años')
print("\n")
persona2 = Persona(None,None,'10/11/2002')
persona2.setNombre("Alan")
persona2.setApellido("Viera")
persona2.setFecha('24/07/2002')
print(persona2)
print(f'Edad: {persona2.calculoEdad()} Años')
print("\n")
persona3 = Persona("Daniel","Acevedo",'10/03/2002')
print(persona3)
print(f'Edad: {persona3.calculoEdad()} Años')