edad = int(input("ingresa tu edad: "))
if edad > 0 and edad <=12:
    print("eres un niño")
elif edad > 12 and edad < 18:
    print("eres adolecente")
elif edad >=18 and edad < 60:
    print("eres mayor de edad")
else:
    print("eres aciano")
    