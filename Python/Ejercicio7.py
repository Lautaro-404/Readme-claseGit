# Ejercicio8

suma = 0

for i in range(1, 6):
    print(f"Salario del empleado {i}:")
    horas = float(input("Digite las horas trabajadas: "))
    tarifa = float(input("Digite la tarifa por hora: "))

    salario = horas * tarifa
    print(f"El salario es: ${salario}")

    suma += salario

print(f"La suma de todos los salarios es: ${suma}")
