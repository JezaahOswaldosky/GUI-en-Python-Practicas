##                              programa1_sesion.py 
##programa1_sesion.py es un programa que pide una cuenta de usuarios y contrasena para ingresar a 
## otra ventana. 

import tkinter as tk 
from tkinter import messagebox 

# Funcion que verifica las credenciales del usuario 
def ID_Chek(): 
    usuario = userEntry.get() 
    psw = pswEntry.get() 

    # Ejemplo simple de validacion 
    if usuario == "admin" and psw == "3541": 
        messagebox.showinfo("Inicio de sesion", "Acceso concedido!!")
    else: 
        messagebox.showerror("Error", "Usuario o contrasena incorrectos!!")
    
# Crear la ventana principal 
ventana = tk.Tk()
ventana.title("Inicio de sesion")
ventana.geometry("300x180")
ventana.resizable(False,False)

# Etiquetas y campos de entrada 
userLabel = tk.Label(ventana, text="Usuario: ")
userLabel.pack(pady=(20,5))

userEntry = tk.Entry(ventana)
userEntry.pack()

pswLabel = tk.Label(ventana, text="Contrasena: ")
pswLabel.pack(pady=(10,5))

pswEntry = tk.Entry(ventana, show="*") # Remplaza los caracteres por el *
pswEntry.pack() 

# Boton de incio de sesion
inicioButton = tk.Button(ventana, text="Iniciar sesion", command=(ID_Chek))
inicioButton.pack(pady=15) 

# Ejecutar la ventana 
ventana.mainloop()