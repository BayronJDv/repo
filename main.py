
agenda = {}

while True:
    print("\nAgenda de contactps")
    print("1. buscar contacto")
    print("2. añadir contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    
    opcion = int(input("Elija una opción: "))

    match opcion:
        case 1:
            if len(agenda) == 0:
                print("Aun no se han añadido contactos ")
            else:
                nombre = input("Introduzca el nombre del contacto: ")
                if nombre in agenda:
                    print(f"Contacto: {nombre}")
                    print(f"Teléfono: {agenda[nombre]}")
                else:
                    print("El contacto no se encuentra en la agenda.")
                
        case 2:
            nombre = input("Introduzca el nombre del contacto: ")
            telefono = input("Introduzca el teléfono del contacto: ")
            agenda[nombre] = telefono
            print("Contacto añadido correctamente.")
            
        case 3:
            nombre = input("Introduzca el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado correctamente.")
            else:
                print("El contacto no se encuentra en la agenda")
        case 4:
            break
        case _:
            print("Opción inválida. Intente de nuevo.")


