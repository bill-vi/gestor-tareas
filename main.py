# main.py
from tareas import Tareas
from usuario import Usuario

def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Crear tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def crear_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento (AAAA-MM-DD): ")
    tarea = Tareas(nombre, descripcion, fecha_vencimiento)
    return tarea

def main():
    print("Bienvenido al gestor de tareas")

    nombre_usuario = input("Ingrese su nombre: ")
    email_usuario = input("Ingrese su correo electrónico: ")

    usuario = Usuario(nombre_usuario, email_usuario)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = crear_tarea()
            usuario.agregar_tarea(tarea)
            print("Tarea creada exitosamente.")
        elif opcion == "2":
            usuario.mostrar_tareas()
        elif opcion == "3":
            usuario.mostrar_tareas()
            tarea_id = int(input("Ingrese el número de la tarea a eliminar: "))
            usuario.eliminar_tarea(tarea_id)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

