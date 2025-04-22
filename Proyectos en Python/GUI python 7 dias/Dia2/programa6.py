import tkinter as tk 

# Configurar ventana 
ventana = tk.Tk() 
ventana.title("Programa que saluda")
ventana.geometry("320x200")

# Configurar un label 
label = tk.Label(ventana, text="Nombre: ")
label.pack() 

# Configurar el Textfield 
campoMensaje = tk.Entry(ventana, width=50)
campoMensaje.pack() 

def enviarMensaje(): 
    mensaje = campoMensaje.get()
    print("Tu mensaje", mensaje)
    labelMensaje = tk.Label(ventana, text="Nombre:"+mensaje)
    labelMensaje.pack() 

# Configurar boton 
boton = tk.Button(ventana, text="Enviar mensaje", command=enviarMensaje)
boton.pack() 

# Configurar el inicio de la ventana en un loop 
ventana.mainloop() 


