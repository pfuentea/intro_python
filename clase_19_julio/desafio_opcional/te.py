#Requerimiento 1
class Te():
    tiempo_duracion=365 #atributo de clase, es común para cada instancia
    '''
    def __init__(self,sabor, formato):
        self.sabor=sabor
        self.formato=formato
        if sabor=="negro":
            self.tiempo_preparacion=3
            self.recomendacion_consumo="desayuno"
        elif sabor=="verde":
            self.tiempo_preparacion=5
            self.recomendacion_consumo="medio día"
        elif sabor=="hierbas":
            self.tiempo_preparacion=6
            self.recomendacion_consumo="atardecer"

        if formato == 300:
            self.precio=3000
        elif formato == 500:
            self.precio=5000
    '''
    #Requerimiento 2 
    @staticmethod
    def preparacion_recomendacion(sabor):
        if sabor == 1:
            return 3, "desayuno"
        elif sabor == 2:
            return 5, "mediodía"
        elif sabor == 3:
            return 6, "atardecer"

    #Requerimiento 3
    @staticmethod
    def precio_por_formato(formato):
        if formato == 300:
            return 3000
        elif formato==500:
            return 5000
        
    #Requerimiento 4: