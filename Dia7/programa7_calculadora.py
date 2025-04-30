##                      programa7_calculadora.py 
##  programa7_calculadora.py es un programa que permite al usuario introducir dos numeros y realizar 
## una calculadora que le permite sumar, restar, dividir o multiplicar dos numeros. 
####################################################################################################

## Imprimir disclaimer para mostrar 
print("Bienvenido a programa7_calculadora.py")
print("\nLas opciones son las siguientes: Sumar(+)\n2.Restar(-)\n3.Multiplicar(x)\n4.Dividir(/)")
## Pedir al usuario el numero a 
a = float(input("Introduzca un numero a: "))

# Pedir opcion para saber que hacer con los numeros 
opc =  input("")

# Peir al usaurio el numero b 
b = float(input("Introduzca un numero b: "))

# Entra al flujo de las opciones 
if(opc == "+"): 
    print(f"{a} + {b} = {a+b}")
elif(opc == "-"): 
    print(f"{a} - {b} = {a-b}")
elif(opc == "x"): 
    print(f"{a} x {b} = {a*b}")
elif(opc == "/"): 
    print(f"{a} / {b} = {a/b}")
else: 
    print("Esa opcion no se encuentra dentro de las opciones!!!")
