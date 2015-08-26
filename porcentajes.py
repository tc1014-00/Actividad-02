#encoding: UTF-8

# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estas resolviendo.

# A partir de aqui escribe tu programa

hombres = int( input("Numero de hombres"))
mujeres = int( input("Numero de mujeres"))

alumnos = hombres + mujeres

porhombres = hombres * 100 / alumnos
pormujeres = mujeres * 100 / alumnos

print("Total de alumnos:",alumnos)
print("Procentaje de hombres: %.0f%%" %porhombres)
print("Procentaje de mujeres: %.0f%%" %pormujeres)


'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
