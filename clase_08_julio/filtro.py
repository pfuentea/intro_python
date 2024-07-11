import sys

def filtro(diccionario,umbral,direccion='mayor'):
    resultado=[]
    if direccion == 'mayor':
        for llave,valor in diccionario.items():
            if valor > umbral:
                resultado.append(llave)
    elif direccion == 'menor':
        for llave,valor in diccionario.items():
            if valor < umbral:
                resultado.append(llave)
    else:
        print('Lo sentimos, no es una opción válida')
    return resultado

#diccionario con los precios
precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
    }
#1 argumento, es el umbral
umbral = int(sys.argv[1])
# 2do argumento es la direccion (mayor o menor)
direccion="mayor"
if len(sys.argv) == 3:
    direccion=sys.argv[2].lower()

# en este punto voy a tener una lista con los productos
productos=filtro(precios,umbral,direccion) 
if direccion=='mayor' or direccion=='menor':
    print(f" Los produtos {direccion}es al umbral son:{', '.join(productos)}"   )













