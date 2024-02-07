'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
suma = 0
for pares in range(0, 100, 2):
  suma += pares
print('la suma es:', suma)
