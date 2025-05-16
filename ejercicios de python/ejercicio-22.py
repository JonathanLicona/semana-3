
lista = [10, 20, 30, 40, 50]
elemento = int(input("ingresa un numero"))
encontrado = False
for elemento in lista:
    if elemento == elemento:
        print("Elemento encontrado:", elemento)
        encontrado = True
        break
      
if not encontrado:
    print("Elemento no encontrado en la lista")