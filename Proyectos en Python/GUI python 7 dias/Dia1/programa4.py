## Diferencias entre .pack() y .grid()?? 
# La principal diferencia entre .pack() y .grid() en Tkinter es su metodo de
#  posicionamiento de widgets: .pack() es un gestor de diseno sencilla que coloca 
# los wirgets uno al lado del otro, mientras que .grid() usa una disposicion de 
# cuadricula, lo que permite colocar widgets en filas y columnas. 
# .pack(): posicionamiento relatico, en direcciones arriba, abajo, izq y der. Facil 
# de usar. No es precisa. 
# .grid(): posicionamiento absoluto, lo que permite colocar widgets en cuadriculas 
# definidas y mayor precision en la ubicacion de los widgets. 
# Organizacion y Flexibilidad 

import tkinter as tk 

ventana = tk.Tk() 
ventana.title("Formulario Basico")
ventana.geometry("300x150")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5,pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0,column=1,padx=5,pady=5)

tk.Label(ventana, text="Edad: ").grid(row=1,column=0,padx=5,pady=5)
entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1,column=1,padx=5,pady=5)

tk.Label(ventana,text="Edad:").grid(row=1,column=1,padx=5,pady=5)
entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1,column=1,padx=5,pady=5)

def mostrar_datos():
    nombre = entrada_nombre.get() 
    edad = entrada_edad.get() 
    resultado.config(text=f"Hola {nombre}, tienes {edad} anios")

boton = tk.Button(ventana, text="Enviar", command=mostrar_datos)
boton.grid(row=2,column=2,columnspan=2,pady=10)

resultado = tk.Label(ventana, text="")
resultado.grid(row=3,column=0,columnspan=2)

ventana.mainloop()
