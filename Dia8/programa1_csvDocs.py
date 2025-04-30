###                             programa1_csvDocs.py 
### programa1_csvDocs.py es un programa que permite al usuario leer archivos .csv para leer informacion
### en formato de listas.
###################################################################################################
import csv 

datos = [['Nombre','Edad','Ciudad'], 
        ['Carlos','28','Sevilla'],
        ['Maria','34','Valencia'] ]

with open('salida.csv', 'w', newline='') as archivo: 
    escritor = csv.writer(archivo) 
    escritor.writerows(datos)

