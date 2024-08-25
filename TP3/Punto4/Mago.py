from Personaje import Personaje


class mago:
    VIDA_POR_DEFECTO = 100
    def __init__(self,vida,nivelAtaque,nivelDefensa) -> None:
        super().__init__(vida,nivelAtaque,nivelDefensa)
        

    @classmethod
    def Constructor(cls, nivelAtaque, NivelDefensa):
        NuevoMago = (cls, cls.VIDA_POR_DEFECTO,nivelAtaque,NivelDefensa)
        return NuevoMago

    def defender(self,ataque):
        