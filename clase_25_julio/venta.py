from item import Item

class Venta():
    def __init__(self):
        self.__detalle=[]

    def mostrar_detalle(self):
        for item in self.__detalle:
            print(item)
    
    def agregar_producto(self,nombre,cantidad):
        item = Item(nombre, cantidad)
        self.__detalle.append(item)
