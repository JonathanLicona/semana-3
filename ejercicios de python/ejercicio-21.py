
num = []

while True:
    entrada = input("Ingrese un número (o 'fin' para finalizar): ")
    
    if entrada.lower() == "fin":
        break 
    
    try:
        numero = float(entrada)  
        num.append(numero)  
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número o 'fin'.")
        continue 
    suma = 0
    for numero in num:
        suma += numero
        print("La suma de los números ingresados es:", suma)