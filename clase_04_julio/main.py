# 

mi_diccionario = {'nombre': 'Alice', 'edad': 25, 'ciudad': 'Nueva York', 'correos':['correo1','correo2']}

# generar una lista con los valores del diccionario

llaves=mi_diccionario.keys()
print(llaves)

valores=mi_diccionario.values()
print(valores)


# desempaquetado significa que un metodo nos puede devolver más de un valor al mismo tiempo y debemos guardarlos en variables distintas

for clave, valor in mi_diccionario.items():
    print(f"llave:{clave}, valor:{valor}")

lista=[ x for x in range(10)  ]
print(lista)

lista_limpia=[y for y in lista  if y>=1 and y <=7 ]
print(lista_limpia)

# print( sum(lista) ) # la suma de los valores
# print( max(lista) ) # el maximo de los valores
# print( min(lista) ) # el minimo de los valores
# print( len(lista) ) # cantidad de elementos

if len(lista) > 0:
    print( sum(lista) / len(lista) )

# métodos con parametros variables:
# def suma_de_3_numero( parametro_fijos , parametro_opcionales)
def suma_de_3_numero(a,b,d,c=0,e=3 ):
    return a+b+c

def suma_de_numero( *args):
    total=0
    for elemento in args:
        total += elemento
    print(total)

suma_de_numero(1,2,3,4,5,6)

def suma_de_numero2( *args, **kwargs):
    total=0
    for elemento in args:
        total += elemento
    print(f"Total:{total}")
    print("empieza kwargs")
    for llave, valor in kwargs.items():
        print(f"llave:{llave}, valor:{valor}")

suma_de_numero2(4,5,6,nombre='Fernando',ciudad='Copiapó')


def multiplicacion_y_division(a,b):
    return a*b,a/b  #entrego dos valores en la salida

#desempaquetar el resultado
mult,divs= multiplicacion_y_division(3,4)

print(f"multiplicacion:{mult}, division:{divs}")