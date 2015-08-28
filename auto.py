#encoding: UTF-8
#Brian Saggiante Parra, A01377511
#Calcular distancia en 6 y 10 hrs. a demas de calcular el tiempo en 500km

v=int(input('velocidad')) #115km 
t=int(input('tiempo')) #6hrs
distanciaUno=v*t

print('distanciaUno: ', distanciaUno,'km')

v=int(input('velocidad')) #115km/hr
t=int(input('tiempo')) #10hrs
distanciaDos=v*t

print('distanciaDos: ', distanciaDos,'km')

d=int(input('distancia')) #500km
v=int(input('velocidad')) #115km/hr

tiempo=d/v

print('tiempo: ', tiempo, 'hrs')