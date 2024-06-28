# esto es un comentario
# print nos sirve para imprimir mensajes al usuario
#print("buenas noches")

'''
esto
es
un
comentario
multilinea
'''
# para definir una variable, escribimos su bombre y le damos un valor
entero = 2 # int
texto ="estO eS uN textO"  # str
decimal=0.7 # float
proposicion=False # bool: verdadero o falso

#print(type(entero)) 

# otros tipos de datos u objetos
# listas 
lista = [4,7,2,8,10,'',15] #list
#para ver lo que contiene
#print(lista[2])  # ver el contenido de un indice de la lista
#print(lista)  # ver el contenido de una lista
lista[3]=1552 #asigno un nuevo valor al indice 3
#print(lista[3])  #reviso el contenido del indice 3
lista.append("Leo")#agregar un nuevo valor al final de la lista original
lista.insert(4,"nuevo") #agrega en el indice que le digamos
#print(lista) 

matriz=[ [1,2], [3,4] ] #cada vector es una fila de una matriz

#print(matriz[1][1])  #ver el contenido de una matriz 

#tuplas
tupla = (4,7,2,8,10,'',15) #tuple
x=3
y=4
par_ordenado=(x,y) 

#set
conjunto = {4,7,2,8,10,'',15} #set

#diccionarios  tienen llaves o keys y un valor asociado a la llave
diccionario = {"nombre": "juan", 
            "apellido": "perez", 
            "edad": 20 ,
            "hijos": ["Miguel","Pedro","Bruno"] 
                } # dict

diccionario = { "nombre": "juan", "apellido": "perez", "edad": 20 , "hijos": ["Miguel","Pedro","Bruno"] ,"nombre":"jose" } # dict

elemento_nuevo={"ciudad":"Copiapó"}

diccionario.update(elemento_nuevo)

print(diccionario["ciudad"])

#print(type(conjunto)) 

#METODOS , transforman en un nuevo resultado
print(texto)
print(texto.upper()) # cambiar a mayusculas todas las letras 
print(texto.lower()) # cambiar a minusculas todas las letras 
print(texto.title()) # capitaliza el texto
print(len(texto)) # calcula la cantidad de elementos
print(texto.count("tO")) #cuenta la cantidad de apariciones de una cadena
print(texto.find("eS")) #devuelve el indice de la primera aparicion de una cadena
#encadenamiento de metodos 

print(texto.lower().count("to")) #se van realizando las transformaciones de izquierda a derecha
lista2=["palabras","separadas","por","comas"]

palabras=set(texto) # construimos un CONJUNTO con las letras de la variable texto
print(palabras)
nueva_frase="/".join(lista2) #junta los elementos del conjunto o lista
print(nueva_frase) 





