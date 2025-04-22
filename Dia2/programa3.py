# programa que hace la utilizacion de label, button, .pack y .grid 
import tkinter as tk 

# Funcion que se llama al hacer clic en el boton 
def saludar():
    nombre = entrada.get() 
    etiquetaSaludo.config(text=f"Hola, {nombre}")

# Crear una ventana principal 
ventana = tk.Tk() 
ventana.title("Saludador")
ventana.geometry("300x200")

# Etiqueta inicial 
etiqueta = tk.Label(ventana, text = "Escribe tu nombre")
etiqueta.pack(pady=10)

# Campo de entrada 
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Boton para llamar la funcion saludar 
botonSaludar = tk.Button(ventana, text="Saludar", command = saludar)
botonSaludar.pack(pady=10)

# Etiqueta para mostrar el saludo 
etiquetaSaludo = tk.Label(ventana, text="")
etiquetaSaludo.pack(pady=10)

#Crear el loop de la vetana 
ventana.mainloop()