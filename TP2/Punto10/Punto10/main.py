from comuna import Comuna
from familia import Familia
from personas import Persona

edad1 = int(input("Ingrese la edad de la persona:"))
persona1 = Persona("Bruno","Aguinaga",22)
persona1.setEstudio("Si")

persona1.setTrabajo("No")

persona2 = Persona("Alan","Viera",22)
persona2.setEstudio("Si")
persona2.setTrabajo("Si")

familia1 = Familia()
familia1.agregarFamilia(persona1)
familia1.agregarFamilia(persona2)

persona3 = Persona("Daniel","Acevedo",30)
persona3.setEstudio("Si")
persona3.setTrabajo("No")

persona4 = Persona("Samuel","Valenciano",20)
persona4.setEstudio("Si")
persona4.setTrabajo("No")

familia2 = Familia()
familia2.agregarFamilia(persona3)
familia2.agregarFamilia(persona4)

comuna1 = Comuna()
comuna1.agregarComuna(familia1)
comuna1.agregarComuna(familia2)
comuna1.imprimirComuna()

cantidadPersonasTotal,promedioEdad,personasTrabajando = comuna1.cantidadPersonasFamilia()
print("Cantidad de familias censadas:",comuna1.cantidadfamilias(), "Cantidad de personas censadas",cantidadPersonasTotal)
print("Promedio de edad:",promedioEdad,"Personas trabajando:",personasTrabajando)
