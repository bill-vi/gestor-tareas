from tareas import Tareas

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.tareas = []

    def agregar_tarea(self, tarea):
        tarea.id = len(self.tareas) + 1
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No tienes tareas pendientes.")
        else:
            print(f"Tareas de {self.nombre}:")
            for tarea in self.tareas:
                tarea.mostrar_tarea()

    def eliminar_tarea(self, tarea_id):
        if tarea_id <= len(self.tareas) and tarea_id > 0:
            tarea_a_eliminar = self.tareas.pop(tarea_id - 1)
            print(f"Tarea '{tarea_a_eliminar.nombre}' eliminada exitosamente.")
        else:
            print("Tarea no encontrada.")

