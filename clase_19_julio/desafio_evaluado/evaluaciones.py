from pizza import Pizza
#Requerimiento 5-a
print(f"EL precio de la pizza es {Pizza.precio} y el tamaño es {Pizza.tamano} ")
#Requerimiento 5-b
respuesta="no"
if Pizza.validar_elemento('salsa de tomate',['salsa de tomate','salsa bbq']):
    respuesta="si"
print(f"La salsa de tomate {respuesta} se encuentra en la lista")

#Requerimiento 5-c
pedido=Pizza()
pedido.solicitar_pizza()
#Requerimiento 5-d
print(f"La pizza es de {pedido.proteina} con {', '.join(pedido.vegetales)} de masa {pedido.masa} y ¿es valida?{pedido.validar}")

#Requerimiento 5-e
#print(f"La clase pizza es  {Pizza.validar} ")
