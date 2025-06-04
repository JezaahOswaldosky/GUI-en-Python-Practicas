##                      programa8_topLeve.py 
## programa8_topLevel.py es un programa que utiliza lo basico 
## un topLevel para crear ventanas secundarias. Ideal para 
## crear ventanas o mensajes de texto personalizados. 
###############################################################
import tkinter as tk 

def abrirVentana(): 
    ventana2 = tk.Toplevel(ventana)
    ventana2.title("Ventana secundaria")
    ventana2.geometry("200x100")
    tk.Label(ventana2, text="Hola desde la ventana secundaria!!").pack()

# Configurar ventana 
ventana = tk.Tk() 
ventana.title("Ventana principal")
ventana.geometry("300x200")

# Configurar un boton para abrir la ventana secundaria 
btn = tk.Button(ventana, text="Abrir ventana secundaria", command=abrirVentana)
btn.pack(pady=20)

ventana.mainloop()