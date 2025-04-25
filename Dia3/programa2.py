import tkinter as tk 
def mostrarTexto(): 
    texto = entrada.get() 
    print(f"El texto ingresado es: {texto}")
    etiqueta.config(text=f"Hola, {texto}")

def cambiarTexto():
    entrada.delete(0,tk.END)
    entrada.insert(0,"Texto cambiado")

def borraTexto(): 
    texto = ""
    print(f"{texto}")
    etiqueta.config(text=f"{texto}")
    entrada.delete(0,tk.END)


# Crear ventana 
root = tk.Tk()
root.title("Leer y Modificar Entry")
root.geometry("300x200")

# Entry 
entrada = tk.Entry(root, width=30)
entrada.pack(pady=10)

# Etiqueta para mostrar el resultado 
etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=5)

# Boton para leer el contenido 
botonLeer = tk.Button(root, text="Leer texto", command=mostrarTexto)
botonLeer.pack(pady=5)

# Boton para cambiar el contenido de Entry 
botonModificar = tk.Button(root, text="Modificar texto", command=cambiarTexto)
botonModificar.pack(pady=5);

# Boton para borrar el contenido del Entry 
botonBorrar = tk.Button(root, text="Borrar texto", command=borraTexto)
botonBorrar.pack(pady=5)

root.mainloop()