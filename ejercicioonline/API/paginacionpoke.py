import requests

url = f"https://pokeapi.co/api/v2/pokemon?limit=50&offset=1"

respuesta = requests.get(url)
dato = respuesta.json()
datos = []
for nombres in range(len(dato['results'])):
  datos.append(dato['results'][nombres]['name'])
print(datos)
   
