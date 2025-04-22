# Prograa que reorganiza frames con pack() y grid() 
import tkinter as tk 

def saludar(): 
    nombre = entryNombre.get() 
    apellido = entryApellido.get() 
    saludo.config(text=f"Hola, {nombre} {apellido}")

# ventana principal 
ventana = tk.Tk() 
ventana.title("Ejemplo de pack() y grid()")
ventana.geometry("320x200")

# frame superior usando pack() para ordenar las cosas 
frameSup = tk.Frame(ventana)
frameSup.pack(pady=10)

titulo = tk.Label(frameSup, text="Formulariod e saludo", font=("Arial", 14))
titulo.pack()

#Frame inferior 
frameInf = tk.Frame(ventana)
frameInf.pack(pady = 10)

# Etiqueta y campo del nombre 
tk.Label(frameInf, text = "Nombre: ").grid(row=0,column=0, padx=5,pady=5)
entryNombre = tk.Entry(frameInf)
entryNombre.grid(row=0,column=1, padx=5, pady=5)

# Etiqueta y campo de apellido 
tk.Label(frameInf, text="Apellido:").grid(row=1,column=0,padx=5,pady=5)
entryApellido = tk.Entry(frameInf)
entryApellido.grid(row=1,column=1, padx=5,pady=5)

# Boton y etiqueta de saludo 
botonSaludo = tk.Button(frameInf, text="Saludar", command=saludar)
botonSaludo.grid(row=2,column=0, columnspan=2, pady=10)

saludo = tk.Label(frameInf, text="", fg="blue")
saludo.grid(row=3, column=0, columnspan=2)


#buble principal 
ventana.mainloop()