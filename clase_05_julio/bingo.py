'''
JUEGO DEL BINGO POR EL LADO JUGADOR
necesitamos el carton de los numeros generado al azar
- generar el carton
- mostrar el carton
- permitr la entrada de los numeros por consola
- llevar el registro de los números que hayan salido (ir marcandolos)
- avisar si llené una fila por primera vez o el cartón completo
-
'''
import random
def generar_tablero():
    '''
    las reglas para generar el tablero son:
    columna 1: 5 números del 1 al 15
    columna 2: 5 números del 16 al 30
    columna 3: 4 números del 31 al 45 y la posicion del medio libre
    columna 4: 5 números del 46 al 60
    columna 5: 5 números del 61 al 75
    '''
    tablero = []
    for i in range(5):
        if i == 0:
            columna= random.sample(range(1,16),5)
        elif i == 1:
            columna= random.sample(range(16,31),5)
        elif i == 2:
            columna= random.sample(range(31,46),5)
            columna[2]=0
        elif i == 3:
            columna= random.sample(range(46,61),5)
        elif i == 4:
            columna= random.sample(range(61,76),5)
        tablero.append(columna)
    return tablero

def mostrar_tablero(tablero,numeros_sacados):
    print(" B |  I |  N |  G |  O |")
    print("------------------------")
    for fila in range(5):
        for columna in range(5):
            if tablero[fila][columna] == 0:
                print(" X  ", end="| ")
            else:
                num=tablero[columna][fila]
                if num in numeros_sacados:
                    print(f"{num:02}*", end=" | ")
                else:
                    print(f"{num:02} ", end=" | ")
        print()
    print("------------------------")
    
def verificar_fila_completa(tablero,numeros_sacados):
    for fila in range(5):
        completa=True
        for columna in range(5):
            if tablero[columna][fila] != 0 and tablero[columna][fila] not in numeros_sacados:
                completa=False
                break
        if completa:
            return True
    return False

def numeros_tablero(tablero):
    numeros = set()
    for fila in range(5):       
        fila_set=set(tablero[fila])       
        numeros.update(fila_set)
    return numeros

def main():
    tablero=generar_tablero() # generar el tablero
    numeros_sin_sacar=numeros_tablero(tablero)
    numeros_sacados=set()
    todos_los_numeros={x for x in range(1,76) }
    fila_completada= False

    while True:
        # mostrar_tablero
        mostrar_tablero(tablero,numeros_sacados)
        # pedir numero
        numero=input("Introduce un numero (o 's' para terminar): ")

        if numero.lower() == "s":
            break

        try:            
            numero=int(numero)
            
            # validar que el numero sea correcto (1,75)
            if numero < 1 or numero > 75:
                print("Numero fuera del rango permitido. Intenta nuevamente.")
                continue
            
            # validar que el numero no haya sido anotado anteriormente
            if numero in numeros_sacados:
                print("Este número ya fue ingresado anteriormente. Intenta de nuevo!")
                continue
            
            # anotamos el numero
            numeros_sacados.add(numero)            
            numeros_sin_sacar.remove(numero)
            
            # verificar si completamos una fila
            if verificar_fila_completa(tablero,numeros_sacados) and not fila_completada:
                print("Primera fila que completas! Continua jugando")
                fila_completada=True            
            
            # verificar si completamos el tablero (salir del while)
            if len(numeros_sin_sacar) == 1:
                print("Completaste el cartón! FELICITACIONES!")
                break   
        except:
            print("No es valida esa opción. Solo números entre 1 y 75 o 's' ")
        
    print("Gracias por jugar")
    #mostrar estado fianl del tablero
# si completamos el tablero, salir del juego

# para ejecutar nuestro programa
if __name__=="__main__":
    main()

