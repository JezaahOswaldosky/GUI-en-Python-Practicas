##                      programa11_proyecto.py 
##
##  programa11_proyecto.py es un programa de aplicacion de notas utilizando 
## la biblioteca tkinter y lenguaje python 
#############################################################################
import tkinter as tk 
from tkinter import messagebox 

## Lista para guardar notas en memoria 
notas = []

def saveNotas(): 
    titulo = entradaTitulo.get() 
    contenido = textoCont.get("1.0", tk.END).strip() 

    if titulo and contenido: 
        notas.append({"titulo": titulo, "contenido": contenido})
        messagebox.showinfo("Guardado", "Nota guardada exitosamente")
        entradaTitulo.delete(0,tk.END)
        textoCont.delete("1.0", tk.END)
    else: 
        messagebox.showwarning("Campos vacios", "Debes completas ambos campos.")

def showNotas(): 
    if not notas: 
        messagebox.showinfo("Sin notas", "No hay notas guardadas aun")
        return
    
    ventanaNotas = tk.Toplevel(ventana)
    ventanaNotas.title("Notas Guardadas")

    for nota in notas: 
        frame = tk.Frame(ventanaNotas, pady=5, padx=5, relief="solid", bd=1)
        tk.Label(frame, text="Titulo:", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(frame, text=nota["titulo"]).pack(anchor="w")
        tk.Label(frame, text="Contenido", font=("Arial",10,"bold")).pack(anchor="w")
        tk.Message(frame, text=nota["contenido"], width=400).pack(anchor="w")
        frame.pack(fill="x", padx=5, pady=5)

## Configurar la ventana principal 
ventana = tk.Tk() 
ventana.title("App de Notas")
ventana.geometry("500x400")

tk.Label(ventana, text="Titulo de la Nota: ").pack(anchor="w", padx=10, pady=(10,0))
entradaTitulo = tk.Entry(ventana, width=60)
entradaTitulo.pack(padx=10, pady=5)

tk.Label(ventana, text="Contenido: ").pack(anchor="w", padx=10)
textoCont = tk.Text(ventana, height=10, width=60)
textoCont.pack(padx=10, pady=5)

## Configurar botones de la aplicacion 
frameBtn = tk.Frame(ventana)
frameBtn.pack(pady=10)

tk.Button(frameBtn, text="Guardar Nota", command=saveNotas).pack(side="left", padx=10)
tk.Button(frameBtn, text="Ver Notas Guardadas", command=showNotas).pack(side="left", padx=10)

## Inicializar la GUI 
ventana.mainloop()