'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''
a = 4
b = 6
def suma (a, b):
  return a + b
resultado_suma = suma(a, b)

def resta (a, b):
  return a - b
resultado_resta = resta(a, b)

def multiplicacion (a, b):
  return a * b
resultado_multiplicacion = multiplicacion(a, b)

def division (a, b):
  return a / b
resultado_division = division (a, b)

print('suma=',resultado_suma)
print('resta=',resultado_resta)
print('multiplicación=',resultado_multiplicacion)
print('división=',resultado_division)

