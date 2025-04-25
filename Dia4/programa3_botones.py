import tkinter as tk 

# Inicializar la ventana 
root = tk.Tk() 
root.title("Programa con botones!!")

# Definir accion del boton 
def botonClicked():
    texto = tk.Label(root, text="No vuelvas a presionar el boton!!").grid()


# Iniciar o configurar la GUI 
boton1 = tk.Button(root, text="No presiones el boton!!", bg="red", padx=100, pady=25, command=botonClicked).grid(row=1, column=2)

# Inicializar la ventanan indefinidamente 
root.mainloop()