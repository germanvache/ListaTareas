'''LISTA DE TAREAS 
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes. 
Implementa métodos para agregar una tarea, marcar una tarea como 
completada y mostrar todas las tareas
'''
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def marcar_completada(self, indice):
       if 0<= indice < len(self.tareas):
           self.tareas[indice]["completada"] = True

    def mostrar_tareas(self):
        for indice, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{indice + 1}. {tarea['tarea']} - {estado}")

# Ejemplo de uso
lista_tareas = ListaTareas()
lista_tareas.agregar_tarea("Hacer la compra")
lista_tareas.agregar_tarea("Estudiar programacion")
lista_tareas.marcar_completada(1)
lista_tareas.mostrar_tareas()

