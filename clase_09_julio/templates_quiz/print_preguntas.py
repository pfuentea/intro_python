import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    # A. alternativa 1
    print(enunciado)
    indices=['A','B','C','D','E']
    '''
    numeros=[1,2,3,4]
    mezcla=zip(numeros,indices)
    [(1,'A'),(2,'B'),(3,'C'),(4,'D')]
    '''
    aux=zip(indices,alternativas)
    for ind, alt in aux:
        print(f"{ind}. {alt[0]}") 
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4