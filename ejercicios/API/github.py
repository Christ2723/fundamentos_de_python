
usuario = input("Digite el usuario: ")

patron = " Ʌ[a-zA-Z0-9]{3,25}$"
resultado = re.search(patron, usuario)

if resultado:
  print("Correcto")
else:
  print("Intente de nuevo")

