# Programa que abre una ventana y cuenta la cantidad de veces que esta es abierta 
import tkinter as tk 
# Crear la ventana princial 
ventana = tk.Tk() 
ventana.title("Viruz cagapalos")
ventana.geometry("400x300")

x = 0

# Etiqueta del conteo 
etiqueta = tk.Label(ventana, text="Hola ", font=("Arial",14))
etiqueta.pack(pady=20)

# Boton para cerrra la ventana 
botonSalir = tk.Button(ventana, text="Salir", command=ventana.quit)
botonSalir.pack()

# Iniciar el buble de la app, pero varias veces 

while x < 5: 
    ventana.mainloop()
    x += 1