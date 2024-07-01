"""
    Daniel Alexander Duarte Ussa
    1016949009
    2877795
    CBA
"""

# Se declaran las listas globales fuera de las funciones
apprentice_list = []
apprentice_file_list = []

def agregar_aprendices():
    while True:
        try:
            # Diccionario para la creacion de aprendices
            add_apprentice = {
                "Documento del aprendiz": int(input("Documento del aprendiz: ")),
                "Nombre del aprendiz": input("Nombre del aprendiz: "),
                "Ficha del aprendiz": int(input("Ficha del aprendiz: ")),
                "Evaluación del aprendiz": input("Evaluación del aprendiz (A/D): ").upper()
            }

            # Control para el manejo de las evaluaciones
            if add_apprentice["Evaluación del aprendiz"] not in ["A", "D"]:
                print("Evaluación inválida. Intente nuevamente.")
                continue
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
            continue
        
        apprentice_file_list.append(add_apprentice["Ficha del aprendiz"])
        apprentice_list.append(add_apprentice)
        agregar_mas_aprendices = input("¿Desea agregar más aprendices? (si/no): ").lower()
        if agregar_mas_aprendices != "si":
            break

    back2_menu()


def buscar_aprendices_por_ficha():
    try:
        search_file = int(input("Digite la ficha que desea buscar: "))
    except ValueError:
        print("Error, digite un número válido.")
        back2_menu()
        return

    found_apprentices = [apprentice for apprentice in apprentice_list if apprentice["Ficha del aprendiz"] == search_file]

    if found_apprentices:
        print(f"Aprendices con la ficha {search_file}:")
        for apprentice in found_apprentices:
            print(apprentice)
    else:
        print(f"No se encontró ningún aprendiz con la ficha {search_file}.")

    back2_menu()


def lista_de_fichas():
    unique_files = set([apprentice["Ficha del aprendiz"] for apprentice in apprentice_list])

    for file_number in unique_files:
        print(f"Aprendices en la ficha {file_number}:")
        found_apprentices = [apprentice for apprentice in apprentice_list if apprentice["Ficha del aprendiz"] == file_number]
        for apprentice in found_apprentices:
            print(f"Documento: {apprentice['Documento del aprendiz']}, Nombre: {apprentice['Nombre del aprendiz']}, Evaluación: {apprentice['Evaluación del aprendiz']}")

    back2_menu()


def resultado_de_aprendices():

    #Esta lista va recorrer ficha por ficha que se hayan registrado
    unique_files = set([apprentice["Ficha del aprendiz"] for apprentice in apprentice_list])


    # Iremos recorriendo cada ficha
    for file_number in unique_files:

        # Imprimimos al principio de cada iteracion la ficha a la que haremos referencia
        print(f"Ficha {file_number}:")

        # Creamos la lista de los aprendices aprobados que se encuentren en la lista repectiva
        approved_apprentices = [apprentice for apprentice in apprentice_list if apprentice["Ficha del aprendiz"] == file_number and apprentice['Evaluación del aprendiz'] == 'A']
        
        # Creamos la condicion sin atributos que lleguen a 
        if approved_apprentices:
            print('Aprendices Aprobados:')
            for apprentice in approved_apprentices:
                print(f"Documento: {apprentice['Documento del aprendiz']}, Nombre: {apprentice['Nombre del aprendiz']}")
        else:
            print("No hay aprendices aprobados en esta ficha.")
        
        disapproved_apprentices = [apprentice for apprentice in apprentice_list if apprentice["Ficha del aprendiz"] == file_number and apprentice['Evaluación del aprendiz'] == 'D']
        if disapproved_apprentices:
            print('Aprendices Desaprobados:')
            for apprentice in disapproved_apprentices:
                print(f"Documento: {apprentice['Documento del aprendiz']}, Nombre: {apprentice['Nombre del aprendiz']}")
        else:
            print("No hay aprendices desaprobados en esta ficha.")
        
        print()  # Linea en blanco entre cada ficha
        
    back2_menu()



def eliminar_aprendiz():
    try:
        documento = int(input("Ingrese el documento del aprendiz que desea eliminar: "))
    except ValueError:
        print("Error, digite un número válido.")
        back2_menu()
        return

    apprentice_to_remove = next((apprentice for apprentice in apprentice_list if apprentice["Documento del aprendiz"] == documento), None)

    if apprentice_to_remove:
        apprentice_list.remove(apprentice_to_remove)
        apprentice_file_list.remove(apprentice_to_remove["Ficha del aprendiz"])
        print(f"Aprendiz con documento {documento} ha sido eliminado.")
    else:
        print(f"No se encontró ningún aprendiz con el documento {documento}.")

    back2_menu()


def editar_aprendiz():
    try:
        if apprentice_list:
            for apprentice in apprentice_list:
                print(apprentice)
        documento = int(input("Ingrese el documento del aprendiz que desea editar: "))
    except ValueError:
        print("Error, digite un número válido.")
        back2_menu()
        return

    apprentice_to_edit = next((apprentice for apprentice in apprentice_list if apprentice["Documento del aprendiz"] == documento), None)

    if apprentice_to_edit:
        try:
            nuevo_nombre = input(f"Nombre actual ({apprentice_to_edit['Nombre del aprendiz']}): ")
            nueva_ficha = int(input(f"Ficha actual ({apprentice_to_edit['Ficha del aprendiz']}): "))
            nueva_evaluacion = input(f"Evaluación actual ({apprentice_to_edit['Evaluación del aprendiz']}) (A/D): ").upper()
            if nueva_evaluacion not in ["A", "D"]:
                print("Evaluación inválida. No se realizaron cambios.")
                back2_menu()
                return
        except ValueError:
            print("Entrada inválida. No se realizaron cambios.")
            back2_menu()
            return

        apprentice_to_edit["Nombre del aprendiz"] = nuevo_nombre if nuevo_nombre else apprentice_to_edit["Nombre del aprendiz"]
        apprentice_to_edit["Ficha del aprendiz"] = nueva_ficha
        apprentice_to_edit["Evaluación del aprendiz"] = nueva_evaluacion

        print(f"Aprendiz con documento {documento} ha sido actualizado.")
    else:
        print(f"No se encontró ningún aprendiz con el documento {documento}.")

    back2_menu()


def back2_menu():
    while True:
        seguir = input("¿Volver al menú? (si/no): ").lower()
        if seguir == "si":
            return
        elif seguir == "no":
            print("******")
            print("Que te vaya bien tocando pasto")
            print("******")
            exit()
        else:
            print("Entrada inválida. Por favor, ingrese 'si' o 'no'.")