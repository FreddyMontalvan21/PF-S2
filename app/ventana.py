import tkinter as tk
from tkinter import Menu, Frame, Label, Entry, Button, filedialog
from producto import Producto

def crear_ventana(master, client, db, collection):
    master.title("CRUD de Productos")
    
    menu = Menu(master)
    master.config(menu=menu)

    crear_menu(master, client, db, collection)

def crear_menu(master, client, db, collection):
    menu_crear = Menu(master)
    menu_crear.add_command(label="Crear", command=lambda: mostrar_panel(master, PanelCrear, client, db, collection))
    menu_crear.add_command(label="Leer", command=lambda: mostrar_panel(master, PanelLeer, client, db, collection))
    menu_crear.add_command(label="Actualizar", command=lambda: mostrar_panel(master, PanelActualizar, client, db, collection))
    menu_crear.add_command(label="Eliminar", command=lambda: mostrar_panel(master, PanelEliminar, client, db, collection))
    master.menu.add_cascade(label="Opciones", menu=menu_crear)

def mostrar_panel(master, panel_class, client, db, collection):
    for widget in master.winfo_children():
        widget.destroy()
    panel = panel_class(master, client, db, collection)
    panel.pack()

class PanelCrear(Frame):
    def __init__(self, master, client, db, collection):
        super().__init__(master)
        self.client = client
        self.db = db
        self.collection = collection

        self.label_nombre = Label(self, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = Entry(self)
        self.entry_nombre.pack()

        self.boton_guardar = Button(self, text="Guardar Producto", command=self.guardar_producto)
        self.boton_guardar.pack()

    def guardar_producto(self):
        nombre = self.entry_nombre.get()
        nuevo_producto = Producto(codigo=1, nombre=nombre, descripcion="Descripción", 
                                  url_imagen="", stock=10, stock_min=1, stock_max=100, precio=20.0)
        insertar_producto(self.collection, nuevo_producto)
        print("Producto agregado:", nuevo_producto)

class PanelLeer(Frame):
    def __init__(self, master, client, db, collection):
        super().__init__(master)
        self.client = client
        self.db = db
        self.collection = collection
        # Implementar lógica para leer productos

class PanelActualizar(Frame):
    def __init__(self, master, client, db, collection):
        super().__init__(master)
        self.client = client
        self.db = db
        self.collection = collection
        # Implementar lógica para actualizar productos

class PanelEliminar(Frame):
    def __init__(self, master, client, db, collection):
        super().__init__(master)
        self.client = client
        self.db = db
        self.collection = collection
        # Implementar lógica para eliminar productos
