# Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.
def ver_edad(age):
    if age > 18:
        return print(f"tu edad {age} es mayor de edad ")
    else:
        return print(f"tu edad {age} es menor de edad")
edades = int(input("ingresa tu edad "))
print(ver_edad(edades))