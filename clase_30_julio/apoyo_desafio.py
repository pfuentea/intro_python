def _crear_nueva_membresia(self, nueva_membresia: int):
    if nueva_membresia == 1:
        return Basico(self.correo_suscriptor, self.numero_tarjeta)    
    elif nueva_membresia == 2:
        return Familiar(self.correo_suscriptor, self.numero_tarjeta)            
    elif nueva_membresia == 3:
        return SinConexion(self.correo_suscriptor, self.numero_tarjeta)          
    elif nueva_membresia == 4:
        return Pro(self.correo_suscriptor, self.numero_tarjeta)