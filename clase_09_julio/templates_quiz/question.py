import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
# si quieres agregar más preguntas en el archivo de preguntas 
# se deben agregar opciones a las listas correspondientes
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    # opciones[dificultad] =  [1,2,3]
    n_elegido = random.choice(opciones[dificultad])  #3
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido) # opciones[dificultad] =  [1,2]
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f'pregunta_{n_elegido}']
    alternativas = shuffle_alt(pregunta)    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')