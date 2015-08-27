#encoding: UTF-8

# Autor: Jorge Daniel Juárez Ruiz, A01376425
# Descripcion: Calcular el porcentaje de hombres y mujeres en un clase

nh= int(input("numero de hombres"))
nm= int(input("numero de mujeres"))
t= nm+ nh
ph= (nh*100)/t
pm= (nm*100)/t
print ("Total de alumnos:",t)
print ("% de hombres:",int(ph),"%")
print ("% de mujeres:",int(pm),"%")
'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
