# Aritmeticos
suma = 5 + 10
print(suma,type(suma))

resta = 5 - 10
print(resta,type(resta))

multiplicacion = 5 * 10
print(multiplicacion,type(multiplicacion))

division = 5 / 10
print(division,type(division))

residuo = 5 % 10
print(residuo,type(residuo))

potencia = 5 ** 10
print(potencia,type(potencia))

division_entera = 5 + 10
print(division_entera,type(division_entera))

# Relacionales

num = 5 > 2
print(num,type(num))

num2 = 1 < 2
print(num2,type(num2))

num3 = 5 == 5
print(num3,type(num3))

num4 = 5 >= 2
print(num4,type(num4))

num5 = 1 <= 2
print(num5,type(num5))

num6 = 5 != 2
print(num6,type(num6))

#Logicos

num = 5 > 2 and 5 > 10
print(num,type(num))

num = 5 > 2 or 5 > 10
print(num,type(num))

num = 5 > 2 and not 5 > 10
print(num,type(num))

# Pertenencia

lista = 10 in range(1,20)
print(lista, type(lista))    


lista = 6 not in range(1,20)
print(lista, type(lista))  

#indentidad 

christ1 = 5
christ2 = 5

print(christ1 is christ2)
print(christ1 is not christ2)