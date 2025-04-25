import tkinter as tk 

# Funcion para saludar 
def saludar(): 
    print("Hola, Chad ")

# Creamos una ventana 
root = tk.Tk() 
root.title("Ejemplo de un boton")
root.geometry("300x150")

# Crear boton y asociarlo a la funcion 
boton = tk.Button(root, text="Haz click", command=saludar)
boton.pack(pady=20)

# Inicializar bucle para la ventana
root.mainloop() 