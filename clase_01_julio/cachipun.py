import sys
import random

# recibir la opcion del jugador, validar si es un valor permitido
seleccion=sys.argv[1].lower() # ingresa: piedra, papel o tijera
opciones=['piedra','papel','tijera']

# validar si es un valor permitido
if seleccion not in opciones:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")

#calcular la opcion del computador
computador=random.choice(opciones)

#revisar quien de los dos ganó
print(f"Tu elección fue {seleccion} y la del NPC fue {computador}")

if seleccion == computador:
    print("Empate")
#condiciones para ganar
elif (seleccion == 'piedra' and computador == 'tijera') or (seleccion == 'tijera' and computador == 'papel') or (seleccion == 'papel' and computador == 'piedra'):
    print("Ganaste")
else:
    print("Perdiste")
#enviar mensaje




