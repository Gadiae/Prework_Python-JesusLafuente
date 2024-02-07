'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''

frase = 'crea un programa que cuente la cantidad de palabras de una oracion ingresada por el usuario'
resultado = len(frase.split())

print('la frase tiene', resultado, 'palabras')