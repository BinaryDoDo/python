###
# 04 - Variables
# Las variables sirven para almacenar datos en memoria
# Python es un lenguaje tipado dinaámico y de tipado fuerte
###

# asignar variables
# Solo hace falta poner esto:

my_name = "David"

print(my_name) # Imprime el valor de la variable

age = 32
print(age)

age = 39
print(age) # El valor de la variable ha cambiado

# Tipado dinámico: el tipo de dato se determina en tiempode ejecución, no es necesario declararlo antes

name = "David"
print(type(name)) # Es una cadena de texto

name = 123
print(type(name)) # Ahora es un entero

# tipado fuerte: no se pueden mezclar tipos de datos sin convertirlos explícitamente

# Para poner una cadena de texto más número se usa f en print

print(f"Hola mi nombnre es: {my_name} y tengo {age} años")

# Convecciones de nombre de variables:
mi_nombre_de_variable = "ok" # snake_case

# Constantes: python no tiene constantes como tal, pero se suele usar mayúsculas para indicar que una variable no debe cambiar