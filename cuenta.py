#encoding: UTF-8
#Brian Saggiante Parra, A01377511
#Total a pagar de una cuenta

comida=int(input('comida')) #$250.ºº
propina=.15*comida
IVA=.16*comida

totalDePago=comida+propina+IVA

print(comida)
print(propina)
print(IVA)
print('El total de la comida es de $',totalDePago)