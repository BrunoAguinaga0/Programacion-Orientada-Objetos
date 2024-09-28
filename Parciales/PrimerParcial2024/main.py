from fuego import Fuego
from hierba import Hierba
from agua import Agua
from entrenador import Entrenador
import random

pokemonPrincipal = Fuego("Charmander")
entrenador1 = Entrenador("Ash",pokemonPrincipal)
pokemonLista = []

for i in range (0,10):
    numeroRandom = int(random.randint(1,3))
    if numeroRandom == 1:
        pokemonLista.append(Agua(f"Pokemon Agua {i+1}"))
    if numeroRandom == 2:
        pokemonLista.append(Fuego(f"Pokemon Fuego {i+1}"))
    if numeroRandom == 3:
        pokemonLista.append(Hierba(f"Pokemon Hierba {i+1}"))
random.shuffle(pokemonLista)

for i in range (0,10):
    atrapado = False
    k = 1
    print("=======================================")
    print(f"  --- Batalla vs {pokemonLista[i].getNombre()} ---")
    while not atrapado and k <= 3:
        k += 1
        if pokemonLista[i].getVida() > 0:
            atrapado = entrenador1.atraparPokemon(pokemonLista[i])
        else:
            k = 4
    if atrapado == True:
        print(f"El pokemon: {pokemonLista[i].getNombre()} a sido añadido a la pokedex")
    else:
        if pokemonLista[i].getVida() > 0:
            print("El pokemon a escapado")
        else:
            print("El pokemon a muerto")
print("=======================================")
print(" ")
print("====== Entrenador ======")
entrenador1.imprimir()