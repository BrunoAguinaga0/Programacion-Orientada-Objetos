from Cartero import Cartero
from Furgoneta import Furgoneta
from Paquete import Paquete
from GestorEnvios import GestorEnvios

paquete1 = Paquete(12345,"Notebook",5,30.0,24.0,2.0)
paquete2 = Paquete(54321,"Lavarropas",25.0,70.0,110.0,60.0)

transportes = [Cartero("Cartero",5,270),Furgoneta("Furgoneta",60,1000)]

gestor = GestorEnvios()

print("============= Paquete 1 =============")
gestor.gestionarEnvios(transportes,paquete1)
print("============= Paquete 2 =============")
gestor.gestionarEnvios(transportes,paquete2)



#Para la abstraccion de transporte, hice una clase abstracta que hereda de una interfaz, si bien cartero no es un medio de transporte
#las 2 clases se encargaban de hacer lo mismo asi que utilize una clase abstracta padre para reutilziar codigo
#la interfaz fue implementada pensando en que las dos clases hijas pueden transportar paquetes

#para paquete definiria una clase padre que "Paquete", que herede a 2 subclases electrodomesticos y Articulos de limpieza
#en el cual definiria un metodo empaquetar, que se encargaria de empaquetar el paquete.
#dependiendo la subclase el empaquetado deberia ser diferente, por ejemplo si es un electrodomestico el empaquetado
#que en la caja del empaquetado se mencione que es muy fragil
#si fuera un articulo de limpieza que se mencione que dentro podria traer articulos con quimicos 

#De esta forma podemos reutilizar el mismo codigo(al menos del constructor) en las subclases, al realizarse el metodo empaquetado
#podria ser abstracto y que se defina en cada una de las subclases realizando polimorfismo