import sys

def imc(peso,altura):
    return peso/(altura*altura)

def clasificacion(indice):    
    if indice < 18.5:
        return "Bajo Peso"
    elif indice < 25:
        return "Adecuado"
    elif indice < 30:
        return "Sobrepeso"
    elif indice <35:
        return "Obesidad grado 1"
    elif indice < 40:
        return "Obesidad grado 2"
    else:
        return "Obesidad grado 3"

#recibir peso en KG, altura en CM
# al pasar los valores por la consola (ARGUMENTOS) se genera una lista llamada argv
peso=float(sys.argv[1])
altura=float(sys.argv[2])/100

#print(sys.argv[0])

#calcular IMC
indice=imc(peso,altura)

#clacular la clasificacion e imprimir
print(f"su IMC es {indice:.2f}")
print(f"La clasificacion OMS es: {clasificacion(indice)}")