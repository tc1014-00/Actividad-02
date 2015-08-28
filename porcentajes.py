#encoding: UTF-8

# Autor: Humberto Serra Mendieta, A01377519
# Descripcion: Calcula porcentajes de hombres y mujeres inscritos en una clase

# A partir de aqui escribe tu programa
hombres=input("Hombres inscritos:")
mujeres=input("Mujeres inscritos:")
men=int(hombres)
women=int(mujeres)
total=men+women
pH=(men*100)/total
pM=(women*100)/total
print("Total de inscritos: ",total)
print("% de mujeres: ",pM,"%")
print("% de hombres: ",pH,"%")



'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
