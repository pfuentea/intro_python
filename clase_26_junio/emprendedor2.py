print("Bienvenido a Emprendedor v2")
print("Calculo de utilidades Utilidades=P*U-GT ")

try:
    precio=int(input("Ingrese el precio de suscripción :"))
except:
    print("Error en el ingreso de precio")

usuarios=int(input("Ingrese la cantidad de usuarios :"))

usuarios_premium = int(input("Ingrese la cantidad de usuarios premium:"))

gasto = int(input("Ingrese el gasto total: "))

print(f"Su utilidad total  es : {(1.5*precio*usuarios_premium)+(precio*usuarios)-(gasto)} " ) 
# primero se multiplica o divide
# luego se suma o resta
