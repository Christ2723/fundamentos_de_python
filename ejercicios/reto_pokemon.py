import requests
import re
# Constantes    
base_url = "https://pokeapi.co/api/v2/"
regrex_numbers = "[0-9]{1,3}$"

limite = input("Digite la cantidad de pokemos a mostrar: ")

while(not re.search(regrex_numbers,id_digitado)) or (id_digitado < primero or id_digitado > ultimo):
    id_digitado = input(f"por favor, digite un id valido [{primero}-{ultimo}]:")

id_digitado = int(id_digitado)

print("Mostrar primeros {limite} pokemones:")

url = base_url + "pokemon?limit={limite}&offset=200"
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
         