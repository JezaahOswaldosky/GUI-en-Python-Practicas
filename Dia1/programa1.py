### Que es tkinter??  Es una biblioteca de Python que permite crear interfaces graficas de usuario GUI. 
# Una interfaz que se basa en la biblioteca Tk, que es una herramienta para el desarrollo de aplicaciones de escritorio 
# multiplataforma. 
# Tkinter proporciona widgets y herramientas necesarias para crear ventanas, botones, etiquetas, cajas de texto y 
# otros elementos que componenen una GUI. 
import tkinter as tk 

ventana = tk.Tk()
ventana.title("Mi primer GUI")
ventana.geometry("300x200")

ventana.mainloop()
