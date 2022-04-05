import re
import requests
import webbrowser

usuario = int(input("Digite el numero de pokemo: "))
  
url = f" https://pokeapi.co/api/v2/ability/{usuario}"
respuesta = requests.get(url)
if respuesta:
  datos = respuesta.json()
  print("Nombres:")
  print(f"Cantidad de nombres: {len(datos['name']) }")

  idiomas = []
  habilidades = []
  peso = None
  altura = None
  cantidad_de_movimientos = []
  for nombres in datos['names']:
    idiomas.append(nombres['language']['name'])
    habilidades.append(nombres,['name'])
    peso.append(nombres,['weight:'])
    altura.append(nombres,['height:'])
    cantidad_de_movimientos.append(nombres,['moves:']) 

  print("-"*20)
  print("Listado de idiomas: ")
  for idioma in idiomas:
    print(idioma)

    print(peso)

    print(altura)

  print("Listado de habilidades: ")
  for movimientos in  cantidad_de_movimientos:
    print( cantidad_de_movimientos)
else:
  Print("El pokemo no existe: ")

