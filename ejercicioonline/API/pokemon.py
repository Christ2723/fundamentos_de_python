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
  for nombres in datos['names']:
    idiomas.append(nombres['language']['name'])
    habilidades.append(nombres,['name'])

  print("-"*20)
  print("Listado de idiomas: ")
  for idioma in idiomas:
    print(idioma)

  print("Listado de habilidades: ")
  for habilidades in habilidades:
    print(habilidad)
else:
  Print("El pokemo no existe: ")


