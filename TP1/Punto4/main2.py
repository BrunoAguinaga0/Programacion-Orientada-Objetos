#clase curso - Nombre - Instructores - Imagen - Valoracion - Precio - descuento
#clase cartelera - lista
from curso import Curso
from tienda import Tienda

tienda1 = Tienda()


curso1 = Curso("PyTorch for Deep Learning Bootcamp","Andrei Neagole - Daniel Bourke","www.google.com","4.6 estrellas - 2907 reseñas",74.99,12.99)
curso1.etiqueta = "Bestseller"
tienda1.agregarcursos(curso1)

curso2 = Curso("Machine Learning A-Z: AI python","Kirill Eremenko - Hadelin de Ponteves","www.google.com","4.5 estrellas - 184,477 reseñas",84.99,14.99)
curso2.etiqueta = "Bestseller"
tienda1.agregarcursos(curso2)

curso3 = Curso("Deep Learning: Advanced computer vision","Lazer Programmer Inc.","www.google.com","4.6 estrellas - 6,157 reseñas",79.99,14.99)
curso3.etiqueta = ""
tienda1.agregarcursos(curso3)

curso4 = Curso("Applied Generative AI and Natural Language Proccesing","Bert Golnick","www.google.com","4.7 estrellas - 88 reseñas",54.99,12.99)
curso4.etiqueta = "Hot & New"
tienda1.agregarcursos(curso4)

tienda1.imprimir()