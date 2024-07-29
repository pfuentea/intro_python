from personaje import Personaje
import random 

print("Bienvenido a GRAN FANTASIA")
nombre=input("Ingrese el nombre de su personaje: ")

protagonista=Personaje(nombre)
print(protagonista.estado)

print("¡Oh no!, ¡Ha aparecido un Orco!")
orco=Personaje("Orco")


pelea=True
while(pelea):
    
    probabilidad=protagonista.probabilidad_de_ganar(orco)
    prob_orco = random.random()

    opcion=Personaje.batalla(probabilidad)
    if opcion==1 :
        if probabilidad > prob_orco:
            protagonista.estado = 50
            orco.estado = -30
            print("¡Le has ganado al orco, felicidades!")
            print("¡Recibirás 50 puntos de experiencia!")
        else:
            protagonista.estado = -30
            orco.estado = 50
            print("¡Has perdido contra el orco, lo lamento!")
            print("Perderas 30 puntos de experiencia!")
        print(protagonista.estado)
    elif opcion==2:
        print(" ¡Has huido! El orco ha quedado atrás.")
        break



