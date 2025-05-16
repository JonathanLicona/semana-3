def numero_par(num):
    if num % 2 == 0:
        return print(f"tu numero {num} es par ")
    else:
        return print(f"tu numero {num} es impar")
numero = int(input("ingrese un numero: "))
print(numero_par(numero))