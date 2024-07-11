# FACTORIAL
# 0!=1
# 1!=1  1*(0!)
# n!=n*(n-1)!

def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial(numero):
    resultado=1
    for i in range(1,numero+1): # range(1,5)=1,2,3,4,5
        resultado=resultado*i   

    return resultado


def productoria(lista):
    resultado=1
    for numero in lista:
        resultado=resultado*numero
    return resultado


def calcular(*args,**kwars): # (34,'hola',[2,3,5,7,3], {'llave1':'valor1'}) args
                            #kwargs : (variable1= 32, variable2=['a','g','r','x'])
    for variable,valor in kwars.items():
        if 'prod' in variable:
            print(f"La productoria de {valor} es {productoria(valor)}")
        elif 'fact' in variable:
            print(f"El factorial de {valor} es {factorial(valor)}" )

        # print(variable,valor)
    

import datetime as dt
def ejecucion():
    inicio= dt.datetime.now()
    factorial(150)
    factorial(150)
    factorial(150)
    factorial(150)
    factorial(150)
    fin= dt.datetime.now()
    print(f"tiempo transcurrido:{fin-inicio}")

def ejecucion2():
    inicio= dt.datetime.now()
    factorial2(150)
    factorial2(150)
    factorial2(150)
    factorial2(150)
    factorial2(150)
    fin= dt.datetime.now()
    print(f"tiempo transcurrido:{fin-inicio}")


# ejecucion()
# ejecucion2()

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6, fact_3=1)