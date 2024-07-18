from medicamento import Medicamento
from farmacia import Farmacia, delivery

#instanciamos un objeto de la clase Medicamento = creamos un objeto
paracetamol=Medicamento("paracetamol") 

#imprimimos el atributo 
print(Medicamento.get_iva())    

#delivery(paracetamol) 

def suma_de_dos(a,b):
    return a+b

#llamada al metodo_estatico
lista=Medicamento.peridicidad()

precio=int(input("Favor ingrese el precio del medicamento: "))

if Medicamento.valida_precio(precio):
    print("El precio es correcto")
else:
    print("El precio no es correcto")

aspirina=Medicamento("aspirina")

if paracetamol.get_iva() == aspirina.get_iva():
    print(f"El iva es igual:{Medicamento.impuesto_valor_agregado}")

# if paracetamol.get_descuento() == aspirina.get_descuento():
#     print(f"El descuento es igual:{Medicamento.descuento}")


aspirina.set_precio(precio)
print(aspirina.get_descuento())




