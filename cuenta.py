#encoding: UTF-8

# Autor: Jorge Daniel Juárez Ruiz, A01376425
# Descripcion: Calcular el total a pagar con propina e IVA

s= int(input("El costo de la comida es"))
p= (s*0.15)
i= (s*0.16)
t= s+p+i
print("Costo de la comida $%5.2f" %(s))
print("Propina $%5.2f" %(p))
print("IVA $%5.2f" %(i))
print("Total a pagar $%5.2f" %(t))

'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
