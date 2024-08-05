from usuario import Usuario
import json
from datetime import datetime

def guardar_log(texto):
    with open("logs.txt",'a+') as archivo: # w: write, r: read
        now=datetime.now()
        archivo.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {texto}\n")

lista_usuarios=[] #vamos a guardar los usuarios que vayamos creando al leer el archivo
try:
    with open("usuarios.txt") as archivo: #abrimos el archivo
        registro=archivo.readline() #leemos una linea del archivo
        while registro: #iteramos entre las lineas del archivo
            try:
                linea=json.loads(registro) #transformamos el json en un diccionario
                usuario=Usuario(linea['nombre'],linea['apellido'],linea['email'],linea['genero'])  #nombre,apellido,email,genero
                lista_usuarios.append(usuario)           
            except json.decoder.JSONDecodeError as jde: #json.JSONDecodeError as jde:
                guardar_log(f"Error al leer el registro: {jde}")
            except AttributeError as ate:
                guardar_log(f"Error de atributo {ate}")
            except Exception as e:
                guardar_log(f"Excepción: {e}")
            else: #en caso de que no haya entrado a ninguna excepción
                print(f"Usuario creado: {usuario.nombre} {usuario.apellido}")
            finally: #realiza una acción cuando termina el bloque de try-excepts
                registro=archivo.readline()

except FileNotFoundError as fnfe:
    guardar_log(f"El archivo {fnfe.filename} no existe")

#solo para probar que quedaron bien guardados
print("listado de usuarios:")
for user in lista_usuarios:
    print(user)
