class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

    def __str__(self):
        return f"Nombre:{self.nombre}, Apellido:{self.apellidos},email: {self.email},genero:{self.genero}"