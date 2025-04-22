import tkinter as tk 

root = tk.Tk()
root.geometry("600x400")

# Frame superior
top_frame = tk.Frame(root, bg="gray", height=50)
top_frame.pack(fill="x")

# Frame principal 
main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)

# Agregar contenido 
label = tk.Label(main_frame, text="Bienvenido", font=("Arial",18))
label.pack(pady=20)

root.mainloop()