# Debes escribir un programa en Python que haga lo siguiente:

#     Cree una lista vacía llamada notas.

#     Use un bucle for que se repita 3 veces.

#     Dentro del bucle, debe pedir al usuario una nota (número) usando input().

#     Ojo aquí: Como input() devuelve texto, debes convertirlo a número decimal (en Python se usa float()) antes de guardarlo.

#     Añade cada nota a la lista usando .append().

#     Al finalizar el bucle, imprime la lista completa.

#     Extra (Opcional): Intenta imprimir cuánto suman todas las notas usando la función sum(notas).

#       ------------------------------------------------------------------------------


# notas = []

# for i in range(3):
#     dato_valido = False
#     while not dato_valido:
#         nota = float(input(f"Introduce la nota de la asignatura nº {i+1}: "))
#         if 0 <= nota <= 10:
#             notas.append(nota)
#             dato_valido = True
#         else:
#             print("Error: Nota fuera de rango.")
    
# print("Las notas guardadas son:", notas)

# print("La suma de las notas es:", sum(notas))

# media = sum(notas) / len(notas)

# print("La media es:", media)

# ------------------------------------------------------------------------------

# En el bucle, pide el nombre.

# Pide la nota (con tu validación).

# Crea un "objeto" rápido así: alumno = {"nombre": nombre, "nota": nota}.

# Haz el append de ese diccionario a tu lista.

notas = []

for i in range(3):
    nombre = input(f"Introduce nombre del alumno {i+1}: ")
    
    dato_valido = False
    while not dato_valido:
        # Pedimos el dato directamente aquí
        dato = float(input(f"Introduce la nota de {nombre}: "))
        
        if 0 <= dato <= 10:
            nota = dato
            dato_valido = True
        else:
            print("Error: Nota fuera de rango.")
            
    # Creamos el diccionario (el "HashMap")
    alumno = {"nombre": nombre, "nota": nota}
    notas.append(alumno)

print("\n--- Resultados ---")
# Para sumar, extraemos las notas de cada diccionario
suma_total = sum(a["nota"] for a in notas)
media = suma_total / len(notas)

print(f"La media de la clase es: {media:.2f}")

# Ejemplo de cómo acceder a las claves de un alumno específico
print(f"Las claves del diccionario son: {alumno.keys()}")


# Ejercicio extra con mapas:

print("\n--- LISTADO DE CLASE ---")
for estudiante in notas:
    # 'estudiante' es el diccionario completo (el "objeto")
    # Ahora accede a sus "atributos" usando los corchetes
    print(f"Alumno: {estudiante['nombre']} | Calificación: {estudiante['nota']}")