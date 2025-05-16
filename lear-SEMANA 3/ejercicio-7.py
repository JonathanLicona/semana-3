#Crea una función que reciba una lista de números y devuelva el mayor.
def maximo(valores):
  if not valores:
    return None
  return max(valores)
valores = [5, 2, 8, 1, 9, 3]
valor_maximo = maximo(valores)
if valor_maximo is not None:
  print("El valor máximo en la lista es:", valor_maximo)
else:
  print("La lista está vacía.")