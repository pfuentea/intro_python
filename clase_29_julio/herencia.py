from personaje import Guerrero,Mago
import random

guerrero=Guerrero('Aragorn',100,20,10)
mago=Mago('Gandalf',80,20,60)

turno=1
while guerrero.sigue_en_pie() and  mago.sigue_en_pie():
    print(f'Turno {turno}')
    if random.choice([True,False]): 
        #atacra el guerrero
        guerrero.accion(mago)
    else:
        #ataca el mago
        mago.accion(guerrero)
    turno+=1

if guerrero.sigue_en_pie():
    print(f"{guerrero.nombre} el guerrero, es el victorioso")

else:
    print(f"{mago.nombre} el mago, es el victorioso")
