# Proyecto de un saludador, el usuario requiere introducir su nombre, y al presionar 
# un boton, este emitira un saludo cordial al usuario en un label. 
import tkinter as tk 

# Funcion para tomar valores o datos 
def saludar(): 
    nombre = nombreVar.get()
    saludoLabel.config(text=f"Hola, {nombre}")

ventana = tk.Tk()
ventana.title("Saludador de usuarios") 
ventana.geometry("300x200")

nombreLabel = tk.Label(ventana, text="Nombre", font=("Arial",14))
nombreLabel.pack() 

nombreVar = tk.Entry(ventana)
nombreVar.pack()

printButton = tk.Button(ventana, text="Saludo!", command=saludar)
printButton.pack()

saludoLabel = tk.Label(ventana, text="")
saludoLabel.pack()

ventana.mainloop()

