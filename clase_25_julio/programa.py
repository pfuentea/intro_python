
from venta import Venta


v=Venta()

while(True):
    print("1. Agregar Venta")
    print("2. Salir")
    opcion=int(input("Ingrese una opcion: "))

    if opcion ==1:
        nombre=input("Ingrese el nombre del producto: ")
        cantidad=int(input("Ingrese la cantidad: "))
        v.agregar_producto(nombre,cantidad)

    elif opcion ==2:
        break

v.mostrar_detalle()
