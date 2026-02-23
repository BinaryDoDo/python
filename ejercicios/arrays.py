# Creamos una lista vacía (como un ArrayList<String>)
frutas = ["manzana", "pera"]

# Pedimos un dato al usuario
nueva_fruta = input("Introduce una nueva fruta: ")

# Añadimos a la lista (equivalente al .add() de Java)
frutas.append(nueva_fruta)

# Imprimimos la lista completa y su longitud
print(f"Tu lista de compra tiene {len(frutas)} elementos: {frutas}")