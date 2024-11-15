from Archivo import Archivo
from Carpeta import Carpeta

if __name__ == "__main__":
    # Archivos
    archivo1 = Archivo("archivo1.txt")
    archivo2 = Archivo("archivo2.txt")
    archivo3 = Archivo("archivo3.txt")
    archivo4 = Archivo("archivo4.txt")

    # Carpeta2
    carpeta2 = Carpeta("carpeta2")
    carpeta2.add(archivo1)
    carpeta2.add(archivo2)

    # Carpeta1
    carpeta1 = Carpeta("carpeta1")
    carpeta1.add(carpeta2)
    carpeta1.add(archivo3)

    # Carpeta3
    carpeta3 = Carpeta("carpeta3")
    carpeta3.add(archivo4)

    # Carpeta raiz
    carpetaRaiz = Carpeta("carpetaRaiz")
    carpetaRaiz.add(carpeta1)
    carpetaRaiz.add(carpeta3)

    # Operaciones
    print(carpetaRaiz.operacion())
