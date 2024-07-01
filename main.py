"""
    Daniel Alexander Duarte Ussa
    1016949009
    2877795
    CBA
"""
from logica import *


def main():
    # print(Fore.BLUE + Back.GREEN)
    while True:
        print("""
        Seleccione una acción:
        1. Limpiar todas las listas
        2. Agregar aprendices
        3. Buscar aprendiz por ficha
        4. Lista de fichas
        5. Resultado de aprendices por ficha
        6. Borrar aprendiz
        7. Editar aprendiz
        0. Salir
        """)
        try:
            user_input = int(input("¿Qué acción quiere llevar a cabo? "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if user_input == 1:  # Limpiar todas las listas
            global apprentice_list, apprentice_file_list
            apprentice_list.clear()
            apprentice_file_list.clear()
            print("Todas las listas han sido limpiadas.")
            back2_menu()

        elif user_input == 2:  # Agregar aprendices
            agregar_aprendices()

        elif user_input == 3:  # Buscar aprendiz por ficha
            buscar_aprendices_por_ficha()

        elif user_input == 4:
            lista_de_fichas()

        elif user_input == 5:
            resultado_de_aprendices()

        elif user_input == 6:
            eliminar_aprendiz()

        elif user_input == 7:
            editar_aprendiz()


        elif user_input == 0:  # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()