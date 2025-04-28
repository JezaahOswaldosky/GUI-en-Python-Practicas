# Crear el archivo y escribir en el 
with open("textoNew.txt", "w") as archivo: 
    archivo.write("Hola mundo \n")
    archivo.write("Otra linea\n")

with open("textoNew.txt", "r") as archivo: 
    contenido = archivo.read()
    print(contenido)
