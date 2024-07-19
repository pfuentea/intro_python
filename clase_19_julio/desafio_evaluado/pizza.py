# Requerimiento 1
class Pizza():
    precio=10000
    tamano="familiar"

# Requerimiento 2
    @staticmethod
    def validar_elemento(elemento, lista):
        return elemento in lista
        
        # if elemento in lista:
        #     return True
        # return False
# Requerimiento 3
    def solicitar_pizza(self):
        self.masa=""
        self.proteina=""
        self.vegetales=[]

        self.proteina=input("Ingrese la proteina(pollo, vacuno, carne vegetal)").lower()
        self.vegetales.append(input("Ingrese vegetal 1 (tomates,aceitunas, champiñones)").lower())
        self.vegetales.append(input("Ingrese vegetal 2 (tomates,aceitunas, champiñones)").lower())
        self.masa=input("Ingrese tipo de masa (tradicional,delgada)")
# Requerimiento 4
        self.validar= Pizza.validar_elemento(self.proteina,['pollo', 'vacuno','carne vegetal']) and Pizza.validar_elemento(self.vegetales[0],['tomates', 'aceitunas','champiñones']) and Pizza.validar_elemento(self.vegetales[1],['tomates', 'aceitunas','champiñones']) and Pizza.validar_elemento(self.masa,['tradicional','delgada'])



