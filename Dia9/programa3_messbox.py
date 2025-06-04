##                              programa3_messbox.py
##
## programa3_messbox.py es un programa de un juego basico basado en
## preguntas de si o no para obtener puntajes. 
#######################################################################
import tkinter as tk
from tkinter import messagebox

# Creamos la funcion para iniciar el juego 
def inicio(): 
    resp = messagebox.askyesno("Haz iniciado el juego", "Deseas continuar?")
    puntos = 0
    mostrarPuntos(puntos)
    if resp: 
        pass
    else: 
        ventana.destroy()
        messagebox.showinfo("Cobarde","Te dio Culo!!\nCobarde. Pierdete de mi vista, maldito pussy")

## Funcion para mostrar las preguntas 
def preguntas(numQuest): 
    


## Funcion para mostrar puntos en el label 
def mostrarPuntos(puntos): 
    ## Entry para mostrar el puntaje 
    puntosLabel2 = tk.Label(ventana, text=f"{puntos}", bg="lightgrey", padx=40, pady=1)
    puntosLabel2.place(x=145, y=15)


def acercaDe(): 
    messagebox.showinfo("Acerca de..", """El programa fue desarrollado por un paralitico mental que se hace llamar Jezaah Oswaldosky. El sujeto tiende a escribir codigo sabiendo que una IA hace un mejor trabajo que el orillandolo a que busque otro trabajo el cual no pueda ser remplazable. Pero en fin. Hablando del programa, consiste en un sistema de preguntas que permite al usuario dar opciones de Si o No y acumular puntajes. 
Atte: Su PTM!! XD  """)

# Configrar la ventana 
ventana = tk.Tk() 
ventana.title("Juego de preguntas")
ventana.geometry("300x150")
ventana.resizable(False, False)

## Colocamos un label para el puntaje 
puntoLabel = tk.Label(ventana, text="Puntos: ", font=("Arial", 14,"bold"))
puntoLabel.place(x=60,y=10)



## Boton de inicio 
startBtn = tk.Button(ventana, text="Iniciar Juego", command=inicio)
startBtn.place(x=100, y=70)

## Boton de Acerca de
aboutBtn = tk.Button(ventana, text="Acerda de..", command=acercaDe)
aboutBtn.place(x=100, y=110)

# Ejecutar la ventana 
ventana.mainloop()

