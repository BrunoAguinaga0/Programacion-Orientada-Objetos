from pokemon import Pokemon
from fuego import Fuego
from hierba import Hierba
from agua import Agua
import random

class Entrenador():
    def __init__(self, nombre,pokemonPrincipal):
        self.__nombre = nombre
        self.__nivelEntrenador = self.__numeroRandom()
        self.__pokedex = []
        self.__pokemonPrincipal = pokemonPrincipal


    def __numeroRandom(self):
        return random.randint(1, 100)

    def nombre(self):
        return self._nombre

    def nivelEntrenador(self):
        return self._nivelEntrenador
    
    def __agregarPokemon(self, pokemon):
        self.__pokedex.append(pokemon)
    
    
    def atraparPokemon(self, pokemon):
            if self.__nivelEntrenador > pokemon.getSalvajismo():
                self.__agregarPokemon(pokemon)
                return True
            else:
                pokemon.defender(self.__pokemonPrincipal.atacar(pokemon))
                pokemon.setSalvajismo(int(pokemon.getSalvajismo()*0.9))
                return False
    
    def imprimir(self):
        print(f"Nombre: {self.__nombre} - Nivel: {self.__nivelEntrenador}")
        print(f"Pokemon Principal: {self.__pokemonPrincipal.getNombre()} - Tipo: {self.__pokemonPrincipal.getTipo()}")
        print(f"====== Pokedex ======")
        for i in range (len(self.__pokedex)):
            print(f"Nombre: {self.__pokedex[i].getNombre()} - Tipo: {self.__pokedex[i].getTipo()}")