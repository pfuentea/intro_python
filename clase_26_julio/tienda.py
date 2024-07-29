from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self,nombre,costo_delivery):
        self.__productos = []
        self.__nombre=nombre
        self.__costo_delivery=costo_delivery

    @abstractmethod
    def ingresar_producto(self,nombre,precio,stock):
        pass
    @abstractmethod
    def listar_productos(self):
        pass
    @abstractmethod # son compromisos por parte de las clases hijos
    def realizar_venta(self,nombre_producto,cantidad):
        pass

    def saludar(self):
        return "HOLA!"
    
    def ingresar_producto(self, producto, cantidad):
        if producto.nombre in self.__productos:
            self.__productos[producto.nombre].stock += cantidad
        else:
            self.__productos[producto.nombre] = producto

class TiendaRestaurant(Tienda):
        
    def ingresar_producto(self,nombre,precio):
        p=Producto(nombre,precio)
        if p not in self.__productos: 
            self.__productos.append(p)
        
    
    def listar_productos(self):
        pass

    def realizar_venta(self,nombre_producto,cantidad):
        pass

    def ingresar_producto(self,nombre,precio,stock):
        p = Producto(nombre,precio,stock)
        if len(self._lista_productos) == 0:
            self._lista_productos.append(p)
        else:
            for producto in self._lista_productos:
                if producto.nombre == p.producto:
                    producto._stock = p.stock
                else:
                    self._lista_productos.append(p)
                    
    def ingresar_producto(self,nombre,precio):
        p = Producto(nombre,precio,0)
        if len(self._lista_productos) == 0:
            self._lista_productos.append(p)
        else:
            for producto in self._lista_productos:
                if producto.nombre != p.producto:
                    self._lista_productos.append(p)

class TiendaSupermercado(Tienda):
    def ingresar_producto(self,nombre,precio,stock):
        p=Producto(nombre,precio,stock)
        if p not in self.__productos: 
            self.__productos.append(p)
        else:
            indice=self.__productos.index(p)
            self.__productos[indice]=self.__productos[indice]+p
    
    def listar_productos(self):
        pass

    def realizar_venta(self,nombre_producto,cantidad):
        pass

class TiendaFarmacia(Tienda):
    def ingresar_producto(self,nombre,precio,stock):
        p=Producto(nombre,precio,stock)
        if p not in self.__productos: 
            self.__productos.append(p)
        else:
            indice=self.__productos.index(p)
            self.__productos[indice]=self.__productos[indice]+p

    def listar_productos(self):
        pass

    def realizar_venta(self,nombre_producto,cantidad):
        pass


mcdonald=TiendaRestaurant('doggis',2000)  

