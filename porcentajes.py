#encoding: UTF-8
# Autor: David Salvador Ruiz Roa, A01377556
# Descripcion: programa que calcula el porcentaje de hombres y mujeres inscritos en una clase.
# A partir de aqui escribe tu programa

H = int(input("Hombres inscritas"))
M = int(input("Mujeres inscritas"))

Total = (H+M)
Hi = ((H*100)//Total)
Mi = ((M*100)//Total)

print("Total inscritos: ",Total)
print("% de mujeres: ",Mi,"%")
print("% de hombres: ",Hi,"%")

'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
