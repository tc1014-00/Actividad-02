#encoding: UTF-8
#Hector Manuel Takami Flores
#Calcula el total de estudiantes y su porcentaje

hombres=int(input("Cuantos hombres estan inscritos?"))
mujeres=int(input("Cuantas mujeres estan inscritas?"))

totalAlumnos= hombres + mujeres
porHombres= (hombres*100) // totalAlumnos
porMujeres= (mujeres*100) // totalAlumnos

print("Hay", totalAlumnos,"alumnos inscritos")
print("Hombres:",porHombres,"%")
print("Mujeres:",porMujeres,"%")
