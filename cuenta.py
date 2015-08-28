#encoding: UTF-8

# Autor: PaolaCastilloNacif, A01376654
# Descripcion: El programa mostrará el IVA, la propina y el total de una comida.

# A partir de aqui escribe tu programa

a=float(input("Costo de su comida"))
print("Costo de la comida:$",a)

b=0.15 
c=(a*b)
d=(a+c)
print ("IVA:$",c)

e=0.16
f=(a*e)
print ("Propina:$",f)
g=(d+f)
print("Total a pagar:$",g)

'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
