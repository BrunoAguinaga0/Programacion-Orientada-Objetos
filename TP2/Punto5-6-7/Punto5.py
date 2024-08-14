
from Persona import Persona

persona1 = Persona("Bruno","Aguinaga",'28/10/2001')
print(persona1)
print(f'Edad: {persona1.calculoEdad()}')
persona2 = Persona(None,None,'10/11/2002')
persona2.setNombre("Alan")
persona2.setApellido("Viera")
persona2.setFecha('24/07/2002')
print(persona2)
print(f'Edad: {persona2.calculoEdad()}')