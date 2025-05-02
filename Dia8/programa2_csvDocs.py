###                 programa2_csvDocs.py
## programa2_csvDocs.py es un programa que captura informacion en un archivo .csv 
####################################################################################################
import csv 

# Capturar informacion del usuario 
nombre =  input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
domicilio = input("Domicilio: ")
cPostal = input("C.P: ")

# Corroborar que la info se guardo correctamente
print("\n\n\aLa informacion se guardo correctamente!!!")
print(f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDomiclio: {domicilio}\nC.P: {cPostal}\n")

# Convertir informacion a datos
datos = [nombre, apellido, edad, domicilio, cPostal]

# Guardar informacion in el archivador 
with open('baseDatos.csv', 'a') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(datos)
