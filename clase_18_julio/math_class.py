# generar una clase que nos permita hacer operaciones matemáticas

class Memoria:
    def __init__(self):
        self.resultado=0

    # sumar(3) , sumar (3,5,6,2,4,5,2)
    #método para sumar, 1 o más números
    def sumar(self,num, *nums): #(4,76,2525) -  **numeros=(numero1=1,numero2=34,numero3=987)
        self.resultado+=num #me suma el primer parametro
        for n in nums: 
            self.resultado+=n   # sumar los siguientes valores
        
        return self
        
    #método para restar, 1 o más números
    def restar(self,num, *nums): #(4,76,2525) -  **numeros=(numero1=1,numero2=34,numero3=987)
        self.resultado-=num #me suma el primer parametro
        for n in nums: 
            self.resultado-=n 
        
        return self

    def ver_resultado(self):
        print(self.resultado) 
        return self       

    def get_resultado(self):
        return self.resultado

ram=Memoria() # "creamos un objeto" o "instanciamos la clase Memoria"
numeros=[3,5,6,2,4,5,2]  # 27
ram.sumar(100,*numeros) #
ram.ver_resultado() 
result=ram.get_resultado() 
print(f"result:{result}")
ram.restar(*numeros)
ram.ver_resultado() 

# ENCADENAMIENTO  
print("encadenamiento")
ram2=Memoria().sumar(3,4,5).restar(10).ver_resultado().restar(5).ver_resultado()

ram3= ram2

ram3.ver_resultado() # -3 

ram2.sumar(15) 

ram3.ver_resultado() # 12

# SPOILER: BASES DE ORIENTACION A OBJETOS (PILARES DE LA ORIENTACION A OBJETOS)
# 1.- Encapsulamiento (coherencia de lógica del programa )
# 2.- Abstracción ( poder resolver el problema en un alto nivel )
# 3.- Herencia ( reutilización de código- coherencia de lógica del programa )
# 4.- Polimorfismo  ( trabajar con distintas clases ) 