#encoding: UTF-8
#Hector Manuel Takami Flores
#Funciones

def distancia1():   
    velocidad = 115 
    tiempo = int(input("Ingrese el tiempo del recorrido(Hrs)"))
    distancia = velocidad * tiempo
    print("La distancia recorrida a una velocidad de 1,500 Km/hr durante",tiempo,"Hrs es de:",distancia,"Kms")

def distancia2():   
    velocidad = 115 
    tiempo = int(input("Ingrese el tiempo del recorrido(Hrs)"))
    distancia = velocidad * tiempo
    print("La distancia recorrida a una velocidad de 1,500 Km/hr durante",tiempo,"Hrs es de:",distancia,"Kms")

def tiempo ():
    distancia = int(input ("Ingrese la distancia que se busca recorrer(Kms)"))
    velocidad = 115
    tiempo = distancia / velocidad
    print("Usted tardara:",tiempo,"Hrs","en recorrer",distancia,"Kms")
    
distancia1 ()
distancia2 ()    
tiempo ()    
print("¡Que tenga buen viaje!")