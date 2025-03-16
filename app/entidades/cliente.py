class Cliente:
    def __init__(self, id_cliente, cedula, fecha_registro):
        self.id_cliente = id_cliente
        self.cedula = cedula
        self.fecha_registro = fecha_registro

    
    def __str__(self):
        return f"{self.id_cliente}, {self.cedula}, {self.fecha_registro}"