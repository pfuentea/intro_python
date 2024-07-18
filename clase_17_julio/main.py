# referencia o valor
a=0
b=a  # copiando por valor
a+=1
print(b)  #se comportan como variables

class numero():
    def __init__(self,valor):
        self.valor=valor
    
    def get_valor(self):
        return f"{self.valor}"

    def set_valor(self,valor_new):
        self.valor=valor_new

uno=numero(1)
dos=numero(2)

tres=dos #copia por referencia

dos.set_valor(4)

print(uno.get_valor()) #1
print(dos.get_valor()) #4
print(tres.get_valor()) #4
