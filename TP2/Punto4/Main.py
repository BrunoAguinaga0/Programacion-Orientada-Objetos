

from Materia import Materia
from Profesor import Profesor


poo = Materia("POO","IF153")
algebra = Materia("Algebra","183")
introduccion = Materia.inicio_con_materia("Introduccion a la computacion")
introduccion.codigo = "IF300"
algoritimica = Materia("Algoritmica","500")

profesores = []

profesor1 = Profesor("Pedro","Hernandez")
profesor1.agregar_materia(poo)
profesor1.agregar_materia(algebra)
profesores.append(profesor1)
profesor2 = Profesor("Romina","Alvarez")
profesor2.agregar_materia(introduccion)
profesor2.agregar_materia(algoritimica)
profesores.append(profesor2)

for pro in profesores:
    print(f'{"Profesor: "}{pro.nombre}{", "}{pro.apellido}')
    print ("Materias:")
    for mat in pro.materia():
        print(mat.nombre())
        