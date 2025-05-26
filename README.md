# Gestor de tareas

Este es un proyecto desarrollado como parte de la actividad del curso de Mantenimiento de Software. El objetivo es simular una colaboración entre múltiples integrantes utilizando Git y GitHub para el control de versiones de un sistema funcional.

---

## Objetivo

Desarrollar un sistema básico de gestión de tareas que permita al usuario:
- Crear tareas
- Ver tareas registradas
- Eliminar tareas
- Simular inicio y cierre de sesión

---

## Tecnologías utilizadas

- Lenguaje: Python 3
- Control de versiones: Git
- Plataforma colaborativa: GitHub

---

## Funcionalidades

1. Solicita los datos del usuario al iniciar.
2. Permite crear tareas con nombre, descripción y fecha de vencimiento.
3. Muestra la lista de tareas registradas.
4. Elimina una tarea según su ID.
5. Permite salir y cerrar sesión en el sistema.

---

## Simulación de trabajo colaborativo

Este proyecto simula una colaboración entre tres participantes:

| Participante | Aporte realizado     |
|--------------|----------------------|
| William      | Archivo `main.py`    |
| Juan         | Archivo `tareas.py`  |
| Laura        | Archivo `usuario.py` |

Cada integrante creó su rama y subió su aporte mediante `git push` a GitHub.

---

## Historias de Usuario

- HU-001: Como usuario, quiero crear tareas con nombre, descripción y fecha.
- HU-002: Como usuario, quiero ver la lista de mis tareas.
- HU-003: Como usuario, quiero eliminar tareas específicas.
- HU-004: Como usuario, quiero ingresar mi nombre y correo al comenzar.
- HU-005: Como usuario, quiero cerrar sesión al terminar el uso del sistema.

---

## Instalación y uso

```bash
git clone https://github.com/bill-vi/gestor-tareas.git
cd gestor-tareas
python3 main.py
