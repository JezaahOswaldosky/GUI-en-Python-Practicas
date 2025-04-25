import tkinter as tk 
 
 # Definimos la funcion del boton 
def botonClicked():
    texto = tk.Label(root, text = "No vuelvas a presionar!").grid(row=1,column=0)

# Inicializar la GUI 
root = tk.Tk() 

# Ejecutar el boton 
boton = tk.Button(root, text="No presiones el boton", bg="green", padx=100, pady=25, command=botonClicked()).grid(row=0,column=0)


# Ejecutar la GUI indefinidamente 
root.mainloop()