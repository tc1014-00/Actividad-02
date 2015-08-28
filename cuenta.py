#encoding: UTF-8

# Autor: Ernesto Cruz López A01169052
# Descripcion: Calcular el costo total de una comida en un restaurante

# A partir de aqui escribe tu programa

comida=int(input("Costo de su comida"))
propina=comida*.15
iva=comida*.16
total=comida+propina+iva

print("Costo de la comida: $%0.2f" % (comida))
print("Propina: $%0.2f" % (propina))
print("Iva: $%0.2f" % (iva))
print("Total a pagar: $%0.2f" % (total))



'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
