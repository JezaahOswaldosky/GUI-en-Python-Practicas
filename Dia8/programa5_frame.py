##                  programa5_frame.py 
##  programa5_frame.py es un programa que utiliza frames para 
## organizar widgets.. 
################################################################
import tkinter as tk 
# Inicializar ventana 
ventana = tk.Tk() 
ventana.title("Utilizacion de Frames")
ventana.geometry("300x280")

# Configurar Frame superior 
frameSup = tk.Frame(ventana, bg="lightgrey",height=100)
frameSup.pack(fill="x")

# Configurar el freme inferior 
bottomFrame = tk.Frame(ventana, bg ="lightblue", height=100)
bottomFrame.pack(fill="both", expand=True)

# Anadir etiquetas al frame superior 
label1 = tk.Label(ventana, text="Encabezado", bg ="lightgreen")
label1.pack(pady = 10)

# Anadir una etiqueta al frame inferior 
label2 = tk.Label(ventana, text="Contenido principal", bg ="lightblue")
label2.pack(pady=10)

# Anadir boton 
btn = tk.Button(bottomFrame, text="Presiona")
btn.pack() 

# Inicializar la GUI 
ventana.mainloop()