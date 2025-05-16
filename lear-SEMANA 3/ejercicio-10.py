def palindromo(texto):

    texto = texto.replace(" ", "").replace(",", "").replace(".", "")

    texto = texto.lower()

    return texto == texto[::-1]

texto = "Anita lava la tina"
if palindromo(texto):
    print(f"'{texto}' es un palíndromo")
else:
    print(f"'{texto}' no es un palíndromo")