# Formulario con resumen del usuario 
import tkinter as tk 
from tkinter import messagebox 

def enviar_datos(): 
    nombre = entrada_nombre.get() 
    edad = entrada_edad.get() 
    correo = entrada_correo.get() 

    if not nombre or not edad or not correo: 
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos")
        return 
    
    mensaje = f"Nombre: {nombre}\n Edad: {edad} \nCorreo: {correo}"
    messagebox.showinfo("Datos ingresados", mensaje)

def salir(): 
    ventana.quit() 

# Inicializacion de la ventana 
ventana = tk.Tk() 
ventana.title("Formulario de usuario")
ventana.geometry("350x250")

# Menu 
menu_principal = tk.Menu(ventana)
ventana.config(menu = menu_principal)
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label = "Archivo", menu = menu_archivo)
menu_archivo.add_command(label="Salir", command=salir)

# Formulario 
tk.Label(ventana, text = "Nombre:").grid(row=0,column=0,padx = 10, pady=10, sticky="e")
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0,column=1)

tk.Label(ventana, text="Edad").grid(row=1,column=0,padx=10,pady=10,sticky="e")
entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1,column=1)

tk.Label(ventana, text="Correo").grid(row=2,column=0,padx=10,pady=10,sticky="e")
entrada_correo =  tk.Entry(ventana)
entrada_correo.grid(row=2,column=1)

# Boton 
boton = tk.Button(ventana, text="Enviar", command=enviar_datos)
boton.grid(row=3,column=0,columnspan=2,pady=20)

ventana.mainloop()