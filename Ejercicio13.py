'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''
dato = 67
if dato < 2:
    print('no es un numero primo')
for i in range(2, dato):
  if (dato % i) == 0:
    print('no es un numero primo')
    break
else:
  print('es un numero primo')
  