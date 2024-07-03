import time

#instruccion BREAK
# esta instruccion sirve para salir de una iteracion antes de tiempo
contador=0 #contador
while contador < 10:
    if contador == 6 :
        break
    #print(contador)
    contador+=1    

# instruccion CONTINUE
contador2=0
while contador2 < 10:
    contador2+=1
    if contador2 % 2 == 0: # saltando los pares
        continue
    # print(contador2)

# while( 1==1 ):
#     print("soy un loop infinito!")

filas=0
tablero=""
while filas < 4:
    columnas=0
    tablero=""
    while columnas < 4:
        tablero+="[]"
        columnas+=1
    #print(tablero)
    filas+=1

contador3=0
while contador3 < 7:
    print(contador3)
    contador3+=1
    if contador3==4:
        break
else:
    print("termino el ciclo sin un break")

print(f" contador 3:{contador3}")

while contador3 < 10:
    #print("esperando el amor eterno")
    #time.sleep(1)
    contador3+=1
#print(f"llego el amor en {contador3}")

# MANEJO DE ERROR : TRY- EXCEPT- RAISE
# calculando el promedio de 3 notas
# cantidad_notas=int(input("Ingrese cuantas notas quiere promediar"))
# lista_notas=[]
# while len(lista_notas) < cantidad_notas :
#     condicion=True
#     while condicion:
#         try:        
#             nota=float(input(f"Ingrese la nota {len(lista_notas)+1}: "))
#             if nota >= 0 and nota <= 7 : 
#                 condicion=False
            
#         except ValueError:
#             print("ingresó un valor no permitido")

#     if nota > 7:
#         raise FileNotFoundError("número superior al permitido")
    
#     lista_notas.append(nota)


# print(f"su promedio de notas es:{(sum(lista_notas)/len(lista_notas))}")
# print(f"su promedio de notas es:{round(sum(lista_notas)/len(lista_notas),1)}")

# CREACION DE MÉTODOS
# Los métodos nos ayudaran a ejecutar bloques de código que sean reiterativos en nuestro
# programa, para ser usados siempre que los invoquemos
# Además de que nos sirven para reutilizar código, nos permite desglosar 
# un problema más complejo en piezas más simples.

lista1=[] #list(range(7))
lista2=list(range(20,13,-1))
# un método se declara con la palabra clave "def" y un nombre único en nuestro programa
# el nombre del método debe ser significativo para que podamos entender su función
#a=[5,1,2,4,3,6]
#b=[2,4,3,6,8,2,4]

def suma_listas(a,b): # sumar indice a indice devolvemos una lista nueva con la suma
    lista_resultado=[]
    ''' código original que fue mejorado
    if len(a) < len(b):
        lista_aux=[]
    else:
        lista_aux=b
        b=a
        a=lista_aux
    '''
    if len(a)==0:
        return b
    if len(b)==0:
        return a
    if len(a) > len(b):
        lista_aux=b
        b=a
        a=lista_aux    
    
    for i in range(len(a)):
        lista_resultado.append(a[i]+b[i])
    #print(f"el i llegó hasta {i}")
    for i in range(i+1,len(b)):
        lista_resultado.append(b[i])

    return lista_resultado

def enviar_misil(ciudad):
    pass

print(lista2)
print(lista1)
print(suma_listas(lista1,lista2)) 

# suma de los primero N números enteros:
