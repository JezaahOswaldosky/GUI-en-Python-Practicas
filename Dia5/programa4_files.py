# Creamos el archivo y escribimos en el 
with open("fileNew.txt", "w") as archivo: 
    archivo.write("Hola mundo \n")
    archivo.write("Pendejos todos!!\n")
    archivo.write("Es broma, solo estamos aqui dude!!\n")
    archivo.write("En fin, todo bien, todo correctus!!!\n")

# Leemos el archivo documentado para verificar que se creo
with open("fileNew.txt", "r") as archivo: 
    contenido = archivo.read() 
    print(contenido)
    