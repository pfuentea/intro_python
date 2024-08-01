class Error(Exception):
    pass
class DimensionError(Error):
    def __init__(self,mensaje,dimension,maximo):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            mensaje=self.mensaje
            if self.dimension:
                mensaje += f" Se ingresó la dimensión :{self.dimension} "
            if self.maximo:
                mensaje += f" El valor máximo permitido es: {self.maximo} "
            return mensaje
        