import tkinter as tk 

# Funcion para mostrar una tecla 
def keyPressed(event): 
    print(f"Tecla presionada: {event.char}")

root = tk.Tk() 
root.title("Detectar teclas")

entry = tk.Entry(root)
entry.pack() 
entry.bind("<Key>", keyPressed)

# Inicializar la ventana 
root.mainloop() 
