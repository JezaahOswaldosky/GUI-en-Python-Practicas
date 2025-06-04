##                  programa10_topLevel.py 
##
## programa10_topLevel.pyt es un programa que permite multiples 
## ventanas abiertas para trabajar... 
#################################################################
import tkinter as tk 

def abrirVentana(): 
    global ventana2
    if ventana2 is None or not ventana2.winfo_exists(): 
        ventana2 = tk.Toplevel(ventana)
        ventana2.title("Solo una ventana")
        tk.Label(ventana2, text="Esta ventana no se duplica").pack() 

    else: 
        ventana2.lift()

# Configurar ventana principal 
ventana = tk.Tk() 
ventana.title("Ventana principal ")
ventana.geometry("300x200")

ventana2 = None

tk.Button(ventana, text="Abrir unica ventana secundaria", command=abrirVentana).pack(pady=20)

## Ejecutar la ventana principal 
ventana.mainloop()