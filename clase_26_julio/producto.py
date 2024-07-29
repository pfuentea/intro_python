class Producto():
    def __init__(self,nombre,precio,stock=0):
        self.__nombre=nombre
        self.__precio=precio
        self.__stock=stock
        self.__sku=12398273982173

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self,stock):
        self.__stock=stock if stock > 0 else 0

    def __add__(self,otro_producto):
        return self.__stock+otro_producto.__stock
    
    def __sub__(self,otro_producto):
        return self.__stock-otro_producto.__stock
    
    def __eq__(self,otro_producto):
        return self.__nombre==otro_producto.__nombre
    



jabon=Producto('jabón',1000,15)

plato_spaguetti=Producto('Spaguetti',10000)