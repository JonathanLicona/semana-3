def vocales(cadena):
    
    vocales = "aeiouAEIOU"  
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
        return contador

cadena = "Hola, mundo!"
cantidad_vocales = vocales(cadena)
print(f"La cadena '{cadena}' tiene {cantidad_vocales} vocales.")
