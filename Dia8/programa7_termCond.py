##                  programa7_termCond.py 
## programa7_termCond.py es un programa de terminos y 
## condiciones para un prograa en especifico para imprimir 
## un documento de casorio digital. 
## Solo constara de un Label con las condiciones del casorio
## y procedimientos para anular el casamiento y que podria 
## ocurrir bajo leyes federales y estatales que pueden ser 
## modificador segun el estado. 
################################################################
import tkinter as tk 
from tkinter import messagebox, scrolledtext

# Definimos la funcion de aceptar 
def aceptar(): 
    if checkVar.get():
        messagebox.showinfo("Aceptado", "Gracias por aceptar los terminos y condiciones.")
        ventana.destroy()  # Cierra la ventana 
    else: 
        messagebox.showwarning("Advertencia", "Debes aceptar los terminos para continuar.")


# Configuramos la ventana 
ventana = tk.Tk() 
ventana.title("Terminos y condiciones")
ventana.geometry("500x400")
ventana.resizable(False, False)

# Configurar el icono de la aplicacion 
icono = tk.PhotoImage(file="icono.png")
ventana.iconphoto(False,icono)

# Titulo 
titulo = tk.Label(ventana, text="TERMINO Y CONDICIONES", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Area de texto con desplazamiento 
terminos = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=60, height=15)
terminos.insert(tk.END, """
Bienvenido a nuestra aplicacion. 
               
Antes de continua, debes aceptar los siguientes terminos: 
               
1. El uso de esta aplicacion es bajo tu propio riesgo
2. No compartas tu informacion personal. 
3. Nos reservamos el derecho de combiar estos terminos en cualquier momento. 
4. Esta aplicacion es solo para fines educativos y no garantiza ningun resultado especifico. 

Por favor, lee con atencion y acepta para contiuar.
""")

terminos.config(state="disabled")
terminos.pack(padx=10,pady=10)

# Checkbox para aceptar 
checkVar = tk.BooleanVar()
check_btn = tk.Checkbutton(ventana, text="Acepto los terminos y codiciones", variable=checkVar)
check_btn.pack()

# Boton para continuar 
btn = tk.Button(ventana, text ="Continuar", command=aceptar)
btn.pack(pady=10)

# Inicializar la ventana 
ventana.mainloop()
