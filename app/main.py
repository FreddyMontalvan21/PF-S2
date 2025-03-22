import tkinter as tk
from mongo import conectar_db, obtener_productos, insertar_producto, actualizar_producto, eliminar_producto
from ventana import crear_ventana
from producto import Producto

def main():
    # Conectar a la base de datos
    client, db, collection = conectar_db()
    
    # Crear la ventana principal
    root = tk.Tk()
    crear_ventana(root, client, db, collection)
    
    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
