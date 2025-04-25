import tkinter as tk 

# Configurar la ventana GUI 
root = tk.Tk() 
root.title("Formulario")

entrada = tk.Entry(root)
entrada.grid(row=0, column=0)

# Funcion del boton 
def botonClicked():
    texto = tk.Label(root, text=f"Se almaceno!! {entrada.get()}").grid(row=1, column=0)

boton1 = tk.Button(root, text="Capturar", bg="green", padx=100, pady=25, command=botonClicked).grid(row=2, column=0)

# Ejecutar la ventana indefinidamente 
root.mainloop()