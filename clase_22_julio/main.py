from medicamento import Medicamento

nombre = input("Ingrese nombre del medicamento:\n")
stock = int(input("Ingrese stock del medicamento:\n"))
precio_bruto = int(input("Ingrese precio bruto del medicamento:\n"))
# instanciamos un objeto de la clase Medicamento
aspirina=Medicamento(nombre,stock)
aspirina.precio=precio_bruto

nombre = input("Ingrese nombre del medicamento:\n")
stock = int(input("Ingrese stock del medicamento:\n"))
precio_bruto = int(input("Ingrese precio bruto del medicamento:\n"))
# instanciamos un objeto de la clase Medicamento
paracetamol=Medicamento(nombre,stock)

paracetamol.precio=precio_bruto

aspirina.mostrar_info() 

print(aspirina)

print(paracetamol)


