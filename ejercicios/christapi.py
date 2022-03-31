import requests  

expresion = [a-z,A-Z,0-9]

usuario = input("Digite su usuario: ").strip().replace(" ","").lower()
if usuario not in expresion:
  print("Debe digitar su usuario de nuevo: ")
elif usuario in expresion:
  print("espere....") 
URL = https://github.com/search?q=&type=
data = requests.get(URL) 

data = data.json() 

for element in data[()]:
    print(element['usuario encontrado'])

followers = 452
followings = 275
prublic_repos = 5

if element == "usuario encontrado":
  print(usuario,followers,followings,public_repos)
else:
  print("El usuario no existe, no fue encontrado. ")
https://github.com/session
encontrado = input("Desea crear un usuario: (y/n)?")
if encontrado == "y":
  print("Abrir en el navegador, la URL para registrarse: https://github.com/session")

if encontrado == "n":
  print("Hasta luego. #KeepCoding.")
  
  
  
  