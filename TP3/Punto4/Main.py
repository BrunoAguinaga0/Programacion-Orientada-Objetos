from Caballero import Caballero
from Mago import Mago 

caballero1 = Caballero("Caballero1",40,50)
caballero2 = Caballero("Caballero2",40,50)
caballero3 = Caballero("Caballero3",40,50)

mago1 = Mago("Mago1",50,30)
mago2 = Mago("Mago2",50,30)
mago3 = Mago("Mago3",50,30)

#caballero1.atacar()
mago1.defender(caballero1.atacar())