#encoding: UTF-8

# Autor: Humberto Serra Mendieta, A01377519
# Descripcion: Calcula el costo total de una comida en un restaurante

# A partir de aqui escribe tu programa
cost=input("Costo de su comida:")
costo=float(cost) 
propina=costo*.15
iva=costo*.16
total=costo+propina+iva
print("Costo de su comida: $",costo)
print("Propina: $",propina)
print("IVA: $",iva)
print("Total a pagar: $",total)



'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
