class Item():
    def __init__(self,nombre,cantidad):
        self.__nombre=nombre
        self.__cantidad= cantidad

    def __str__(self):
        return "Nombre: "+self.__nombre+" Cantidad: "+str(self.__cantidad)
