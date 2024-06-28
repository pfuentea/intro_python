# que es un algoritmo??
# secuencia de pasos definidas: inicio, desarrollo y un final
# desarrollo de un procedimiento, forma de resolver un problema, con varias rutas para resolverlo
# representacion de una pregunta , siguiendo un metodo podemos llegar a la respuesta
# conjunto de operaciones que siguen cierta metodologia para solucionar un problema

# algoritmo de cocina: plato tallarines sin gluten

# 0.- entrar en la cocina y verificar si existe la cocina, fideos sin gluten , utencilios, gas, agua , operador de olla 
# 1. poner la olla al fuego con agua a hervir
# 2. cuando el agua hierva agregar los fideos, 1gr sal 
# 3. esperar el tiempo de cocción o verificar si el producto esta cocido
# 4. escurrir los fideos ( sacar agua de los fideos o los fideos del agua)
# 5. darle un golpe de frio para que no se sigan cociendo
# 6. servir los fideos en un plato y agregar la salsa de tu prefer
# 7. agregar salga
# 8. servir el plato y disfrutarlo

## PROBLEMA -> ANALIZAMOS ->  BUSCAMOS LA PIEZAS PARA LA SOLUCION == DESCOMPONER EL PROBLEMA
## LLEGAMOS AL RESULTADO ESPERADO

# Pasos para calcular área de un triángulo
# pedir base > 0 y que sea un número válido
# pedir altura > 0 y que sea un número válido
# calcular area = base * altura / 2 
# mostrar resultado 10 4 5

# ITERACIONES : WHILE (mientras) - FOR (por)
# iteraciones con WHILE

edad=0
# while (edad < 18 ):
#     edad=int(input("Ingrese su edad:"))
#     if edad >= 18 : 
#         print("Usted es mayor de edad")

lista=['pedro','david','gonzalo','ruben']

# for nombre in lista:
#     print(f"nombre:{nombre}") 

diccionario = {"nombre": "juan", 
            "apellido": "perez", 
            "edad": 20 ,
            "hijos": ["Miguel","Pedro","Bruno"] 
                } 

# for llave in diccionario:
#     print(f"llave:{llave}-valor:{diccionario[llave]}")

# for llave,valor in diccionario.items():
#     print(f"llave:{llave}-valor:{valor}")

# for valor in diccionario.values():
#     print(f"valor:{valor}")

# for i in range(10):  #va desde 0 a n-1 , con 1 parametro
#     print(f"Hola{i}")

# for i in range(3,10):  # con 2 parametros, va desde 3 a n-1 
#     print(f"Hola: {i}")

# for i in range(3,20,3):  # con 3 parametros, va desde 3 a n-1 , el tercer parametro es el PASO
#     print(f"Hola: {i}") 

for i in range(20,5,-2):  # con 3 parametros, va desde 3 a n-1 , el tercer parametro es el PASO
    print(f"Hola: {i}") 

lista=list(range(8)) #genera una lista de 8 elemento 

print(lista)











