##                      programa4_frame.py 
## programa4_frame.py es un programa que implementa el uso de frames para 
## organizar widgets en GUI por la biblioteca tkinter 
########################################################################
import tkinter as tk 

# Creamos la ventana principal 
ventana = tk.Tk() 
ventana.title("Ejemplo con Frame")
ventana.geometry("300x200")

## Creamos un frame para la parte superior 
topFrame = tk.Frame(ventana, bg = "lightblue", height = 100)
topFrame.pack(fill="x")

# Crear un frame para la parte inferior 
bottomFrame = tk.Frame(ventana, bg = "lightgreen")
bottomFrame.pack(fill="both", expand=True)

# Anadir una etiqueta al frame superior 
label1 = tk.Label(ventana, text="Encabezado", bg="lightgrey")
label1.pack(pady= 10)

# Anadir una etiqueta al frame inferior 
label2 = tk.Label(ventana, text =  "Contenido principal", bg="white")
label2.pack(pady=10)

# Anadir boton 
boton = tk.Button(bottomFrame, text = "Presiona")
boton.pack() 

# ejecutar la ventana 
ventana.mainloop()
