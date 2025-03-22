class Producto:
    def __init__(self, codigo, nombre, descripcion, url_imagen, stock, stock_min, stock_max, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.url_imagen = url_imagen
        self.stock = stock
        self.stock_min = stock_min
        self.stock_max = stock_max
        self.precio = precio

    def __str__(self):
        return f"Producto(codigo={self.codigo}, nombre={self.nombre}, stock={self.stock})"
