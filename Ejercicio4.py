'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''

palabra = 'barbacoa'
vocales = 'aeiou'
cantidad = 0
for letra in palabra:
  if letra in vocales:
    cantidad +=1
print(cantidad)
