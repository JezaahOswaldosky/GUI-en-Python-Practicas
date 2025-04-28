import tkinter as tk 
from tkinter import messagebox

# Funcion que verifica las credenciales del usuario 
def checkID(): 
    usuario = userEntry.get() 
    password = pswEntry.get() 

    # Validacion simpletas 
    if usuario == "admin" and password == "panza123": 
        messagebox.showinfo("Inicio de sesion", "Ingresaste exitosamente")
    else: 
        messagebox.showerror("Error", "Usuario o contrasena incorrectos")

# Creamos la ventana 
ventana = tk.Tk() 
ventana.title("Inicio de sesion")
ventana.geometry("300x180")
ventana.resizable(False, False)

# Etiquetas y campos de entrada 
userLabel = tk.Label(ventana, text="Usuario: ")
userLabel.pack(pady=(20,5))

userEntry = tk.Entry(ventana)
userEntry.pack()

pswLabel = tk.Label(ventana, text="Contrasena: ")
pswLabel.pack(pady=(10,5))

pswEntry = tk.Entry(ventana, show="*")
pswEntry.pack()

# Boton de inicio de sesion 
inicioButton = tk.Button(ventana, text="Iniciar sesion", command=checkID)
inicioButton.pack(pady=15)

# Ejecutar la ventana 
ventana.mainloop()
