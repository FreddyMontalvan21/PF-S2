from vistas.vista_general import generar_ventana


def main():
    ventana_principal = generar_ventana("MQ Distribuidora", 700, 400)
    ventana_principal.mainloop()


main()