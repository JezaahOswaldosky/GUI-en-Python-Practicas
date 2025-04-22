# Programa que tiene entrada de texto 
# entry para campos de texto y leer valores escritos por el usuario 
import tkinter as tk 

def mostrar_texto(): 
    texto = entrada.get() 
    etiqueta_resultado.config(text=f"Escribister: {texto}")

ventana = tk.Tk()
ventana.title("Entrada de Texto")
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="Escribiste algo:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack() 

boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
