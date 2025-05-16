filas = int(input("Ingrese la altura de la pirámide: "))
for p in range(1, filas + 1):
    print(" " * (filas - p), end="")
    for j in range(1, p + 1):
        print("*", end="*")
    print()