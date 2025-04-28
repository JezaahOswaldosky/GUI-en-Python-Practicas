import tkinter as tk 

## Definie funciones para el doble click y click derecho 
def doubleClick(event): 
    print("Doble click detectado")

def rightClick(event): 
    print("Click derecho detectado")

## Configurar las ventanas 
ventana = tk.Tk() 
ventana.title("Detector de Clicks ")

label = tk.Label(ventana, text="Haz doble click o click derecho", width=30, height=5, bg = "lightyellow")
label.pack() 

label.bind("<Double-1>", doubleClick)
label.bind("<Button-3>", rightClick)

## Inicializar la ventana 
ventana.mainloop()