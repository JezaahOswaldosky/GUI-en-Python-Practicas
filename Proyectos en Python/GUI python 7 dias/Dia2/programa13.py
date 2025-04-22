import tkinter as tk 
from tkinter import ttk 

# Crear ventana principal 
root = tk.Tk() 

# Personalizacion basica 
root.title("Mi aplicacion Pro")
root.geometry("400x300")
root.resizable(False,False) #Evita redimencionar 

# Cambiar el iconode la ventana
try: 
    root.iconbitmap("iconoImg.ico")
except: 
    print("No se encontro el icono, asegurate de tener un archivo .ico en la carprta")

# Estilo con ttk 
style = ttk.Style() 
style.theme_use("clam")

# widgets 
label = ttk.Label(root, text="Bienvnido a tu app", font=("Segoe UI", 14))
label.pack(pady=20)

entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

button = ttk.Button(root, text="Aceptar")
button.pack(pady=10)

root.mainloop()
