#encoding: UTF-8

# Autor: Sergio Alberto Hernandez Mendez, A01371446
# Descripcion: Obtiene el total y porcentajes de hombres y mujeres en una clase a partir de la cantidad de personas de cada sexo

# A partir de aqui escribe tu programa
hombresInscritos = float (input ("¿Cual es el numero de hombres inscritos en la clase?"))
mujeresInscritas = float (input("¿Y de mujeres?"))
total = hombresInscritos + mujeresInscritas
porcentajeHombres = hombresInscritos / total * 100
porcentajeMujeres = mujeresInscritas / total * 100
print ("Total inscritos: %i \n%% de mujeres: %i%% \n%% de hombres: %i%%" % (total, porcentajeHombres, porcentajeMujeres))


'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 14 mujeres y 11 hombres.

Total inscritos: 25
% de mujeres: 56%
% de hombres: 44%
'''
