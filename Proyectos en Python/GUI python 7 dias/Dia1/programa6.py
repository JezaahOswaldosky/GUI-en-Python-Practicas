# Programa que utiliza un meno y organiza iconos 
import tkinter as tk 

def accion_nuevo(): 
    etiqueta.config(text="Nuevo archivo creado")

def accion_guardar(): 
    etiqueta.config(text="Archivo guardado")

def accion_salir():
    ventana.quit()

ventana = tk.Tk() 
ventana.title("Menus en Tkinter")
ventana.geometry("300x200")

# Creamos el menu principal 
menu_principal = tk.Menu(ventana)
ventana.config(menu = menu_principal)

# Submenu "Archivo"
menu_archivo =  tk.Menu(menu_principal, tearoff = 0)
menu_principal.add_cascade(label = "Archivo", menu = menu_archivo)
menu_archivo.add_command(label="Nuevo", command = accion_nuevo)
menu_archivo.add_command(label="Guardar", command = accion_guardar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command = accion_salir)

# Etiqueta para mostrar acciones 
etiqueta = tk.Label(ventana, text = "Selecciona una opcion del menu")
etiqueta.pack(pady = 50)

ventana.mainloop()
