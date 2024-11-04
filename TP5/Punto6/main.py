from ConcretJuegoDigital import ConcretJuegoDigital
from ConcretJuegoFisico import ConcretJuegoFisico
from Cliente import mostrar_precios_juegos

if __name__ == "__main__":
    print("Juego digital: ")
    mostrar_precios_juegos(ConcretJuegoDigital(), 1, "Minecraft", 100)
    print("Juego fisico: ")
    mostrar_precios_juegos(ConcretJuegoFisico(), 1, "Roblox", 120)
