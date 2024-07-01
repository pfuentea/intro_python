import time

def sumar_n_primeros(numero): # si n es 10= 1+2+3+4+5+6+7+8+9+10
    total=0
    contador=1
    while contador <= numero:
        total+=contador
        contador+=1   
    return total

def sumar_n_primeros2(numero): # si n es 10= 1+2+3+4+5+6+7+8+9+10
    total=0 #acumulador
    for i in range(1,numero+1): #rango=range(10)= 0....9
        total+=i  # total=total+1 (acumulador)
    return total

def sumar_n_primeros3(numero):
    return (numero*(numero+1))//2 

# para probar el método

# numero = int(input("Ingrese un número entero: "))
# suma=sumar_n_primeros(numero) 
# print(f"La suma de los primeros {numero} enteros es {suma}")

# sumar los primeros n numeros PARES   17:42
# sin CHATGPT!!!

def suma_numero_pares(numero):
    total=0 #acumulador
    for i in range(2,numero+1,2): #rango=range(10)= 0....9
        total+=i  # total=total+1 (acumulador)
    return total

def suma_numero_pares2(numero):
    total=0 #acumulador
    for i in range(1,numero+1): #rango=range(10)= 0....9
        if( i%2 ==0):
            total+=i  # total=total+1 (acumulador)
    return total

def suma_numero_pares3(numero):
    if(numero%2==0):
        mitad=numero//2
    else:
        mitad=(numero-1)//2    
    return mitad*(mitad+1)


numero = int(input("Ingrese un número entero para sumar los pares: "))
suma=suma_numero_pares3(numero) 
print(f"La suma de los primeros {numero} pares es {suma}")





