# Crear un label pata texto y un boton
# Utilizar el posicionamiento con .pack()
import tkinter as tk

def saludar():
    print("¡Hola!")

ventana = tk.Tk()

etiqueta = tk.Label(ventana, text="Haz click perro!!")
etiqueta.pack()

boton = tk.Button(ventana, text="Haz clic", command=saludar)
boton.pack()

ventana.mainloop()