##                          programa2_messbox.py
##
## programa2_messbox.py es un programa que muestra la utilidad y uso de los 
## messagebox en tkinte ry python. 
## Existen funciones como: showinfo, showwarning, showerror, askokcancel
## askquestion, askyesno, askretrycancel
##############################################################################
import tkinter as tk 
from tkinter import messagebox

def mostrarMensaje(): 
    messagebox.showinfo("Informacion", "Esto es un mensaje informativo")
    respuesta = messagebox.askyesno("Pregunta","Deseas continuar?")
    if respuesta: 
        messagebox.showinfo("Respuesta", "Elegiste continuar")
    else: 
        messagebox.showwarning("Respuesta", "Elegiste cancelar")
    
ventana = tk.Tk() 
ventana.title("Ejemplo de messagebox")

boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrarMensaje)
boton.pack(pady=20)

ventana.mainloop()