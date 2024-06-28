print("Bienvenido a Emprendedor v3")
print("Calculo de utilidades Utilidades=P*U-GT ")
print("Ingrese solo números enteros ")

precio=int(input("Ingrese el precio de suscripción :"))
usuarios=int(input("Ingrese la cantidad de usuarios :"))
gasto=int(input("Ingrese el gasto total: "))
utilidades=int(input("Ingrese las utilidades del año anterior: "))
u=precio*usuarios-gasto

print(f"Su utilidad es : {u}") 
print(f"La razón entre año actual y anterior es:{u/utilidades:.2f}")

