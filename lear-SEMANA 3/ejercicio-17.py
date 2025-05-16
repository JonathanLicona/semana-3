import random

def tirar_dado():

    return random.randint(1, 6)

# como se usa 
resultado = tirar_dado()
print(f"El resultado del lanzamiento es: {resultado}")