
def contar_letra(palabra, letra):

  return palabra.count(letra)

palabra = "Python es un lenguaje de programación"
letra = "n"
cantidad = contar_letra(palabra, letra)
print(f"La letra '{letra}' aparece {cantidad} veces en la palabra '{palabra}'") 
