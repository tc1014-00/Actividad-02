#encoding: UTF-8

# Autor:David Salvador Ruiz Roa, A01377556
# Descripcion: programa que calcula el costo total de una comida en un restaurante.

# A partir de aqui escribe tu programa

A = int(input("Csoto de su comida "))

IVA = ((16*A)/100)
Propina = ((15*A)/100)
Total = (IVA+Propina+A)

print("Costo de la comida: $",A,".00")
print("Propina: $",Propina,".00")
print("IVA: $",IVA,".00")
print("Total a pagar: $",Total,".00")


'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
