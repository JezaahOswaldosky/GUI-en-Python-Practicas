import tkinter as tk 

def teclaPresionada(event): 
    etiqueta.config(text=f"Presionaste: {event.char}")


# Configuramos la ventana 
root = tk.Tk() 
root.title("Keylogger sencillo")
root.geometry("300x150")

# Configurar la variable de entrada 
entrada = tk.Entry(root)
entrada.pack(pady=10)
entrada.bind("<Key>", teclaPresionada)

etiqueta = tk.Label(root, text="Presiona una tecla... ")
etiqueta.pack(pady=10)

root.mainloop()
