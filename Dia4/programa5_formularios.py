import tkinter as tk 
# Inicializar la gUI 
root = tk.Tk() 

# Inicializar el textfield 
entrada = tk.Entry(root)
entrada.grid(row=0, column= 0)

def botonCliked():
    texto = tk.Label(root, text="Se envio correctamente").grid(row=1,column=0)

# Configurar el boton 
boton = tk.Button(root,text="Enviar", bg="green", padx=100, pady=25, command=botonCliked).grid(row=2,column=0)

# Inicializar la GUI de forma indefinida
root.mainloop()