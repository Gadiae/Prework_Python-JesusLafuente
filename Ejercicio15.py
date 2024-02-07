'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''

minutos = 230
horas = minutos // 60
minutos_rest = (minutos % 60)
print (minutos, 'minutos equivalen a',horas, 'horas y', minutos_rest, 'minutos')
