class Personaje():
    
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__nivel=1
        self.__experiencia=0
        

    @property
    def estado(self):
        return f"Nombre: {self.__nombre} \n Nivel: {self.__nivel} \n Experiencia: {self.__experiencia}"
    
    @estado.setter
    def estado(self,exp):
        self.__experiencia += exp
        if self.__experiencia >99:
            self.__nivel+=self.__experiencia//100
            self.__experiencia=self.__experiencia%100
        
        if self.__experiencia <0:
            #print(f"Bajamos un nivel por tener {self.__experiencia} exp")
            #print(f"Nivel:{self.__nivel}, le quitamos:{(self.__experiencia//100)+2}")
            self.__nivel-=(self.__experiencia//100)+2
            if self.__nivel < 1:
                self.__nivel=1
                if self.__experiencia<0 :
                    self.__experiencia=0
            else:
                #print(f"Actualizamos la exp {self.__experiencia} exp")
                self.__experiencia=self.__experiencia%100
                #print(f"nueva exp:{self.__experiencia}")
        
                
    def __lt__(self, otro):  # lower than (menor que "<" )
        return self.__nivel < otro.__nivel
    
    def __gt__(self, otro): # greater than (mayor que  ">" )
        return self.__nivel > otro.__nivel
    
    def __eq__(self, otro): # equals (iguales "==")
        return self.__nivel == otro.__nivel

    def probabilidad_de_ganar(self,other):
        if self < other:
            return 1/3
        elif self == other:
            return 1/2
        else:
            return 2/3
        
    def batalla(probabilidad):
        print(f"Tu probabilidad de ganar es {probabilidad*100}%. En caso de que ganes recibiras 50exp y el oponente perderá 30exp ")
        print(" En caso de que pierdas, perderas 30exp y el oponente ganará 50exp")
        opcion=int(input("Que deseas hacer? (1.-Atacar,2.-Huir)"))
        return opcion
    
    # n1=35
    # n2=78
    # if n1 > n2:
    #     print("35 es mayor que 78")
    # elif n1 < n2:
    #     print("35 es menor que 78")
    # else:
    #     print("35 es igual que 78")

