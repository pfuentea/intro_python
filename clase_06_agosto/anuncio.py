from error import SubTipoInvalidoException
from abc import ABC, abstractmethod

class Anuncio(ABC):
    

    def __init__(self,alto,ancho,url_archivo='',url_click='',sub_tipo=''):
        if alto >0:
            self.__alto=alto
        else:
            self.__alto=1

        if ancho >0:
            self.__ancho=ancho
        else:
            self.__ancho=1

        self.__url_archivo=url_archivo
        self.__url_click=url_click
        
        

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self,valor):
        if valor > 0:
            self.__alto = valor
        else:
            self.__alto = 1

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self,valor):
        if valor > 0:
            self.__ancho = valor
        else:
            self.__ancho = 1

    @property
    def url_archivo(self):
        return self.__url_archivo
    @url_archivo.setter
    def url_archivo(self,valor):
        self.__url_archivo=valor

    @property
    def url_click(self):
        return self.__url_click
    @url_click.setter
    def url_click(self,valor):
        self.__url_click=valor

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass

class Video(Anuncio):
    FORMATO='Video'
    SUB_TIPOS=['Instream','Outstream']
    def __init__(self,duracion):
        super().__init__(1,1)
        self.__duracion=duracion

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self,valor): 
        if valor in Video.SUB_TIPOS:
            self.__sub_tipo=valor
        else:
            raise SubTipoInvalidoException()

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self,valor):
        if valor > 0:
            self.__duracion = valor
        else:
            self.__duracion = 5
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    @staticmethod
    def  mostrar_formatos(self):
        print(Video.FORMATO)
        print("============")
        for st in Video.SUB_TIPOS:
            print(f"-{st}")

class Display(Anuncio):
    FORMATO='Display'
    SUB_TIPOS=['Tradicional','Native']

    @staticmethod
    def  mostrar_formatos(self):
        print(Display.FORMATO)
        print("============")
        for st in Display.SUB_TIPOS:
            print(f"-{st}")
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO='Social'
    SUB_TIPOS=['Facebook','Linkedin']

    @staticmethod
    def  mostrar_formatos(self):
        print(Social.FORMATO)
        print("============")
        for st in Social.SUB_TIPOS:
            print(f"-{st}")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
