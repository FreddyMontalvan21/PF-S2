from .ventana import nueva_ventana


def generar_ventana_principal():
    ventana_principal = nueva_ventana("MQ Distribuidora", 700, 400, False)
    ventana_principal.mainloop()