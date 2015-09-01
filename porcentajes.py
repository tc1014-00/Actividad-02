#encoding: UTF-8

# Autor: Mauricio Alejandro Medrano Castro, A01272273
# Descripcion: Calcular porcentajes

# A partir de aqui escribe tu programa

alumnosHombres = int(input("Alumnos Hombres")) 

alumnosMujeres = int(input("Alumnos Mujeres")) 

alumnosTotales = alumnosHombres + alumnosMujeres 

Hombres = int(alumnosHombres * 100/alumnosTotales) 

Mujeres = int(alumnosMujeres * 100/alumnosTotales) 

print ( "Total de Alumnos:", alumnosTotales, "alumnos")

print ( "Alumnos Hombres:",Hombres,"%")

print ("Alumnos Mujeres:", Mujeres,"%") 


'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
