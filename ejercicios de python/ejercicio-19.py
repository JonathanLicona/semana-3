num = int(input("Ingresa un número: "))
fac = 1

for i in range(1, num + 1):
    fac = fac * i

print("El factorial de", num, "es:", fac)