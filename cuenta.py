#encoding: UTF-8

# Autor: Pablo Alejandro Snchez Tadeo A01377515 
# Este programa calcula el iva y la propina de una comida.

# A partir de aqui escribe tu programa

costo = float( input("Costo total de la comida"))

propina =  costo * .15
iva =  costo *.16 
total = costo + propina + iva 

print("Costo de la comida: $%.2f" %costo)
print("propina: $%.2f" %propina)
print("IVA: $%.2f" %iva)
print("Total a pagar: $%.2f" %total)


'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
