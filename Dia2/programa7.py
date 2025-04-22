import tkinter as tk 

ventana = tk.Tk() 

label1 = tk.Label(ventana, text="Etiqueta 1", bg="red")
label1.pack(side="top",fill="x")

label1 = tk.Label(ventana, text="Etiqueta 2", bg="blue")
label1.pack(side="bottom",fill="x")

ventana.mainloop()
