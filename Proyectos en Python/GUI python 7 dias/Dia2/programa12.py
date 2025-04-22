from tkinter import Tk, ttk 

root = Tk() 
style = ttk.Style() 

# Ver temas disponibles 
print(style.theme_names())

# Usar un tema 
style.theme_use('xpnative')  # Otros temas son alt, default, vista xpnative

ttk.Button(root, text="Boton con estilo!").pack(pady=20)

root.mainloop()