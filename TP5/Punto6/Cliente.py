def mostrar_precios_juegos(creator, id, nombre, importe) -> None:
    juego = creator.factory_method(id, nombre, importe)
    print(f"el Juego: {juego.get_nombre()} tiene un importe de ${juego.get_precio()}")
