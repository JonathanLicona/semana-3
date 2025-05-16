
calificaciones = []
while True:
    calificacion = input("Ingrese una calificación (o 'fin' para terminar): ")
    if calificacion.lower() == 'fin':
        break
    try:
        calificacion = float(calificacion) 
        calificaciones.append(calificacion)
    except ValueError:
        print("Entrada inválida. Ingrese un número o 'fin'.")
if len(calificaciones) > 0:
    suma = 0
    for calificacion in calificaciones:
        suma += calificacion 
    promedio = suma / len(calificaciones)
    print("El promedio de las calificaciones es:", promedio)
else:
    print("No se ingresaron calificaciones.")