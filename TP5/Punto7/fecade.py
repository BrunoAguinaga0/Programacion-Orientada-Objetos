class fachada:
    def __init__(self, helper1, helper2):
        self.__helper1 = helper1
        self.__helper2 = helper2

    def operation(self, palabra):
        respuestas = []
        respuestas.append(self.__helper1.traductor(palabra))
        respuestas.append(self.__helper2.minusculas(palabra))
        respuestas.append(self.__helper2.mayusculas(palabra))
        return respuestas
