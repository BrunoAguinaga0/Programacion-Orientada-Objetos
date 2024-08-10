from cartelera import Cartelera
from serie import Series
from categoria import Categoria

serie1 = Series()
serie2 = Series()
serie3 = Series()
serie1.nombresg = "Doom Patrol"
serie1.diasg = "Lunes"
serie1.imagensg = "INSERTAR IMG XD"
serie2.nombresg = "Steven Universe"
serie2.diasg = "Jueves"
serie2.imagensg = "INSERTAR IMG XD"
serie3.nombresg = "Breaking Bad"
serie3.diasg = "Jueves"
serie3.imagensg = "INSERTAR IMG XD"
cate1 = Categoria("Episodios nuevos cada semana")
cartelera1 = Cartelera()
cartelera1.añadir(serie1)
cartelera1.añadir(serie2)
cartelera1.añadir(serie3)
cartelera1.imprimir(cate1.cate)
#Agregar clase categoria