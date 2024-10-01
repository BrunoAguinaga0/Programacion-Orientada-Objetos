from Especial import Especial
from BronceEspecial import BronceEspecial
from Oro import Oro
from Plantilla import Plantilla
import random


habilidadesEspeciales = ["Ataque","Pase","Defensa"]
listaClubes = ["Arsenal","River Plate","Inter Miami","Manchester City"]
listaPaises = ["Argentina","Holanda","Inglaterra","Japon"]
jugadores = []
plantilla1 = []
plantilla2 = []

for i in range (0,22):
    numeroRandom = int(random.randint(1,3))
    if numeroRandom == 1:
        jugadores.append(BronceEspecial(f"Jugador {i+1}",listaClubes[random.randint(0,3)],listaPaises[random.randint(0,3)],habilidadesEspeciales[random.randint(0,2)]))
    elif numeroRandom == 2:
        jugadores.append(Oro(f"Jugador{i+1}",listaClubes[random.randint(0,3)],listaPaises[random.randint(0,3)]))
    else:
        random.shuffle(habilidadesEspeciales)
        jugadores.append(Especial(f"Jugador{i+1}",listaClubes[random.randint(0,3)],listaPaises[random.randint(0,3)],habilidadesEspeciales[0:2]))


random.shuffle(jugadores)
for i in range (0,22):
    if i < 11:
        plantilla1.append(jugadores[i])
    else:
        plantilla2.append(jugadores[i])


equipo1 = Plantilla("Bruno Aguinaga","Argentina","River Plate")
equipo1.agregarPlantilla(plantilla1)
equipo2 = Plantilla("Marco Mendez","Japon","Arsenal")
equipo2.agregarPlantilla(plantilla2)

print("====================================")
equipo1.imprimirPlantilla()
print("====================================")
equipo2.imprimirPlantilla()
print("====================================")