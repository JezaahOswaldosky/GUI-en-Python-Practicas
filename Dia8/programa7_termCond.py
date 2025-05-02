##                  programa7_termCond.py 
## programa7_termCond.py es un programa de terminos y 
## condiciones para un prograa en especifico para imprimir 
## un documento de casorio digital. 
## Solo constara de un Label con las condiciones del casorio
## y procedimientos para anular el casamiento y que podria 
## ocurrir bajo leyes federales y estatales que pueden ser 
## modificador segun el estado. 
################################################################
import tkinter as tk 
import ctypes

# Configurar la ventana de terminos y condiciones 
ventana = tk.Tk() 
ventana.title("Terminos y condiciones")
ventana.geometry("400x350")
ventana.resizable(False, False) 

# Ingresamos icono al programa 
icono = tk.PhotoImage(file="icono.png")
ventana.iconphoto(False,icono)


# Inicializar la ventana GUI 
ventana.mainloop()