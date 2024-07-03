opciones=['piedra','papel','tijera']

#trabajando con listas:
#las listas van desde el indice 0 al n-1 cuando tienen n elementos
#acceso a los elementos de la lista
primer_valor=opciones[0]
print(primer_valor) 

#podemos agregar elementos al final
opciones.append('lagarto')
print(opciones)

#podemos agregar elementos en una posicion especifica, por ejemplo en el indice 2

opciones.insert(2,'spock')

print(opciones)

opciones.insert(4,'spock') 
print(opciones)
# quitar el ÚLTIMO  elemento de la lista
opciones.pop()
print(opciones)

#LIFO : last in first out  (PILAS o STACK) 
# usamos append y pop

#FIFO : first in first out
# el primero de la fila es el primero que sale

#quitar el primer elemento de la lista que coincida
opciones.remove('spock')
print(opciones)

conjunto=set(opciones) # transformamos la lista en un conjunto de elementos únicos
new_opciones=list(conjunto) #transformar un conjunto a una lista
print(new_opciones)

new_opciones.sort() #ordenamos la lista internamente
print(new_opciones) 

new_opciones.reverse() #ordenamos la lista internamente
print(new_opciones)

if 'lagarto' in new_opciones:  #validamos que el elemento exista en la lista con el operador IN 
    indice= new_opciones.index('lagarto')
    new_opciones.pop(indice)
else:
    new_opciones.append('lagarto')
print(new_opciones)

#ENUMERATE

colores=['rojo','azul','verde','amarillo','violeta','cafe']

for indice, color in enumerate(colores):
    print(f"indice:{indice},color:{color} ")
    
# ZIP colores,opciones
lista_zip= zip(colores,opciones,new_opciones) 

#lista_zip (rojo,piedra,tijera) , (azul,papel,spock) ,()

print(colores)
print(opciones)
print(new_opciones)

for a,b,c in lista_zip:
    print(f"sabor:{a},opcion:{b} ,new:{c}")

for e2 in colores:
    print(e2.upper())

set_colores=set(colores)
print(set_colores) #  a = { 1,3,5,7,9 } # a son los numeros impares hasta el 10

for i in range(0,3):
    for j in range(i,3):
        print(f"i:{i},j:{j}")

# COMPREHENSIONS
# GENERA UNA LISTA DE VALORES
# [expresion for item in iterable if condicion]
cuadrados = [ x**2 for x in range(10) ]
print(cuadrados)
c=[]
for x in range(10):
    c.append(x**2)

cuadrados_pares = [ x**2 for x in range(10) if x%2==0 ]

print(cuadrados_pares)
c2=[]
for x2 in range(10):
    if x2 %2==0:
        c2.append(x2**2)

cuadrados_pares = { x**2 for x in range(10) if x%2==0 }
print(cuadrados_pares)

# diccionarios
# { llave_expresion : valor_expresion for elemento in secuencia }
dicciona1={'llave1':'valor1' , 'llave2':'valor2' ,'llave1':'valor3'}

cuadrados_dict={ x : x**2 for x in range(10) } 
print(cuadrados_dict)
















