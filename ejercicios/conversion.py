# Hacer un programa que me pida digitar un monto en pesos y mostar el resultado en dolares. Hacerlo en USer-friendly

monto = float(input("Bienvenido, por favor ingrese su monto: ".strip()))
dinero = "{0:.2f}".format(monto / 55.15)
print(dinero)