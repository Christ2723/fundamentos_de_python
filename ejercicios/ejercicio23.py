try:
  num1 = input("Digite numero 1: ")
  num2 = input("Digite numero 2: ")

  resultado = numero1 / numero2

except TypeError:  
  print("ha ocurrido un error dde tipeo")

except ZerpdivisionError:
  print("No se puede dividir entre 0")

  edad = int(input("Digite una edad"))

  if edad < 18:
    raise Exception("No puede ser menor")
    
  print("El leo....")  
print("hola")  