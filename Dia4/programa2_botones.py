import tkinter as tk 

# Inicializar la GUI 
root = tk.Tk()

# Inicialiar el marco 1 
mainFrame = tk.Frame() 
mainFrame.grid(row=0, column=0)
mainFrame.config(width="100", height="100")
mainFrame.config(bg="red")

# Configurar el segunfo marco 
mainFrame2 = tk.Frame() 
mainFrame2.grid(row=0, column=1)
mainFrame2.config(width="100", height="100")
mainFrame2.config(bg="blue")

# Configurar el tercer marco 
mainFrame3 = tk.Frame() 
mainFrame3.grid(row=1, column=2)
mainFrame3.config(width="100", height="100")
mainFrame3.config(bg="green")

# Configurar el cuarto marco 
mainFrame4 = tk.Frame()
mainFrame4.grid(row=1, column=1)
mainFrame4.config(width="100", height="100")
mainFrame4.config(bg="yellow")

# Configurar el marco 5 
mainFrame5 = tk.Frame() 
mainFrame5.grid(row=2, column=0)
mainFrame5.config(width="100", height="100")
mainFrame5.config(bg="pink")

# Configurar el sexto marco 
mainFrame6 = tk.Frame() 
mainFrame6.grid(row=2, column=1)
mainFrame6.config(width="100", height="100")
mainFrame6.config(bg="purple")

# Configuramos el boton a utilizar 
boton1 = tk.Button(root, text="No presione el boton", bg="red", padx=100, pady=25, state="disabled").grid(row=1,column=2)

# Correr la GUI de forma indefinida 
root.mainloop()