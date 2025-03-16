class Persona:
    def __init__(self, cedula, nombres, apellidos, correo, telefono, sexo, fecha_nacimiento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.telefono = telefono
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento


    def __str__(self):
        return f"{self.nombres} {self.apellidos}, {self.correo}, {self.telefono}, {self.sexo}, {self.fecha_nacimiento}"