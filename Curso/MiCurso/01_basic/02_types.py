###
# 02 - types()
# Python tiene varios tipos de datos
# int, float, complex, str, bool, noneType, list, tuple, dict, range, set...
###

print("int:")
print(type(10))
print(type(0))
print(type(-5))
print(type(521635656465465456456))

print("Float:")
print(type(3.14))
print(type(1.0))
print(type(1e-9)) # Notación científica

print("Complex:")
print(type(1 + 2j))

print("Str:")
print(type("Hola"))
print(type("123"))
print(type("""
    Multilínea
"""))

print("Bool:")
print(type(True))
print(type(False))
print(type(10 > 5)) # Las comparaciones también son booleanas

print("NoneType:")
print(type(None)) # El tipo NoneType representa la ausencia de valor
