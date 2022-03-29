# Ejercicio 1: calcular la multiplicacion y suma de dos numeros: dados dos numeros enteros , devuelva su producto solo si el producto es mayor que 1000, de lo contrario, devuelven su suma.

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
multiplicacion = num1 * num2
suma = num1 + num2

if multiplicacion > 1000:
  print (multiplicacion)
else:
  print(suma)





