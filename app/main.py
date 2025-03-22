import procesos as p

def main():
    ejecutar = True

    while ejecutar:
        p.presentar_menu()

        opcion = input('Ingresa una opción: ')

        if opcion not in ('1', '2', '3', '4', '5'):
            print('\n Adioooss!!\n')
            ejecutar = False


main()