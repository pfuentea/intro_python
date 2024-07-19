class OrdenDeCompra():
    #creamos el constructor:
    #método de instancia, siempre lleva el parametro self como primer parametro
    def __init__(self,id,total_productos):
        self._identificador=id
        self.total_productos=total_productos
        self.monto=0
        ''' antes de la refactorización
        if monto >=10000 and monto <20000:
            self.codigo_descuento="10PORCIENTO"
        elif monto >=20000:
            self.codigo_descuento="20PORCIENTO"
        else:
            self.codigo_descuento=""

        if codigo_descuento !="":
            self.codigo_descuento=codigo_descuento
        '''
        self.codigo_descuento=""

    def asigna_monto(self,nuevo_monto):
        self.monto=nuevo_monto
        if nuevo_monto >=10000 and nuevo_monto <20000:
            self.codigo_descuento="10PORCIENTO"
        elif nuevo_monto >=20000:
            self.codigo_descuento="20PORCIENTO"
        print(f"Código de descuento: {self.codigo_descuento}")

    def mostrar_orden(self):
        print("-------------------------")
        print("Orden de compra: ",self.identificador)
        print("Total de productos: ",self.total_productos)
        print("Monto: ",self.monto)
        print("Codigo de descuento: ",self.codigo_descuento)
        print("-------------------------")

    @property
    def identificador(self,valor):
        #alguna validacion antes de darle un valor al atributo
        self._identificador=valor
    @property
    def identificador(self):
        # tal vez tengamos que hacer un cálculo anterior antes de entregar el resultado
        return self._identificador
