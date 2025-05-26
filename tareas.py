# tareas.py
class Tareas:
    def __init__(self, nombre, descripcion, fecha_vencimiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.id = None  # Para asignar un ID único más adelante

    def mostrar_tarea(self):
        print(f"{self.id}. Tarea: {self.nombre}, Descripción: {self.descripcion}, Fecha de Vencimiento: {self.fecha_vencimiento}")

