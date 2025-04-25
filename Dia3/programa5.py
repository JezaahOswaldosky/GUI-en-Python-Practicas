import tkinter as tk 
def clickIzq(event): 
    etiqueta.config(text=f"Click izquierdo en x={event.x}, y={event.y}")

# Crear la ventana 
root = tk.Tk() 
root.title("Evento con el mouse")
root.geometry("300x150")

etiqueta = tk.Label(root, text="Haz click en la etiqueta")
etiqueta.pack(pady=20)
etiqueta.bind("<Button-1>", clickIzq)

root.mainloop()
