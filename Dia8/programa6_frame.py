##                      programa6_frame.py 
## programa6_frame.py es un programa que utiliza la funcion 
## .grid() y .pack() en widgets. Esto puede ser posible si se
## utiliza en diferentes frames. Un ejemplo en un frame trabajar 
## con grid() y en otro con pack() 
######################################################################
import tkinter as tk

root = tk.Tk()

# Frame 1 con pack()
frame1 = tk.Frame(root, bg="lightblue")
frame1.pack(side="top", fill="x")

label1 = tk.Label(frame1, text="Usando pack()")
label1.pack(padx=10, pady=10)

# Frame 2 con grid()
frame2 = tk.Frame(root, bg="lightgreen")
frame2.pack(side="top", fill="both", expand=True)

label2 = tk.Label(frame2, text="Fila 0, Columna 0")
label3 = tk.Label(frame2, text="Fila 0, Columna 1")

label2.grid(row=0, column=0, padx=5, pady=5)
label3.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()