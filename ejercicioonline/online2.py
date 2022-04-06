# Hacer un programa que muestre un listado con los pokemones, el usuario tendra la oportunidad de digitar su id correspondeinte, y se le mostrara la informacion relacionada al mismo.

# ademas, el usuario podra navegar en el programa mediante los shortcuts y/o teclas del teclado:
# algunas de las opciones serian:
# ver siguiente/anterior listado:
# ver siguiente/anterior pokemo:
# salir del programa:
# buscar un pokemon por su id:
# buscar:

import requests

pokemones = []

usuario = input("Digite un pokemon")
url = f" https://pokeapi.co/api/v2/ability/{usuario}" respuesta = requests.get(url)
if respuesta:
  datos = requests,json()
  for poke in lista()  