import re
import requests
import webbrowser

usuario = int(input("Digite el numero de pokemo: "))
  
url = f" https://pokeapi.co/api/v2/ability/{usuario}"
respuesta = requests.get(url)
if respuesta:
  datos = respuesta.json()
  print(datos)
else:
  Print("El pokemo no existe: ")