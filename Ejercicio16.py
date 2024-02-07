'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''

lista = [1, 6, 8, 9, 14, 17, 24]
pares=0
impares=0
num_pares = []
num_impares =[]
for n in lista:
  if n % 2 == 0:
    pares +=1
    num_pares.append(n)
  else:
    impares +=1
    num_impares.append(n)
print('en la lista hay',pares,'numeros pares que son',num_pares,'y',impares,'numeros impares que son',num_impares)


