#encoding: UTF-8
# Armando Tapia Campos A01169413
# Calculando el total a pagar

subTotal = int(input("¿cual fue el total de la comida?"))
propina = subTotal*.15
IVA = subTotal*.16

total = subTotal+propina+IVA

print("Costo de la comida", subTotal)
print("Propina:", propina)
print("IVA:", IVA)
print("Total a pagar:",total)



'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
