###
# 03 - cast()
# Transformar un tipo de dato en otro
###

print("Conversión de tipos:")
print(type(int("100"))) # Convierte una cadena a un entero

# Ejemplo de fallos por diferentes tipos
# print("100" + 2) # Esto da error porque no se pueden sumar una cadena y un entero

# Para evitar el error, podemos convertir el entero a cadena o la cadena a entero
print("100" + str(2)) # Convertimos el entero a cadena
print(int("100") + 2) # Convertimos la cadena a entero

# Ejemplo de boleanos

print(bool(0)) # Cero es falso
print(bool(1)) # Cualquier número distinto de cero es verdadero
print(bool("")) # Cadena vacía es falsa
print(bool("Hola")) # Cualquier cadena no vacía es verdadera
print(bool([])) # Lista vacía es falsa
print(bool([1, 2, 3])) # Cualquier lista no vacía es verdadera
