from Director import Director
from BuilderTorta import BuilderTorta
from ConcreteBuilderTorta import ConcreteBuilderTortaVainilla


director = Director()
builder = ConcreteBuilderTortaVainilla()
director.builder = builder

print("Armado de torta: ")
director.build_torta()
builder.get_torta.lista_partes()