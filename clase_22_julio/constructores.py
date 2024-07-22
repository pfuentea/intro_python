class Persona():
    def __init__(self,p_name,p_apellido,edad=0 ): # el parametro 2 es el que toma el valor del argumento cuando se crea
        v_nombre1 = "Ernesto"
        self.nombre2 = p_name #asignar el valor que tiene el parametro p_nombre al atributo nombre2
        self.apellido = p_apellido
        self.edad= edad

p1=Persona('Armando','Perez') # 1 argumento
p2=Persona('Rubén','Fernandez',18)

print(f"persona 1:{p1.edad}")  
print(f"persona 2:{p2.edad}")  