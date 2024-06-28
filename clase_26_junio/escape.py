import math # importamos la biblioteca math para utilizar la raiz cuadrada

print("Bienvenido a V-scape")
print("A continuación vamos a calcular la velocidad de escape ")

radio= float(input("Ingrese la el radio del planeta en Km :"))
gravit = float(input("Ingrese la constante de gravedad g (m/s2): ")) #cast a float para asegurarnos al momento de multiplicar

vel_esc=math.sqrt(2*gravit*radio*1000) #hacemos el calculo de la velocidad de escape

print(f"La velocidad de Escape es {vel_esc:.1f} [m/s]")
