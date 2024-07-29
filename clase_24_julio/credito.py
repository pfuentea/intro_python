from abc import ABC, abstractmethod

class SolicitudCredito(ABC):

    @abstractmethod
    def valida_monto(self,monto):
        pass
    
    @abstractmethod
    def validar_correo(self,correo):
        pass

class SolicitudCreditoDeConsumo(SolicitudCredito):
    __terminaciones = (".cl", ".com")

    def __init__(self,monto,correo):
        self.__monto=self.valida_monto(monto)
        self.__correo=self.validar_correo(correo)

    @property
    def monto(self):
        return self.__monto    
    @monto.setter
    def monto(self,monto):
        self.__monto=self.valida_monto(monto)

    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self,correo):
        self.__correo=self.validar_correo(correo)

    def valida_monto(self,monto):
        if monto <1000000:
            monto=1000000
        elif monto >5000000:
            monto=5000000
        return monto
    
    def validar_correo(self,correo):
        if correo.count("@") == 1 and correo.endswith(SolicitudCreditoDeConsumo.__terminaciones):
            return correo
        else:
            return ""
    
    def __str__(self):
        return f"Crédito de Consumo :Monto:{self.__monto}, correo:{self.__correo}"

class SolicitudCreditoComercial(SolicitudCredito):
    __prohibidos = ("gmail", "outlook", "hotmail")
    __terminaciones = (".cl", ".com",".org")

    def __init__(self,monto,correo):
        self.__monto=self.valida_monto(monto)
        self.__correo=self.validar_correo(correo)

    @property
    def monto(self):
        return self.__monto    
    @monto.setter
    def monto(self,monto):
        self.__monto=self.valida_monto(monto)

    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self,correo):
        self.__correo=self.validar_correo(correo)

    def valida_monto(self,monto):
        if monto <1000000:
            monto=1000000
        elif monto >5000000:
            monto=5000000
        return monto
    
    def validar_correo(self,correo):
        if correo.count("@") == 1 and correo.endswith(SolicitudCreditoDeConsumo.__terminaciones) and not any(p in correo.lower() for p in SolicitudCreditoComercial.__prohibidos):
            return correo
        else:
            return ""
    
    def __str__(self):
        return f"Crédito Comercial:Monto:{self.__monto}, correo:{self.__correo}"

class SolicitudCreditoHipotecario(SolicitudCredito):
    __terminaciones = (".cl", ".com")

    def __init__(self,monto,correo):
        self.__monto=self.valida_monto(monto)
        self.__correo=self.validar_correo(correo)

    @property
    def monto(self):
        return self.__monto    
    @monto.setter
    def monto(self,monto):
        self.__monto=self.valida_monto(monto)

    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self,correo):
        self.__correo=self.validar_correo(correo)

    def valida_monto(self,monto):
        if monto <20000000:
            monto=20000000
        elif monto >100000000:
            monto=100000000
        return monto
    
    def validar_correo(self,correo):
        if correo.count("@") == 1 and correo.endswith(SolicitudCreditoDeConsumo.__terminaciones) :
            return correo
        else:
            return ""
    
    def __str__(self):
        return f"Crédito Hipotecario: Monto:{self.__monto}, correo:{self.__correo}"
