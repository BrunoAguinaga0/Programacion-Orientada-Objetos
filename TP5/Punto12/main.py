from Multimedia import Multimedia
from PerfilAdolecente import PerfilAdolecente
from PerfilAdulto import PerfilAdulto
from PerfilNiños import PerfilNiños

peliculas = []
# Peliculas para menores de 13 años
Pelicula1 = ("Toy Story", 3)
Pelicula2 = ("El rey leon", 3)
pelicula3 = ("Mi vecino Totoro", 12)
# Peliculas para menores de 18 años
pelicula4 = ("El senor de los anillos", 16)
pelicula5 = ("Harry Potter: El prisionero de Azkaban", 16)
# Peliculas para mayores de 18
pelicula6 = ("50 Sombras de Grey", 18)
# Agregar Peliculas a la lista
peliculas.append(Pelicula1)
peliculas.append(Pelicula2)
peliculas.append(pelicula3)
peliculas.append(pelicula4)
peliculas.append(pelicula5)
peliculas.append(pelicula6)

# Multimedia
multimedia = Multimedia(peliculas, PerfilNiños("Roma", 5))
# Mostrar Peliculas para niños
print("--------- Peliculas para menores de 13 ---------")
multimedia.consultar_catalogo()
# Cambiar estrategia
multimedia.set_estrategia(PerfilAdolecente("Jeremias", 15))
# Mostrar Peliculas para adolecentes
print("--------- Peliculas para menores de 18 ---------")
multimedia.consultar_catalogo()
# Cambiar estrategia
multimedia.set_estrategia(PerfilAdulto("Ricardo", 25))
# Mostrar Peliculas para adultos
print("--------- Peliculas para mayores de 18 ---------")
multimedia.consultar_catalogo()
