from orden_de_compra import OrdenDeCompra

identificador = input("Ingrese el identificador: ")
monto= int(input("Ingrese el Monto: "))
total_productos= int(input("Ingrese el total de productos: "))
#codigo = input("Ingrese el código de descuento: ")

orden1=OrdenDeCompra(identificador,total_productos)
orden1.asigna_monto(monto)
orden1.mostrar_orden()

monto= int(input("Ingrese el nuevo Monto: "))
orden1.asigna_monto(monto)
orden1.mostrar_orden()