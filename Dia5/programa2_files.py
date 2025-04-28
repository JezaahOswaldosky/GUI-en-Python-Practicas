# Metodo aceptado por la industria del software 
with open("texto.txt", "r") as archivo: 
    for linea in archivo: 
        print(linea.strip())

# Metodo utiliado por las academias 
archivo = open("texto.txt", "r")
print(archivo.readline())   # Lee una linea 
print(archivo.readlines())  # Devuelve una lista de todas las lineas 
archivo.close()
