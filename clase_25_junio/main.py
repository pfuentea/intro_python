nombres=["Loreto","Fernando","Marcelo","Fernando", ]
t_nombre=tuple(nombres)
#print(t_nombre)
#print por interpolación 
#print( "EL nombre del alumno en la posicion 0 y 1 son: {} y {} ".format(nombres[0],nombres[1] , ) )

#print con formato
#print(f"Los ultimos nombres de la lista son { nombres[-1] } y {nombres[-2]}  ")
# se supone que las listas van desde el indice 0 al N-1 
# el -1 es el último elemento de la lista, el -2 es el penúltimo elemento

#ajustar la precisión de un float (decimales)

#print(f"El valor de 1/9 es { 1/9:.4} ") 

#print("este mensaje \n \t\t tiene varias \n lineas ")


# INGRESO DE DATOS

# respuesta=input("Ingrese su nombre: \n")
# respuesta2=input("Ingrese su direccion: \n")

# print(f"Bienvenido! {respuesta} que vive en {respuesta2}")

# JALISCO NUNCA PIERDE 
# 1.- solicitar un numero al usuario
# 2.- sumar 1 a la respuesta
# 3.- mostrar el resultado en pantalla diciemndo que el computador ganó 

# CONTROL DE FLUJO (IF-ELIF-ELSE)

# control + } => comentar las lineas seleccionadas 
# respuesta=input("Ingrese su altura: \n")
# # para escribir el control de flujo
# # if proposición lógica :
# if respuesta > 1.20 :
#     print("Puede subirse! ")    
# else: # cualquier otro caso 
#     print("No puede subirse! ")

# respuesta=input("Ingrese que color de la bandera le gusta más(blanco/azul/rojo): \n")

# if respuesta.lower() == "azul" and respuesta2 == "Chile" : # entonces
#     print("Como el cielo! ")
# elif respuesta.lower() == "rojo" :
#     print("Como la sangre! ")
# elif respuesta.lower() == "blanco" :
#     print("Como la nieve! ")
# else: #sino
#     print("Ese color no esta en la bandera de Chile")

#importar librerias externas
import math

valor_pi=math.pi
radio=float(input("Cual es el radio de la circunferencia: "))
perimetro=2*valor_pi*radio
print(f"El perimetro de la circunferencia es: PERIMETRO: {perimetro}/ CEIL:{math.ceil(perimetro)} / FLOOR: {math.floor(perimetro)} / ROUND: {round(perimetro)}")

# CONTAR CALORIAS
# ingresar numero de proteinas, carbohidratos y grasa
# calcular calorías= 4*(Proteinas + carbohidratos) + (9*grasa)
# mostrar resultado en pantalla














