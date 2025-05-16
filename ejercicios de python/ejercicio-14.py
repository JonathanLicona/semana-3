num = int(input("ingresa un numero: "))
for i in range (0,11):
    resultado = i * num
    print(("%d * %d = %d") % (num, i, resultado))