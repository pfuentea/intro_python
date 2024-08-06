from error import LargoExcedidoError
from anuncio import Video,Display,Social

class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.__anuncios=[] # crear una estructura con los anuncios para cargar en este atributo
        self.__nombre=nombre
        self.__fecha_inicio=fecha_inicio
        self.__fecha_fin=fecha_fin

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) <= 250:
            self.__nombre = nombre
        else:
            raise LargoExcedidoError("Mensaje")
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self,valor):
        self.__fecha_inicio=valor

    @property
    def fecha_fin(self):
        return self.__fecha_fin
    @fecha_fin.setter
    def fecha_fin(self,valor):
        self.__fecha_fin=valor

    @property 
    def anuncios(self):
        return self.__anuncios
    
    def add_anuncio(self,anuncio):
        self.__anuncios.append(anuncio)
    
    def __str__(self):
        #Nombre de la campaña: Campaña 1
        #Anuncios: 1 Video, 2 Display, 0 Social
        resultado=f"Nombre de la campaña:{self.__nombre}\n"
        #self.__anuncios
        conteo = {
            'Videos': 0,
            'Display': 0,
            'Social': 0
        }
        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                conteo['Videos'] += 1
            elif isinstance(anuncio, Display):
                conteo['Display'] += 1
            elif isinstance(anuncio, Social):
                conteo['Social'] += 1

        resultado+=f"Anuncios: {conteo['Videos'] } Video, {conteo['Display']} Display, { conteo['Social']} Social"

        return resultado