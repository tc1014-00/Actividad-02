#encoding: UTF-8
#Brian Saggiante, A01377511
#Total y porcentaje de hombres y mujeres en una clase

H=int(input('H'))
M=int(input('M'))

totalAlumnos=H+M

porcentajeH=(H/totalAlumnos)*100
porcentajeM=(M/totalAlumnos)*100

print('El total de alumnos es de ', totalAlumnos)
print('El porcentaje de hombres en el grupo es de: ' , porcentajeH,'%')
print('El porcentaje de mujeres en el grupo es de: ' , porcentajeM,'%')