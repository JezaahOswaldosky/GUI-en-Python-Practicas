archivo = open('texto.txt', 'r')
contenido = archivo.read() 
print(contenido)

with open("texto.txt", "r") as archivo: 
    contenido = archivo.read() 
    print(contenido) 