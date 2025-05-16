#Escribe una función que devuelva el área de un triángulo dado su base y altura.
def area(base, altura):
  return (base * altura) / 2.0
base = 8
altura = 5
areas = area(base, altura)
print(f"El área del triángulo con base {base} y altura {altura} es: {areas}")