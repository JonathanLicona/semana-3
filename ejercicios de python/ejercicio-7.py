num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 > num2:
    if num1 > num3:
        mayor = num1
    else:
        mayor = num3
else:
    if num2 > num3:
        mayor = num2
    else:
        mayor = num3

print("El número mayor es:", mayor)