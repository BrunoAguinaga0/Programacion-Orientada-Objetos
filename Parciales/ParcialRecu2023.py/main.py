from Usuario import Usuario
from Perfil import Perfil
from Multimedia import Multimedia
from Pelicula import Pelicula
from Serie import Serie
from Capitulos import Capitulos
import random

pelicula1 = Pelicula("El joker", 2018, 3)
pelicula2 = Pelicula("El caballero oscuro", 2008, 4)
serie1 = Serie("Okupas", 2001, 5)
for i in range (0,11):
    serie1.agregar_capitulo(Capitulos(f"Episodio {i+1}",i+1))

cuenta = Usuario("Bruno","Aguinaga","brunoaguinaga","bruno123")
perfil1 = Perfil("Bruno",False)
perfil1.agregar_multimedia(serie1)
perfil1.agregar_multimedia(pelicula1)
perfil1.agregar_multimedia(pelicula2)
cuenta.agregar_perfil(perfil1)

cuenta.imprimir_perfiles()
cuenta.__perfil
