import tkinter as tk 

# Funcion para mostrar el click 
def clickShow(event): 
    print(f"Click en las coordenadas: {event.x}, {event.y}")

# Configurar la ventana de GUI 
ventana = tk.Tk() 
ventana.title("Ejemplo de click con bind()")

# Configurar un canvas o cubierta en la GUI
canvas = tk.Canvas(ventana, width=300, height=200, bg="lightblue")
canvas.pack() 

canvas.bind("<Button-1>", clickShow)

# Ejecutar la ventana 
ventana.mainloop()
asceasd