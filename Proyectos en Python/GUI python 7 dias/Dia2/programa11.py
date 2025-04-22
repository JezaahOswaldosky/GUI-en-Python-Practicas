from tkinter import Tk, ttk 

root = Tk() 
root.geometry("300x200")

label = ttk.Label(root, text="Ingrese su nombre")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=5)

button = ttk.Button(root, text = "Enviar")
button.pack(pady=10)

root.mainloop()