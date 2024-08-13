

from Materia import Materia
from Profesor import Profesor


poo = Materia.inicio_con_materia_y_codigo("POO","IF153")
algebra = Materia.inicio_con_materia_y_codigo("Algebra",183)
introduccion = Materia.nombre.setter("Introduccion a la computacion")
introduccion = Materia.codigo.setter("IF300")
algoritimica = Materia.inicio_con_materia_y_codigo("Algoritmica","500")

profesores = []
profesor1 = Profesor("Pedro","Hernandez")
profesor1.agregar_materia(algebra)
profesores.append(profesor1)
profesor2 = Profesor("Romina","Alvarez")
profesor2.agregar_materia(introduccion)
profesor2.agregar_materia(algoritimica)
profesores.append(profesor2)

for pro in profesores:
    print(f'{"Profesor: "}{pro.nombre()}{","}{pro.apellido}')
    print ("Materias:")
    for mat in pro.materia():
        print(mat.nombre())