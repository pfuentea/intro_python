# 1.- error de sintaxis => programa no funciona
# 2.- error de ejecución => programa funciona, pero se detiene en algún punto
# 

#________________EXCEPCIONES________________

'''
El try puede tener entre 2 a 4 partes:
try  (intentara hacer )
varios except
finally 
else
'''
# JUEGO DE DADOS
# crear una clase especial para las excepciones de este tipo de objeto (InvalidDiceError)
# crear una clase para el juego de dados que contiene:
## lanzamiento de dados
## juego
import random 
class Error(Exception):
    pass

class InvalidDiceError(Error):
    def __init__(self,mensaje, numero):
        self.__mensaje = mensaje
        self.__numero = numero

        @property
        def mensaje(self):
            return self.__mensaje
        
        @property
        def numero(self):
            return self.__numero
        

class JuegoDado:
    def __init__(self):
        self.__dados = {4:'D4',6:'D6',8:'D8',10:'D10',12:'D12',20:'D20'} #{2:'D2', 6:'D6'} #
        
    def lanzamiento(self,caras,tiradas):
        if caras not in self.__dados:
            raise InvalidDiceError(f'El dado {caras} no existe', caras)
        else:
            pass
        return [random.randint(1,caras) for _ in range(tiradas)] 

    
    def game_01(self):
        dados_posibles=[]
        while True:
            try:
                print("Opciones de dados:")
                for lados in self.__dados:
                    print(f'{lados}-caras : {self.__dados[lados]}')
                    dados_posibles.append(lados)
                caras = int(input("Ingrese el número de caras del dado: "))
                if caras not in dados_posibles:
                    raise InvalidDiceError(f'El dado {caras} no existe', caras)
                tiradas = int(input("Ingrese el número de tiradas: "))
                resultado = self.lanzamiento(caras,tiradas)
                print(f"El resultado de {self.__dados[caras]} es: {resultado}")
            except InvalidDiceError as e:
                print(e)
            except ValueError:
                print("Error: El valor ingresado no es un número")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                try:
                    respuesta = input("¿Desea lanzar nuevamente? (s/n): ")
                    if respuesta.lower() != 's':
                        print("Gracias por usar este juego")
                        break
                except Exception as e:
                    print(f"Error: {e}")

if __name__ == "__main__":
    juego = JuegoDado()
    juego.game_01()

