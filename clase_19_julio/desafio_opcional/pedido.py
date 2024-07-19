from te import Te

def menu_sabor():
    print("Que sabor de té desea?")
    print("1.-Té Negro")
    print("2.-Té Verde")
    print("3.-Agua de Hierbas")

def menu_formato():
    print("Que formato de té desea?")
    print("1.-300 grs.")
    print("2.-500 grs.")

menu_sabor()
opcion = int(input("Ingrese una opción: "))
menu_formato()
opcion2 = int(input("Ingrese una opción: "))

# a. Sabor del tipo de té (como texto)
match opcion:
    case 1:
        texto_sabor="Té Negro"        
    case 2:
        texto_sabor="Té Verde"        
    case 3:
        texto_sabor="Agua de Hierbas"  

# b. Formato (como número)
match opcion2:
    case 1:
        texto_formato=300
    case 2:
        texto_formato=500

# c. Precio (como número)
precio= Te.precio_por_formato(texto_formato)
# d. Tiempo (como número)

# e. Recomendación (como texto)
tiempo, recomendacion=Te.preparacion_recomendacion(opcion)

print(f"Se ha ingresado su pedido de {texto_sabor} de {texto_formato} grs. el cual tiene un costo de ${precio}. Recomendamos dejar preparando durante {tiempo} minutos y consumirlo preferentemente durante el {recomendacion} ")