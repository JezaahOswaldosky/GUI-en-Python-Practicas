##                          ScumTools.py 
## ScumTools.py es un programa que permite a los desarrolladores trabajar con scrum donde se 
## se muestra una interfaz visual para asignar tareas y mostrar cuales son las que se estan 
## trabajando en el momento.. 
######################################################################################################
import tkinter as tk
from tkinter import simpledialog, messagebox

class ScrumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tablero Scrum con Puntos")

        self.columns = {
            "To Do": [],
            "In Progress": [],
            "Done": []
        }

        self.total_points = 0  # Puntos acumulados
        self.frames = {}

        for i, col in enumerate(self.columns):
            frame = tk.Frame(root, bd=2, relief=tk.RIDGE, padx=10, pady=10)
            frame.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
            tk.Label(frame, text=col, font=("Arial", 14)).pack()
            self.frames[col] = frame

        add_button = tk.Button(root, text="Añadir tarea", command=self.add_task)
        add_button.grid(row=1, column=1)

        self.points_label = tk.Label(root, text="Puntos acumulados: 0", font=("Arial", 12, "bold"))
        self.points_label.grid(row=2, column=1, pady=10)

        self.update_columns()

    def add_task(self):
        desc = simpledialog.askstring("Nueva tarea", "Descripción de la tarea:")
        if not desc:
            return
        try:
            points = int(simpledialog.askstring("Puntos", "¿Cuántos puntos vale esta tarea?"))
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Debes ingresar un número entero.")
            return

        task = {"desc": desc, "points": points}
        self.columns["To Do"].append(task)
        self.update_columns()

    def move_task(self, col, task):
        next_col = {
            "To Do": "In Progress",
            "In Progress": "Done"
        }.get(col)

        if next_col:
            self.columns[col].remove(task)
            self.columns[next_col].append(task)

            if next_col == "Done":
                self.total_points += task["points"]
                self.points_label.config(text=f"Puntos acumulados: {self.total_points}")

            self.update_columns()

    def update_columns(self):
        for col, frame in self.frames.items():
            # Limpiar botones anteriores
            for widget in frame.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.destroy()

            for task in self.columns[col]:
                label_text = f"{task['desc']} ({task['points']} pts)"
                btn = tk.Button(frame, text=label_text, wraplength=100,
                                command=lambda c=col, t=task: self.move_task(c, t))
                btn.pack(pady=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrumApp(root)
    root.mainloop()