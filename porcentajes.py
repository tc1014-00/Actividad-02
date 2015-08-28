#encoding: UTF-8
# Armando Tapia Campos A01169413
# Porcentaje de mujeres y hombres

mujeres = int(input("¿cuantas mujeres hay en la clase?"))
hombres = int(input("¿cuantos hombres hay en la clase?"))
 
total = mujeres+hombres
porcentajeMujeres = (mujeres/total)*100
porcentajeHombres = (hombres/total)*100

print("Total inscritos:", total)
print("% de mujeres:", porcentajeMujeres, "%")
print("% de hombres:", porcentajeHombres, "%")
 
 




'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
