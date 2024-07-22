class Medicamento():  #la firma de la clase (cabecera) #nombres se escriben con pascal-case
    descuento=0.05
    #iva=0.18
    impuesto_valor_agregado=0.18

    #definimos el método inicial para crear un obejto de la clase
    #constructor, es un método de instacia
    # 1.- el el primero que se ejecuta cuando creamos un objeto
    # 2.- no lo ejecutamos por su nombre __init__
    # 3.- solo se ejecuta una vez 
    # 4.- se ejecuta de forma automatica

    def __init__(self,nombre, stock=0):
        self.precio_neto=0     # precio bruto, sin impuestos, sin descuentos, sin comision del jefe de turno  
        self.precio_bruto=0
        self.descuento=0
        self.nombre=nombre
        self.stock= stock
        self.descripcion = None 
        self.cantidad=0
        self.cantidad_en_una_tira = 10  

# método de instacia 
    @property
    def precio(self):
        return self.precio_neto

    @precio.setter
    def precio(self,precio_bruto):
        if Medicamento.valida_precio(precio_bruto):
            self.precio_bruto=precio_bruto
            precio_iva=precio_bruto*(1+self.impuesto_valor_agregado)            
            
            if  precio_iva>= 10000 and precio_iva <20000:
                self.descuento=0.1
            elif precio_iva >= 20000 : 
                self.descuento=0.2
            self.precio_neto = precio_iva*(1-self.descuento)
        else:
            print("el valor no válido") 
        return self.precio_neto
    
    
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre} ")
        print(f"Precio Bruto: {self.precio_bruto} ")
        print(f"Descuento: {self.descuento} ")
        print(f"Precio Neto: {self.precio_neto} ")
    
    @classmethod  # se pone este decorador para un MÉTODO DE CLASE. No tengo que instanciar ningun objeto para usarlo
    def get_iva(cls):
        return cls.impuesto_valor_agregado
    
    # un método de instancia necesita que el objeto sea creado
    def get_descuento(self):
        return self.descuento
    
    def otro_metodo(self):
        self.impuesto_valor_agregado

    @staticmethod
    def peridicidad():
        return [8,16,24]
    
    @staticmethod
    def valida_precio(precio):
        if precio >= 0:
            return True
        return False
    
    # método de instacia 
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre} ")
        print(f"Precio Bruto: {self.precio_bruto} ")
        print(f"Descuento: {self.descuento} ")
        print(f"Precio Neto: {self.precio_neto} ")

    def __str__(self):
        return f"Nombre: {self.nombre}  Precio Bruto: {self.precio_bruto}"







