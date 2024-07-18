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

    def __init__(self,nombre):
        self.precio=0     # precio bruto, sin impuestos, sin descuentos, sin comision del jefe de turno  
        self.nombre=nombre
        self.cantidad=0
        self.descripcion=None
    
    @classmethod  # se pone este decorador para un MÉTODO DE CLASE. No tengo que instanciar ningun objeto para usarlo
    def get_iva(cls):
        return cls.impuesto_valor_agregado
    
    
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
    def set_precio(self,precio):
        if Medicamento.valida_precio(precio):
            self.precio=precio

            if precio >= 10000 and precio <20000:
                self.descuento=0.1

            elif precio >= 20000 and precio <30000:
                self.descuento=0.2
            elif precio >= 30000 : 
            #else:
                self.descuento=0.3

        else:
            print("el valor no válido") 

        match precio:
            case 10000:
                pass
            case 20000:






