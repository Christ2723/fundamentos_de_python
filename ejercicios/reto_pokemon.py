import requests
import re

print("Mostrar primeros 20 pokemones:")

base_url = "https://pokeapi.co/api/v2/"
regrex_numbers = "[0-9]{1,3}$"

url = base_url + "pokemon?limit=100&offset=200"
respuesta = requests.get(url)

if respuesta:
    datos = respuesta.json()

    primero = None
    ultimo = None
    for pokemon in datos ['results']:
        id_pokemon = pokemon['url'].split('/')[6]
        nombre = pokemon['name']

    if primero == None:
        primero = int(id_pokemon)

    print(id_pokemon, nombre)

ultimo = int(id_pokemon)

id_digitado = input(f'Digite un id[{primero}-{ultimo}]:')
resultado = re.search(regrex_numbers, id_digitado)
import requests
import re

print("Mostrar primeros 20 pokemones:")

base_url = "https://pokeapi.co/api/v2/"
regrex_numbers = "[0-9]{1,3}$"

url = base_url + "pokemon?limit=100&offset=200"
respuesta = requests.get(url)

if respuesta:
    datos = respuesta.json()

    primero = None
    ultimo = None
    for pokemon in datos ['results']:
        id_pokemon = pokemon['url'].split('/')[6]
        nombre = pokemon['name']

    if primero == None:
        primero = int(id_pokemon)

    print(id_pokemon, nombre)

ultimo = int(id_pokemon)

id_digitado = input(f'Digite un id[{primero}-{ultimo}]:')
resultado = re.search(regrex_numbers, id_digitado)

while not resultado:
    id_digitado = input(f'Digite un id [{primero}-{ultimo}]: ')
    resultado = re.search(regrex_numbers,id_digitado)

id_digitado = int(id_digitado)

while id_digitado < primero or id_digitado > ultimo:
    id_digitado = int(input(f'Digite un id valido[{primero}-{ultimo}]:'))

else:
    print(f"Ocurrio un error ({respuesta.status_code}) al obtener los datos")  
while not resultado:
    id_digitado = input(f'Digite un id [{primero}-{ultimo}]: ')
    resultado = re.search(regrex_numbers,id_digitado)

id_digitado = int(id_digitado)

while id_digitado < primero or id_digitado > ultimo:
    id_digitado = int(input(f'Digite un id valido[{primero}-{ultimo}]:'))

else:
    print(f"Ocurrio un error ({respuesta.status_code}) al obtener los datos")  
         