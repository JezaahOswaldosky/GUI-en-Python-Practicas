#                       programa3_objetos.py
# programa3_objetos.py es un programa ejemplo de como crear 
# objetos desde python y a utilizarlos, muy ideal para desarrolalr
# cosas como GUI o interfaces graficas n.n 
########################################################################

# creamos el objeto 
class Hotel: 
    def __init__(self,nombre, direccion, numHab): 
        self.nombre = nombre 
        self.direccion = direccion 
        self.numHab = numHab 

    def showData(self): 
        print(f"\t\t\tDatos del hotel\n")
        print(f"Nombre del hotel: {self.nombre}\n")
        print(f"Direccion = {self.direccion}\n")
        print(f"Numero de habitaciones = {self.numHab}\n")
    
class Habitacion: 
    def __init__(self, numHab, precio, capacidad): 
        self.numHab = numHab
        self.precio = precio 
        self.capacidad = capacidad 
    def showData(self): 
        print(f"\t\t\tDatos de la Habitacion\n")
        print(f"Numero de habitaciones: {self.numHab}\n")
        print(f"Precio: {self.precio}\n")
        print(f"Capacidad: {self.capacidad}\n")

class Huesped:
    def __init__(self, nombre, apellido): 
        self.nombre = nombre 
        self.apellido = apellido 

    def showData(self): 
        print(f"\t\t\tDatos del huesped\n")
        print(f"Nombre: {self.nombre}\n") 
        print(f"Apellido: {self.apellido}\n")

# Creamos la informacion 
hotel1 = Hotel("Hotel San Juan", "Calle 24", 50)
hotel1.showData()

# Creamos mas informacion 
habitacion = Habitacion(50,399,4)
habitacion.showData()

# Creamos los datos del cliente 
huesped1 = Huesped("Jose Luis", "Morales Gozo")
huesped1.showData()