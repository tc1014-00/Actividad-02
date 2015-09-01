#encoding: UTF-8

# Autor: Mauricio Alejandro Medrano Castro, A01272273
# Descripcion: Calcular la propina, el IVA y total de una cuenta.

# A partir de aqui escribe tu programa

subtotal = int(input("subtotal"))  
propina = subtotal * 0.15 
impuesto = subtotal * 0.16 
totalAPagar = subtotal + propina + impuesto 

print ("Subtotal: $", "%.2f" % subtotal) 
print ("Propina: $", "%.2f" % propina)
print ("Impuesto: $", "%.2f" % impuesto) 
print ("Total a Pagar: $" ,"%.2f" % totalAPagar) 



'''
Ejemplo de salida (por ahora no te preocupes por los acentos):

Suponiendo que el usuario teclea 250.

Costo de la comida: $250.00
Propina: $37.50
IVA: $40.00
Total a pagar: $327.50
'''
