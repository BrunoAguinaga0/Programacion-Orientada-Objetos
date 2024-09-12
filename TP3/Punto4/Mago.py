from Personaje import Personaje


vida_mago: int = 100

class Mago(Personaje):


    def __init__(self, nombre, nivelAtaque, nivelDefensa):
        super().__init__(nombre,vida_mago, nivelAtaque, nivelDefensa)


    def defender(self, ataque):
        self._vida = self._vida + self._nivelDefensa - ataque
        print(f"El personaje {self._nombre} tiene {self._vida} de vida")
        if self._vida < 1:
            print("El personaje {} ha muerto".format(self._nombre))
        
    def atacar(self): #Agrege una extencion del metodo atacar de la clase padre
        atacar2 = super.atacar() + 35 #suma + 25 de daño al daño original
        return atacar2

        