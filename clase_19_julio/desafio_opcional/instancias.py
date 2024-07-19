from te import Te
# Requerimiento 4
#Parte a
te1 = Te()
te2 = Te()
#parte b
tipo_te1=type(te1)
tipo_te2=type(te2)
#parte c
print(f"El tipo del té 1 es: {tipo_te1}")
print(f"El tipo del té 2 es: {tipo_te2}")

#parte d
if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo")
else:
    print("“Los objetos no son del mismo tipo")