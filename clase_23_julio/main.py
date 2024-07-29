class Pelota():
    def __init__(self, tamanio:int = 0):
        self.tamanio = tamanio
        self.color="rojo"
    def __add__(self, other):
        return self.tamanio + other.tamanio
    def __eq__(self, other):
        return self.tamanio == other.tamanio

p1 = Pelota(16)
p2 = Pelota(16)
p3 = p2

# Salida: False
print(p1 == p2)  
# Salida: True
print(p2 == p3)  

# print(p1+p2) 

class Coordenada():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, other):
        nuevo_x = self.x + other.x
        nuevo_y = self.y + other.y
        return Coordenada(nuevo_x, nuevo_y)
    
    def __eq__(self, other):
        compara_x = self.x == other.x
        compara_y = self.y == other.y
        return compara_x and compara_y
    
c1 = Coordenada(5, 10)
c2 = Coordenada(-5, 10)
suma_coordenadas = c1 + c2

# print(type(suma_coordenadas)) 

# print(f"({suma_coordenadas.x},{suma_coordenadas.y})")

c1 = Coordenada(-5, 10)
c2 = Coordenada(-5, 10)
# Salida: True
print(c1 == c2)