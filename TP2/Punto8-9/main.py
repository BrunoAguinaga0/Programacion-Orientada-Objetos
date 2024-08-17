from comuna import Comuna
from familia import Familia
from personas import Persona

persona1 = Persona("Bruno","Aguinaga",22)
persona1.setEstudio("Si")
persona1.setTrabajo("No")
print("Ingreso 4 personas a la base de datos, a continuacion les haremos las siguientes preguntas:")
print("Persona 1:")
manejo = input("tiene permitido trabajar? Si/No: ")
trabajo = input("Tiene permitido manejar vehiculos particulares? Si/No: ")
persona1.setpermisomanejar(manejo)
persona1.setpermisotrabajo(trabajo)

print("\nPersona 2:")
persona2 = Persona("Alan","Viera",22)
persona2.setEstudio("Si")
persona2.setTrabajo("Si")
manejo = input("tiene permitido trabajar? Si/No: ")
trabajo = input("Tiene permitido manejar vehiculos particulares? Si/No: ")
persona2.setpermisomanejar(manejo)
persona2.setpermisotrabajo(trabajo)

familia1 = Familia()
familia1.agregarFamilia(persona1)
familia1.agregarFamilia(persona2)

persona3 = Persona("Daniel","Acevedo",30)
persona3.setEstudio("Si")
persona3.setTrabajo("No")
print("\nPersona 3:")
manejo = input("tiene permitido trabajar? Si/No: ")
trabajo = input("Tiene permitido manejar vehiculos particulares? Si/No: ")
persona3.setpermisomanejar(manejo)
persona3.setpermisotrabajo(trabajo)

persona4 = Persona("Samuel","Valenciano",20)
persona4.setEstudio("Si")
persona4.setTrabajo("No")
print("\nPersona 4:")
manejo = input("tiene permitido trabajar? Si/No: ")
trabajo = input("Tien---e permitido manejar vehiculos particulares? Si/No: ")
persona4.setpermisomanejar(manejo)
persona4.setpermisotrabajo(trabajo)

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
