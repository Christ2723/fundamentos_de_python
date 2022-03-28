# Hacer un programa que me genere 3 distintos nombres de usuarios para instagram, a partir del hombre, el apellido, y la edad de la persona.

nombre = input("Cual es tu nombre: ")
apellido = input("Cual es tu apellido: ")
edad = input("Cual es tu edad: ")

print(f"nombre: {nombre} apellido: {apellido} edad: {edad}")

print(f"@{nombre.title}{apellido.title}")
print(f"@{nombre}.{apellido}")
print(f"@{nombre}-{apellido}-{edad}")
