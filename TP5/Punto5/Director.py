from BuilderTorta import BuilderTorta

class Director:
    def __init__(self):
        self._builder = None
    
    @property
    def builder(self) -> BuilderTorta:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderTorta):
        self._builder = builder

    def build_torta(self):
        self.builder.produce_masa()
        self.builder.produce_relleno()
        self.builder.produce_decoracion()