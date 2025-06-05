# Lista inicial de estudiantes
nombres_estudiantes = ["Juan", "Ana", "Luis", "María", "Pedro", "Sofía"]

# Diccionario de contactos
contactos = {
    "Juan": "juan@example.com",
    "Ana": "ana@example.com",
    "Carlos": "carlos.perez@example.com"
}

while True:
    print("\n===== MENÚ INTERACTIVO =====")
    
    # Mostrar la lista de estudiantes
    print("\nLista de estudiantes:")
    for nombre in nombres_estudiantes:
        print("- " + nombre)

    # Mostrar la lista de contactos
    print("\nInformación de contacto:")
    for nombre, correo in contactos.items():
        print(f"{nombre}: {correo}")

    # Opciones del menú
    print("\nSeleccione una opción:")
    print("1. Agregar un estudiante a la lista")
    print("2. Actualizar o agregar un contacto")
    print("3. Salir")

    opcion = input("Opción (1, 2 o 3): ")

    if opcion == "1":
        nuevo_nombre = input("Ingrese el nombre del nuevo estudiante: ")
        nombres_estudiantes.append(nuevo_nombre)
        print("\nEstudiante agregado. Lista actualizada:")
        for nombre in nombres_estudiantes:
            print("- " + nombre)

    elif opcion == "2":
        nombre_contacto = input("Ingrese el nombre del contacto: ")
        nuevo_correo = input(f"Ingrese el correo de {nombre_contacto}: ")
        contactos[nombre_contacto] = nuevo_correo
        print("\nContacto actualizado. Lista de contactos:")
        for nombre, correo in contactos.items():
            print(f"{nombre}: {correo}")

    elif opcion == "3":
        print("\nSaliendo del programa. ¡Hasta luego!")
        break

    else:
        print("\nOpción no válida. Intente de nuevo.")

