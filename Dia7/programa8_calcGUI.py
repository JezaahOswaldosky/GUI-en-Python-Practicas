##                          programa8_calcGUI.py 
## programqa8_calcGUI.py es una interfaz grafica que permite al usuario introducis dos datos en unos 
## campos de texto Entry para presionar un boton y sumar los numeros. Mostrando el resultado en un 
## una etiqueta. 
#########################################################################################################
import tkinter as tk 

# Definir funcion 
def sumar(): 
    # Tomamos los numeros de A y B y convertimos a enteros
    a = numA.get()
    a = int(a)

    b = numB.get() 
    b = int(b)

    # Imprimir el resultado en el label 
    resLabel.config(text=f"{a+b}")
def restar(): 
    # Tomamos los numeros de A y B y convertimos a enteros
    a = numA.get()
    a = int(a)

    b = numB.get() 
    b = int(b)

    # Imprimir el resultado en el label 
    resLabel.config(text=f"{a-b}")

def salir(): 
    ventana.destroy()

# Configurar la GUI 
ventana = tk.Tk() 
ventana.title("programa8_calcGUI.py")
ventana.geometry("300x300")
ventana.resizable(False, False)

# Colocar Label de titulo
titulo = tk.Label(ventana, text="Calculadora de Suma/Resta")
titulo.pack(pady=(20,5))
# Colocar campos de texto o entry
numA = tk.Entry()
numA.pack(pady=(20,15))

numB = tk.Entry()
numB.pack(pady=(20,25))

## Configurar la etiqueta del resultado 
etiquetaLabel = tk.Label(ventana, text="Resultado:")
etiquetaLabel.place(x=20, y=150)

resLabel = tk.Label(ventana, text="", bg="lightgrey", padx=60, pady=1)
resLabel.place(x=87,y=150)

## Configurar botones
sumaButton = tk.Button(ventana, text="Sumar", command = sumar)
sumaButton.place(x=90, y=200)

restaButton = tk.Button(ventana, text = "Restar", command= restar)
restaButton.place(x=160, y=200)

salirButton = tk.Button(ventana, text= "Salir", command=salir)
salirButton.place(x=125 , y=250)


# Ejecutar la ventana
ventana.mainloop()