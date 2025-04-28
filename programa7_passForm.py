import tkinter as tk 
from tkinter import messagebox

# Funciones para los botones
def catchFnc(): 
    # Capturar la informacion del entry 
    infoNombre = nombre.get() 
    infoApellido = apellido.get() 
    infoEdad = edad.get()
    infoCURP = curp.get() 
    infoRFC = rfc.get()
    infoDireccion = direccion.get()
    infoCP = cp.get()
    # Comparar si algun entry se encuentra vacio 
    if(not infoNombre.strip()) or (not infoApellido.strip()) or (not infoEdad.strip()) or (not infoCURP.strip()) or (not infoRFC.strip()) or (not infoDireccion.strip()) or (not infoCP.strip()):
        messagebox.showwarning("Campo vacio!!", "Por favor llene todos los campos para continuar.")
    else:
    # Mostrar la informaciondel resulatado 
        etiquetaResultado.config(text=f"Nombre: {infoNombre}\nApellido: {infoApellido}\nEdad: {infoEdad}anios\nCURP: {infoCURP}\nRFC: {infoRFC}\nDireccion: {infoDireccion}\nC.P: {infoCP}")
    # Guardar informacion en un documento .txt 
        with open("UsarData.txt", "a") as archivo: 
            archivo.write(f"{infoNombre}, {infoApellido}, {infoEdad}, {infoCURP}, {infoRFC}, {infoDireccion}, {infoCP}; \n")
        


# Funcion para borrar informacion 
def borrarFnc():
    nombre.delete(0,tk.END)
    apellido.delete(0, tk.END)
    edad.delete(0, tk.END)
    curp.delete(0, tk.END)
    rfc.delete(0, tk.END)
    direccion.delete(0, tk.END)
    cp.delete(0, tk.END)
    etiquetaResultado.config(text=f"Aqui aparecera el texto!!!")
    etiquetaResultado.grid(row="15", column="1")
# Funcion para mostrar informacion sobre el proceso de captura 
# de informacion
def acercaFnc():
    messagebox.showinfo("Acerca de...", "Proceso donde el usuario debe registrar a " \
    "un empleado. ")
# Funcion para salir del programa 
def salir(): 
    root.destroy()

#  Configurar una ventana para GUI
root  = tk.Tk() 
root.title("Capturador de datos")
root.geometry("350x400")

# Creamos las etiquetas 
titulo = tk.Label(root,text="Datos del usuario")
titulo.grid(row="0", column="1" )

nomLabel = tk.Label(root, text="Nombre: ")
nomLabel.grid(row="1", column="0")

apeLabel = tk.Label(root, text="Apellido: ")
apeLabel.grid(row="2", column="0")

apeLabel = tk.Label(root, text="Edad: ")
apeLabel.grid(row="3", column="0")

apeLabel = tk.Label(root, text="CURP: ")
apeLabel.grid(row="4", column="0")

apeLabel = tk.Label(root, text="RFC: ")
apeLabel.grid(row="5", column="0")

apeLabel = tk.Label(root, text="Direccion: ")
apeLabel.grid(row="6", column="0")

apeLabel = tk.Label(root, text="CP: ")
apeLabel.grid(row="7", column="0")

# Etiqueta para mostrar informacion 
etiquetaResultado = tk.Label(root, text="Aqui aparecera el texto!!!")
etiquetaResultado.grid(row="15", column="1")

# Crear entradas para cada label 
nombre = tk.Entry()
nombre.grid(row="1", column="1")

apellido = tk.Entry()
apellido.grid(row="2", column="1")

edad = tk.Entry()
edad.grid(row="3", column="1")

curp= tk.Entry()
curp.grid(row="4", column="1")

rfc = tk.Entry()
rfc.grid(row="5", column="1")

direccion = tk.Entry()
direccion.grid(row="6", column="1")

cp = tk.Entry()
cp.grid(row="7", column="1")

# Configurar un boton para capturar la informacion 
catchButton = tk.Button(root, text="Capturar", padx=25, pady=3, command=catchFnc).grid(row="9", column="1")
eraseButton = tk.Button(root, text="Borrar", padx=32, pady=3, command=borrarFnc).grid(row="11", column="1")
acercaButton = tk.Button(root, text="Acerca de", padx=22, pady=3, command=acercaFnc).grid(row="12", column="1")
salirButton = tk.Button(root,text="Salir", padx=37, pady=3, command=salir).grid(row="13", column="1")

# Ejecutar la ventana indefinidamente 
root.mainloop()