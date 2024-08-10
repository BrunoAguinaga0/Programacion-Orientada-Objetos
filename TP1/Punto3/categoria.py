

class Categoria:
    def __init__(self,cate):
        self.__dia = cate
        
    @property
    def cate(self):
        return self.__dia