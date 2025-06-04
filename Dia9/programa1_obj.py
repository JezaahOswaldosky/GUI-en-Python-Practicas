##                                  programa1_onj.py
## 
## programa1_obj.py es un programa que maneja programacion orientada a objetos POO. 
## El programa consiste en manejar una clase Animal para heredar atributos de Animal a 
## a las clases heredados Ave, Mamifero, Reptil y Pez
####################################################################################################
# Inicializar la clase animal
class Animal: 
    def __init__(self, nombre, alimento, habitat): 
        self.nombre = nombre 
        self.alimento = alimento 
        self.habitat = habitat 
    def mostrarInfo(self): 
        print(f"Nombre: {self.nombre}\nAlimento: {self.alimento}\nHabitad: {self.habitat}")
    
# Inicializar la clase mamifero
class Mamifero(Animal):
    def __init__(self, nombre, alimento, habitat, pelaje, esCuadrupedo, esAcuatico)
        super().__ini__(nombre, alimento, habitat)
        self.pelaje = pelaje 
        self.esCuadrupedo = esCuadrupedo
        self.esActuatico = esAcuatico
    def mostrarInfo(self): 
        super().mostrarInfo()
        print(f"Tipo de pelaje: {self.pelaje}\nEs cuadrupedo: {self.esCuadrupedo}\nEs acuatico: {self.esActuatico}")

# Inicializar la clase Reptil
class Reptil(Animal): 
    def __init__(self, nombre, alimento, habitat, tienePatas, esVenenoso, esRegenerativo): 
        super().__init__(nombre, alimento, habitat)
        self.tienePatas = tienePatas
        self.esVenenoso = esVenenoso 
        self.esRegenerativo = esRegenerativo
    def mostrarInfo(self): 
        super().mostrarInfo()
        print(f"Tiene patas: {self.tienePatas}\nEs venenoso: {self.esVenenoso}\nEs regenerativo: {self.esRegenerativo}")
    
## Inicializar la clase Pez
class Pez(Animal): 
    def __init__(self, nombre, alimento, habitat, tipoAgua, esPredador): 
        super().__init__(nombre, alimento, habitat)
        self.tipoAgua = tipoAgua
        self.esPredador = esPredador
    def mostrarInfo(self): 
        super().mostrarInfo() 
        print(f"Tipo de agua: {self.tipoAgua}\nEs depredador: {self.esPredador}")

# Llamar a una clase con su metodo 
