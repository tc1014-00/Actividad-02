#encoding: UTF-8

# Autor: Ernesto Cruz López A01169052
# Descripcion: Calcular el porcentaje de mujeres y hombres inscritos en una clase.

# A partir de aqui escribe tu programa

mujeres=int(input("Numero de mujeres:"))
hombres=int(input("Numero de hombres:"))

Total= mujeres+hombres
mujeresPor= ((mujeres*100)//Total)
hombresPor= ((hombres*100)//Total)

print("Total de inscritos:", Total)
print("%% de mujeres: %2i%%" % (mujeresPor))
print("%% de hombres: %2i%%" % (hombresPor))



'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
