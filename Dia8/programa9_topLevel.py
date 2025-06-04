##                          programa9_topLevel.py 
## programa9_topLevel.py es un programa que pasa datos de 
## ventana principal a la ventana secundaria. 
############################################################
import tkinter as tk 

def abrirVentana(): 
    def enviar(): 
        valor = entry.get() 
        label.config(text=f"Texto ingresado: {valor}")
        top.destroy() 
    
    top = tk.Toplevel(ventana)
    top.title("Introduce texto")
    entry = tk.Entry(top)
    entry.pack(padx=10, pady=10)
    tk.Button(top, text="Enviar", command=enviar).pack()

# Configurar ventanan principal 
ventana = tk.Tk() 
ventana.title("Ventana principal")
ventana.geometry("300x200")

label = tk.Label(ventana, text ="Texto ingresado.")
label.pack(pady=10)

tk.Button(ventana, text="Abrir entrada de texto", command=abrirVentana).pack()

# Ejecutar la ventana principal 
ventana.mainloop()