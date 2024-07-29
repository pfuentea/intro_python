from abc import abstractmethod

class Personaje:  # CLASE PADRE
    def __init__(self,nombre,salud):
        #atributos de la clase padre que serán heredados por los hijos
        self.__nombre=nombre
        self.__salud=salud #si la salud llega a 0 el personaje es derrotado

    #Método de instancia del padre que será heredado por los hijos
    def recibir_dano(self,cantidad):
        self.__salud-=cantidad
        print(f"{self.__nombre} ha recibido {cantidad} de daño. Su salud a disminuido a {self.__salud}")

    # aca utilizamos el polimorfismo , cada hijo debe llenar con su propio código
    @abstractmethod
    def accion(self,otro_personaje):
        pass
    
    # GETTER del Padre que heredaran los hijos
    @property
    def salud(self):
        return self.__salud
    
    # GETTER del Padre que heredaran los hijos
    @property
    def nombre(self):
        return self.__nombre
    
    #Método de instancia del padre que será heredado por los hijos
    def sigue_en_pie(self):
        return self.__salud > 0    

class Combatiente:
    def __init__(self,fuerza,armadura):
        self.__fuerza=fuerza
        self.__armadura=armadura
    
    # GETTER PROPIO DE LA CLASE
    @property
    def fuerza(self):
        return self.__fuerza
    
    # GETTER PROPIO DE LA CLASE
    @property
    def armadura(self):
        return self.__armadura

    def atacar(self,otro_personaje):
        damage=self.fuerza - (otro_personaje.armadura if hasattr(otro_personaje,'armadura') else 0)
        print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {damage} daño")
        otro_personaje.recibir_dano(damage)

class Hechicero:
    def __init__(self,inteligencia,mana):
        self.__inteligencia=inteligencia
        self.__mana=mana

    # GETTER PROPIO DE LA CLASE
    @property
    def inteligencia(self):
        return self.__inteligencia
    # GETTER PROPIO DE LA CLASE
    @property
    def mana(self):
        return self.__mana
    # SETTER PROPIO DE LA CLASE
    @mana.setter
    def mana(self,uso):
        self.__mana-=uso

    def lanzar_hechizo(self,otro_personaje):
        if self.mana > 0 :
            damage=self.inteligencia
            self.mana-=10
            print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {damage} daño")
            otro_personaje.recibir_dano(damage)
        else :
            print(f"{self.nombre} no tiene suficiente mana para lanzar un hechizo")


#creamos la clase Guerrero que hereda de la clase Personaje
class Guerrero(Personaje,Combatiente): #derivan de Personaje, se pone entre parentesis el nombre de la clase padre
    def __init__(self,nombre,salud,fuerza,armadura): #pedimos todos los valores para llenar los atributos
        #estos atributos son del padre, heredados por los hijos
        #self.__nombre=nombre
        #self.__salud=salud
        #self.__fuerza=fuerza  #esto esta MALO!!!
        Personaje.__init__(nombre,salud) #llama al constructor de la clase padre
        #self.__fuerza=fuerza
        #self.__armadura=armadura
        Combatiente.__init__(fuerza,armadura)

    #Método abstracto que debemos llenar en la clase hijo
    def accion(self,otro_personaje):
        self.atacar(otro_personaje)

    # Método de instancia propia del hijo

    #METODOS HEREDADOS DEL PADRE:
    # def recibir_dano(self,cantidad):
    # def sigue_en_pie(self):

class Mago(Personaje,Hechicero): #derivan de Personaje
    def __init__(self,nombre,salud,inteligencia,mana):
        #self.__nombre=nombre
        #self.__salud=salud
        Personaje.__init__(nombre,salud) #llama al constructor de la clase padre
        Hechicero.__init__(inteligencia,mana) 

    #Método abstracto que debemos llenar en la clase hijo
    def accion(self,otro_personaje):
        self.lanzar_hechizo(otro_personaje)

    # Método de instancia propia del hijo

    #METODOS HEREDADOS DEL PADRE:
    # def recibir_dano(self,cantidad):
    # def sigue_en_pie(self):