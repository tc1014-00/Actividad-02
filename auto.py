#encoding: UTF-8

# Autor: Jorge Daniel Juárez Ruiz, A01376425
# Descripcion: Calcula la distancia o tiempo a partir de velocidad

t1=int(input("Tiempo 1"))
t2=int(input("Tiempo 2"))
d3=int(input("Distancia 3"))
d1=t1*115
d2=t2*115
t3=d3/115
print("Distancia recorrida en",t1,"horas:",d1)
print("Distancia recorrida en",t2,"horas:",d2)
print("Tiempo para recorrer",d3,"km:",t3)

'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Distancia recorrida en 6 horas: 690
Distancia recorrida en 10 horas: 1150
Tiempo para recorrer 500 km: 4.34782608696
'''
