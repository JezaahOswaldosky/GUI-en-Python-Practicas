import tkinter as tk 

def entro(event): 
    etiqueta.config(text="Entraste al area")

def salio(event): 
    etiqueta.config(text="Saliste del area")

# Configurar la ventana 
root = tk.Tk() 
root.title("Busca areas")
root.geometry("300x150")

frame = tk.Frame(root, width=300,hegiht=100, bg="lightgreen")
frame.pack()
frame.bind("<Enter>", entro)
frame.bind("<Enter>", salio)

etiqueta = tk.Label(root, text="Psa el mouse por el cuadro")
etiqueta.pack(pady=5)

root.mainloop()