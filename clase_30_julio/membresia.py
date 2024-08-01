from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self,email,tarjeta):
        self.__email=email
        self.__tarjeta=tarjeta
    @property
    def email(self):
        return self.__email
    
    @property
    def tarjeta(self):
        return self.__tarjeta
    
    @abstractmethod
    def cambiar_suscripcion(self,nueva_membresia):
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return MembresiaBasica(self.correo_suscriptor, self.numero_tarjeta)    
        elif nueva_membresia == 2:
            return MembresiaFamiliar(self.correo_suscriptor, self.numero_tarjeta)            
        elif nueva_membresia == 3:
            return MembresiaSinConexion(self.correo_suscriptor, self.numero_tarjeta)          
        elif nueva_membresia == 4:
            return MembresiaPro(self.correo_suscriptor, self.numero_tarjeta)


class MembresiaGratis(Membresia):
    costo=0
    dispositivo=1
    def cambiar_suscripcion(self,nueva_membresia):
        if nueva_membresia>=1 and nueva_membresia <=4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

class MembresiaBasica(Membresia): #id=1
    costo=3000
    dispositivo=2
    def __init__(self,email,tarjeta):
        super().__init__(email,tarjeta)

        if isinstance(self,MembresiaFamiliar) or isinstance(self,MembresiaSinConexion):
            self.__dias_regalo=7
        if isinstance(self,MembresiaPro):
            self.__dias_regalo=15

    def cambiar_suscripcion(self,nueva_membresia):#id=1
        if nueva_membresia in [2,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

class MembresiaFamiliar(MembresiaBasica): #id=2
    costo=5000
    dispositivo=5
    def cambiar_suscripcion(self,nueva_membresia):
        if nueva_membresia in [1,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
        
    def modificar_control_parental(self):
        pass

class MembresiaSinConexion(MembresiaBasica):#id=3
    costo=3500
    dispositivo=2
    def cambiar_suscripcion(self,nueva_membresia):
        if nueva_membresia in [1,2,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
        
    def incrementar_cantidad_contenido(self):
        pass

class MembresiaPro(MembresiaFamiliar,MembresiaSinConexion):#id=4
    costo=7000
    dispositivo=6
    def cambiar_suscripcion(self,nueva_membresia):
        if nueva_membresia in [1,2,3]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
        

gratis=MembresiaGratis('correo@gmail.com','3636 2783 2389 2718')
basica=MembresiaBasica('correo@gmail.com','3636 2783 2389 2718')
familiar=MembresiaFamiliar('correo@gmail.com','3636 2783 2385 8272')
sinconexion=MembresiaSinConexion('correo@gmail.com','3636 2783 2385 8272')
pro=MembresiaPro('correo@gmail.com','3636 2783 2385 1289')