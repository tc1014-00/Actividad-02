#encoding: UTF-8
# Autor: Manuel Eduardo Zavala Gómez A01375832
# Descripcion: Calcular porcentajes

# A partir de aqui escribe tu programa
hombres=int(input("Hombres inscritos"))
mujeres=int(input("Mujeres inscritas"))
total=(hombres+mujeres)
porcentajeMujeres= ((mujeres*100)/total)
porcentajeHombres=((hombres*100)/total)
print("Total inscritos:",total)
print(" Porcentaje de mujeres: %02i%%" % porcentajeMujeres)
print("Porcentaje de hombres: %02i%%" % porcentajeHombres)



'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
