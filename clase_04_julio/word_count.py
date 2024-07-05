with open("lorem_ipsum.txt", "r") as file:
    texto=file.read()
    
    caracteres_distintos=set(texto)
    palabras_distintas=set(texto.split(" "))


    print(f"EL numero de caracteres distintos es : {len(caracteres_distintos)}")
    print(f"EL numero de palabras distintas es : {len(palabras_distintas)}")
