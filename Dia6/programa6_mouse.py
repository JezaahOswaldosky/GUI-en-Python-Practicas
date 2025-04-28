import tkinter as tk 

## Funcion para mover el mouse 
def mouseMove(event): 
    print(f"Mouse en: {event.x}", {event.y})

ventana = tk.Tk() 
ventana.title("Seguimiento del mouse ")
frame = tk.Frame(ventana, width=300, height=200, bg="lightgreen")
frame.pack() 

frame.bind("<Motion>", mouseMove)

# Inicializar la ventana 
ventana.mainloop()
