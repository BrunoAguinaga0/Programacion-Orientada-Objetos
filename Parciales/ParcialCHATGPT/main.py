from Ave import Ave
from Reptil import Reptil
from Zoologico import Zoologico
from Mamifero import Mamifero

mamifero1 = Mamifero("Leon",5,"Carne","Mucho")
mamifero2 = Mamifero("Delfin",2,"Peces","Nada")
reptil1 = Reptil("Piton",3,"Ratas","Nada")
reptil2 = Reptil("Iguana",3,"Hojas","Nada")
ave1 = Ave("Gallina",2,"Maiz","Mucho")
ave2 = Ave("Aguila",1,"Peces","Mucho")

animales = [mamifero1, reptil1, reptil2, ave1, ave2]

zoologico1 = Zoologico("Zoologico Chubut")

for animal in animales:
    zoologico1.agregar_animal(animal)

zoologico1.hacer_invetario()
print("-------------------------------------------------")
zoologico1.alimentar_animales()