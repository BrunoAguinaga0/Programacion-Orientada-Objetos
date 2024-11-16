from Director import Director
from BuilderTorta import BuilderTorta
from ConcreteBuilders import (
    ConcreteBuilderTortaVainilla,
    ConcreteBuilderTortaCoco,
    ConcreteBuilderTortaChocolate,
)


director = Director()
builder = ConcreteBuilderTortaVainilla()
director.builder = builder

print("Armado de torta: ")
director.build_torta()
Torta1 = builder.get_torta()
print(Torta1)

print("----------------------------------------")

builder2 = ConcreteBuilderTortaCoco()
director.builder = builder2

print("Armado de torta: ")
director.build_torta()
Torta2 = builder2.get_torta()
print(Torta2)

print("----------------------------------------")

builder3 = ConcreteBuilderTortaChocolate()
director.builder = builder3

print("Armado de torta: ")
director.build_torta()
Torta3 = builder3.get_torta()
print(Torta3)
