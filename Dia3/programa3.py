import tkinter as tk 
def actualizarTexto(event):
    texto = entrada.get() 
    etiqueta.config(text=f"Escribiento: {texto}")

# Configurar la ventana 
root = tk.Tk() 
root.title("Texto dinamico")
root.geometry("300x200")

# entrada de datos 
entrada = tk.Entry(root, width=30)
entrada.pack(pady=5)

# Evento para que se actualice mientras se escribre 
entrada.bind("<KeyRelease>", actualizarTexto)

etiqueta = tk.Label(root, text="empieza a escribir...")
etiqueta.pack(pady=10)

# Inicializar la ventana 
root.mainloop()