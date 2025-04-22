## Programa que genera ventanas emergentes 
import tkinter as tk 
from tkinter import messagebox 

def mostrar_mensaje(): 
    nombre = entrada.get() 
    if nombre: 
        messagebox.showinfo("Saludo",f"Hola, {nombre}")
    else: 
        messagebox.showwarning("Advertencia", "Por favor, escribe tu nombre")

ventana = tk.Tk()
ventana.title("Mensaje emergente")
ventana.geometry("300x150")

tk.Label(ventana, text="Ingresa tu nombre: ").pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()

