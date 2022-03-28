# Recrear el Sign Up de GitHub (Esta fue mi manera).

usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese la Contrasena: ")
if usuario 
    print("El usuario es correcto") 
else:
    print("El usuario es incorrecto")       
if contrasena 
        print("La contrasena es correcta ")
else:
    print("La contrasena es incorrecta")

# La manera del maestro (Esto era lo que teniamos que hacer).

import pwinput
import time

texto = "Welcome to GitHub! Let's begin the adventure"

for letra in texto:
  print(letra,end="",flush=True)
  time.sleep(0.04)

print("Enter your email")
email = input("-> ")

print("Create a password")
input = pwinput.pwinput(mask="*")