#DICCIONARIOS
'''
<xml>
    <personas> 
        <nombre>Jose</nombre>
        <apellido>Sanchez</apellido>
        <edad>30</edad>
        <hijos></hijos>
    </personas>
    <direcciones>
    </direcciones>
</xml>
'''
# JSON
# data={
#     'personas':[
#         {
#             "nombre":"Jose",
#             "apellido":"Sanchez",
#             "edad":30
#             },
#         {
#             "nombre":"Marcelo",
#             "apellido":"Gonzalez",
#             "edad":35
#             }
#     ],
#     'direcciones':[]    
# }

# # nombre_variable = { 'clave1' : valor1 , 'clave2' : valor2 , ... , 'clave_n': valor_n }

# sports_directory = {
#     'deportes' : 'basquetball',
#     'implemento' : 'balón',
#     'jugador':'perez',
#     'jugador':'gonzalez'
# }
# # para acceder la data
# print(sports_directory['implemento'])  
# #para asignar un valor a una llave, por ejemplo a la llave 'deportes'
# sports_directory['deportes'] =['basquetball','futbol','tenis','natación']
# print(sports_directory['deportes'])  

# print(sports_directory['implemento'])  

# sports_directory['paises']=['Chile','Peru','Argentina']

# #del sports_directory['implemento']
# sports_directory.pop('implemento')
# canal={
#     'nombre':'youtube',
#     'canal':'programacion',
# }
# canal.update(sports_directory)

# #canal['directorio']=sports_directory

# pozo={'id':1,'coord_n':-78.1237687632,'coord_e':-12.2178372 }

# perforaciones={'malla':'mmala_1','pozo':{}}
# perforaciones['pozo']=pozo



x = [ [5,2,3], [10,8,9] ] 

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ 
    {'x': 10, 'y': 20} 
    ]
# EJERCICIOS
# 1.- cambiar el valor de 10 en x , a 15
x[1][0]=15 

# 2.- cambiar el valor de Jordan a Bryant en el diccionario students
students[0]['last_name']='Bryant'

# 3.- cambiar el valor de Messi a Andresson en el diccionario sports_directory
sports_directory['soccer'][0]='Andresson'

# 4.- Cambiar el valor 20 a 30 en z
z[0]['y']=30


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterarLista(lista):
    for i in lista:
        elemento=""
        for item in i:
            elemento += item+" - "+i[item]+", "
        print(elemento[0:-2])
        
def iterarLista2(lista):
    for i in lista:
        elemento=[]
        for item in i:
            elemento.append(item+" - "+i[item])
        print( (", ").join(elemento) )
    

# iterar el diccionario para que la salida sea 
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
#iterarLista2(students)

# iterarPorLlave(llave, lista)
# iterarPorLlave('first_name',students)
# Michael
# John
# Mark
# KB
def iterarPorLlave(llave, lista):
    for item in lista:
        if llave in item:
            print(item[llave])
        else:
            print("No existe la llave "+llave+" en el diccionario")

iterarPorLlave('first_name',students)

