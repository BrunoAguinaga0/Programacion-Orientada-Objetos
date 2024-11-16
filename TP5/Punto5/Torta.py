class Torta:
    def __init__(self):
        self.__masa = str
        self.__relleno = str

    def set_relleno(self, relleno):
        self.__relleno = relleno

    def set_masa(self, masa):
        self.__masa = masa

    def __str__(self) -> str:
        return f"Relleno: {self.__relleno} | Masa: {self.__masa}"
