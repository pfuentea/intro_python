from credito import *

def menu():
    print("1. Crédito de Consumo")
    print("2. Crédito Comercial")
    print("3. Crédito Hipotecario")


menu()
tipo = int(input("Seleccione una opcón de crédito: ")) 
monto= int(input("Introduzca un monto para el crédito: "))
correo=input("ingrese un correo de contacto: ")
if tipo==1:
    credito = SolicitudCreditoDeConsumo(monto,correo)
elif tipo==2:
    credito = SolicitudCreditoComercial(monto,correo)
elif tipo==3:
    credito = SolicitudCreditoHipotecario(monto,correo)

print(credito)