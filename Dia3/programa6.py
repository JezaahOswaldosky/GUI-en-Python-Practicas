import tkinter as tk 

def mover(event):
    etiqueta.config(text=f"Mouse en ({event.x}, {event.y})")

root = tk.Tk()
root.geometry("300x150")

frame = tk.Frame(root, width=300, height=100, bg="lightblue")
frame.pack()
frame.bind("<Motion>", mover)

etiqueta = tk.Label(root, text="Mueve el mouse dentro del área azul")
etiqueta.pack(pady=5)

root.mainloop()