import tkinter as tk 

# Configurar la ventana 
ventana = tk.Tk() 
ventana.title("Mi ventana")
ventana.geometry("320x200")

# Configurar una ventana 
label = tk.Label(ventana, text="Nombre: ")
label.pack() 

# Configurar un boton 
boton = tk.Button(ventana, text="Presioname!", command=lambda : print("Hola como estas? "))
boton.pack() 

# Ejecutar el ciclo de la ventana 
ventana.mainloop()
