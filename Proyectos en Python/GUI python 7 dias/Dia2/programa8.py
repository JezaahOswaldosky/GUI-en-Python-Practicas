import tkinter as tk 
ventana = tk.Tk() 

label1 = tk.Label(ventana, text="Fila 0, Columna 0", bg="lightblue")
label1.grid(row=0, column=0)

label2 = tk.Label(ventana, text="Fila 0, Columna 1", bg="lightgreen")
label2.grid(row=0, column=1)

label3 = tk.Label(ventana, text="Fila 1, Columna 0", bg="lightyellow")
label3.grid(row=1, column=0, columnspan=2)

label4 = tk.Label(ventana, text="Fila -, Columna0", bg="lightblue")
label4.grid(row=1, column=2, columnspan=3)

ventana.mainloop()
