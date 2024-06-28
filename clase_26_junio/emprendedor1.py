print("Bienvenido a Emprendedor v1")
print("Calculo de utilidades Utilidades=P*U-GT ")

try:
    precio=int(input("Ingrese el precio de suscripción :"))
except:
    print("Error en el ingreso de precio")

usuarios=int(input("Ingrese la cantidad de usuarios :"))
gasto=int(input("Ingrese el gasto total: "))

print("Su utilidad es : ",precio*usuarios-gasto)