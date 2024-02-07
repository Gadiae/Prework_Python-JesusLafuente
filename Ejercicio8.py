'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

peso = 75
altura = 1.75
# La fórmula del IMC es peso/altura^2
imc = peso / altura**2

if imc<16:
  print(imc,'Delgadez severa')
elif imc<17:
  print(imc, 'delgadez moderada')
elif imc<18.5:
  print(imc, 'delgadez aceptable')
elif imc<25:
  print(imc, 'peso normal')
elif imc<30:
  print(imc, 'sobrepeso')
elif imc<35:
  print(imc, 'obeso tipo I')
elif imc<40:
  print(imc, 'obeso tipo II')
elif imc>40:
  print(imc, 'obeso tipo III')
else:
  print('datos incorrectos')
