import requests
x1 = int(input("Cuantos resultados desea ver:? "))
while 1x <= 898:
rl = f"https://pokeapi.co/api/v2/pokemon?limit=50&offset=1"

respuesta = requests.get(url)
datos = respuesta.json()
nombres = []
for x in range(len(datos['results'])):
  nombres.append(datos['results'][x]['name'])

for i,x in enumerate(nombre,1):
  print(f"{i+x}

