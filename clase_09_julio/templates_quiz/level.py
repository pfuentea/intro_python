def choose_level(n_pregunta, p_level):
    level=0
    # Construir lógica para escoger el nivel
    # p_level: preguntas por nivel (1,2,3)
    # n_pregunta: numero de pregunta 
    ##################################################
    if n_pregunta<=p_level: #p_level=2
        level='basicas'
    elif n_pregunta<=p_level*2:
        level='intermedias'
    elif n_pregunta<=p_level*3:
        level='avanzadas'
    elif n_pregunta<=p_level*4:
        level='hell'
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(1, 2)) # básicas
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(4, 2)) # intermedias
    print(choose_level(5, 2)) # avanzadas
    print(choose_level(6, 2)) # avanzadas

    print(choose_level(4, 3)) # intermedias
    print(choose_level(8, 3)) # intermedias
    