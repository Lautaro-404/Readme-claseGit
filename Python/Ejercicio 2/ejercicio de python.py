# Ejercicio 4: Suponga que se tiene un conjunto de calificaciones de un
# grupo de 10 alumnos. Realizar un algoritmo para calcular
# la calificacion promedio y la calificacion mas baja de todo el grupo.

# Inicialización de variables
suma = 0
calificacion_baja = 99999

# Bucle para leer 10 calificaciones
for i in range(1, 11):
    calificacion = float(input(f"{i}. Digite una calificación: "))

    # Sumar la calificación a la suma total
    suma += calificacion

    # Determinar la calificación más baja
    if calificacion < calificacion_baja:
        calificacion_baja = calificacion

# Calcular el promedio
calificacion_promedio = suma / 10

# Mostrar resultados
print(f"La calificación promedio es: {calificacion_promedio}")
print(f"La calificación más baja es: {calificacion_baja}")

