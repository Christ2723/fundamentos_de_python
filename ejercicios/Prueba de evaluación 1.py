# El usuario debe digitar su nombre, edad, y dos números. Luego podrá seleccionar una opción de un listado con las 4 operaciones básicas (Suma, Resta, División y Multiplicación) marcando su número correspondiente (1 - 4). Luego que elija la opción deseada, se debe realizar el cálculo de los 2 números con dicha operación e imprimir el cálculo La impresión del cálculo se debe mostrar de la siguiente manera (Ej: si el usuario digita los números 3 y 5 y selecciona la suma como operación):“La suma de 3 y 5 es igual a 8” Validaciones:Sólo se puede ingresar una edad de 1 a 120 años.El usuario no puede digitar una opción que no sea del 1 al 4.En el caso de la división, no se debe realizar si el usuario digita 0 como segundo número. En su defecto, se debe mostrar un mensaje que explique por qué no se pudo realizar la operación.

# El programa dira su nombre, edad, y dos números. Luego podrá seleccionar una opción de un listado con las 4 operaciones básicas (Suma, Resta, División y Multiplicación) marcando su número correspondiente (1 - 4). Luego que elija la opción deseada, se debe realizar el cálculo de los 2 números con dicha operación e imprimir el cálculo. 

print("Autor: Christopher Payero\n")

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: (edad maxima 120)"))
num = int(input("Digite un número: "))
num2 = int(input("Digite un número: "))


operacion = int(input("Elija un operador +,-,*,/:"))

if operacion == +:
    resultado1 = num + num2
    print(resultado1)
if operacion == -:
    resultado2 =  num - num2 
    print(resultado2)
if operacion == *:
    resultado3 = num * num2
    print(resultado3)
    
if operacion == /:
    num2 == 0
    print("La operacion no puede ser ejecutada: ") 
if not num2 == 0:
    resultado4 = num / num2  
    print(resultado4)
        
print("Hola mi nombre es Christlopher Payero: \n")

tabla = input("Te gustaria que te mostremos la tabla de multiplicacion de tu edad? (y/n) \n")

        
if tabla == "y":
    for num in range(1,13):
        resultado = num * edad
        print(edad, " x ", num, " = ", resultado)
    
elif tabla == "n":
   print("Gracias por su atencion!")


