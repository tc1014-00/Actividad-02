#encoding: UTF-8

# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estas resolviendo.

# A partir de aqui escribe tu programa

#encoding: UTF-8
#Autor: Abraham Gandaria Alonso, A01377349
#Descripcion: Porcentaje

a=int(input("Hombres inscritos"))
b=int(input("Mujeres inscritas"))
c=(a+b)
print("Total inscritos:",c)

d=100
e=int((a*d)/c)
print("%de Hombres:", e,"%")

f=int((b*d)/c)
print("%de Mujeres:",f,"%")



'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
