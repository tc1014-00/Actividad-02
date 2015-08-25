#encoding: UTF-8
# Autor: Manuel Eduardo Zavala Gómez
# Descripcion: Total de comida

# A partir de aqui escribe tu programa
comida=int(input("Total de tu comida"))
subtotal=(comida)
propina=(subtotal*.15)
iva=(subtotal*.16)
total=(subtotal+propina+iva)
print("Costo de la comida:$%.2f"% comida)
print("Propina:$%.2f"% propina)
print("Iva:$%.2f"% iva)
print("Total a pagar:$%.2f"% total)
      


'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
