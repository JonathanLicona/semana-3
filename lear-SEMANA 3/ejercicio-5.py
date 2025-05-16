#Crea una función que convierta grados Celsius a Crea una función que convierta grados Celsius a Fahrenheit.

def grados(celsi):
    fahrenheit = (celsi * 9/5) + 32
    return fahrenheit

try:
    temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
except ValueError:
    print("error ingrese un numero ")
exit()
temperatura_fahrenheit = grados(temperatura_celsius)
print(f"La temperatura {temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")


