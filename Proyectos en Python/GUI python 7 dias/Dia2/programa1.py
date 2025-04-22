# Programa o arquitectura basica para el manejo de una ventana con la biblioteca Tkinter. 
import tkinter as tk

## Crear la ventana principal 
ventana = tk.Tk() 
ventana.title("Mi primera ventana")
ventana.geometry("300x200")

# Etiqueta de bienvenida 
etiqueta = tk.Label(ventana, text="Hola mundo!!", font=("Arial", 14))
etiqueta.pack(pady=20)

# Boton para cerra la ventana 
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack()

# Iniciar el bucle de la app 
ventana.mainloop()
