# Ejemplo para crear un documento de texto 
# Introducir simple texto al documento 
with open("nuevo.txt", "w") as archivo: 
    archivo.write("Nuevo mensaje\n")
    archivo.write("Putos!!\n\a")
# Leemos el documento 
with open("nuevo.txt", "r") as archivo: 
    print(archivo.read())
# Agregar informacion al documento 
with open("nuevo.txt", "a") as archivo: 
    archivo.write("Linea adicional agregada\n")

#Volver a leer el archivo pero esta ver completo 
with open("nuevo.txt", "r") as archivo: 
    print(archivo.read())
    