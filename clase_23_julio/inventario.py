from medicamento import Medicamento

farmacia=[] # los medicamentos
#listado_de_remedios=[] # solo nombres
respuesta=True
while (respuesta):
    print("1. Agregar medicamento")
    print("2. Salir")
    opcion= int(input("Seleccione una opción:"))
    if opcion == 2:
        break
    else:
        nombre=input("Ingrese el nombre del medicamento: ")
        stock = int(input("Ingrese el stock del medicamento:"))
        #tenemos que ingresarlos a una lista, en el caso de que ya exista, debemos sumar el stock
        remedio=Medicamento(nombre,stock)

        if remedio in farmacia:
            indice= farmacia.index(remedio)
            farmacia[indice]+=remedio
        else:
            precio = int(input("Ingrese el precio del medicamento:"))
            remedio.precio=precio
            farmacia.append(remedio)
            indice= farmacia.index(remedio)
        
        farmacia[indice].mostrar_info()
        print(f"Existen {len(farmacia)} medicamentos distintos")

