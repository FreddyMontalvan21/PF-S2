import tkinter as tk


def generar_ventana(titulo, ancho, alto):
    ventana = tk.Tk()
    ventana.title(titulo)
    
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    return ventana