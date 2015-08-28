#encoding: UTF-8

# Autor: Sergio Alberto Herndandez Mendez, A01371446
# Descripcion: Programa que calcula el costo total de una comida incluyendo el IVA y la propina

# A partir de aqui escribe tu programa
subtotal = float (input("¿Cual es el costo de la comida?"))
propina = subtotal * 0.15
IVA = subtotal * 0.16
total = subtotal + propina + IVA
print ("Costo de la comida: $%.2f \nPropina: $%.2f \nIVA: $%.2f \nTotal a pagar: $%.2f" % (subtotal, propina, IVA, total) )

'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
