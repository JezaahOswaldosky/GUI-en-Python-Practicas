###################################################################################################
##                          programa3_sesion.py 
## programa3_sesion.py es un programa que permite al usuario introducir los datos de usuario y 
## contrasena para ingresar a un programa o software. Pero este se comparar con una base de datos 
## en formato .txt de usuarios y contrasenas
###################################################################################################
import tkinter as tk 
from tkinter import messagebox

## Creamos la funcion para compar las credenciales 
def checkID(): 
    pass

## Crear ventana 
ventana = tk.Tk() 
ventana.title("Inicio de sesion")
ventana.geometry("300x180")
ventana.resizable(False, False)

## Configurar las etiquetas y textfields necesarias como usuario y contrasena 
userLabel = tk.Label(ventana, text="Usuario:") 
userLabel.pack(pady=(20,5))

userField = tk.Entry()
userField.pack()

pswLabel = tk.Label(ventana, text="Contrasena: ")
pswLabel.pack(pady=(10,5))

pswField = tk.Entry(ventana, show="*") 
pswField.pack() 

## Configurar boton para ingresar o iniciar sesion 
introButton = tk.Button(ventana, text="Iniciar sesion", command=checkID)
introButton.pack(pady=15)

# Ejecutar la ventana 
ventana.mainloop()
