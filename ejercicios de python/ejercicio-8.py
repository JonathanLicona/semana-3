num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa un operador (+, -, *, /): ")


if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        resultado = print("Error: División por cero")
    else:
        resultado = num1 / num2
else:
    resultado = print("Operador inválido")

print("El resultado es:", resultado)