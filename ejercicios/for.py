nombres = ["Ana", "Berto", "Carlos"]

# 1. Iterar directamente sobre los elementos (como el for-each)
print("Lista de nombres:")
for nombre in nombres:
    print(f"- {nombre}")

# 2. Iterar un número específico de veces (usando range)
# range(5) genera números del 0 al 4
print("\nContando hasta 5:")
for i in range(5):
    print(f"Número: {i}")