import tkinter as tk 

# Inicializar la GUI 
root = tk.Tk()
# Marco 1 
mainFrame = tk.Frame() 
mainFrame.grid(row=0, column=0)
mainFrame.config(width="100", height="100")
mainFrame.config(bg="red")

# Marco 2
mainFrame2 = tk.Frame() 
mainFrame2.grid(row=1, column=0)
mainFrame2.config(width="100", height="100")
mainFrame2.config(bg="yellow")
 
# Marco 3
mainFrame2 = tk.Frame() 
mainFrame2.grid(row=1, column=1)
mainFrame2.config(width="100", height="100")
mainFrame2.config(bg="blue")

# Marco 4
mainFrame2 = tk.Frame() 
mainFrame2.grid(row=2, column=0)
mainFrame2.config(width="100", height="100")
mainFrame2.config(bg="green")

# Correr la GUI infinitamente 
root.mainloop()
