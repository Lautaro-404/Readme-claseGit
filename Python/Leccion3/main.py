# OPERADORES ARITMETICOS
# Operador de suma
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print(f"El resultado de la suma es: {suma}") # Otra forma de imprimir la variable

# Operador de resta
resta = operandoA - operandoB
print(f'El resultado de la resta: {resta}')

# Operador de multiplicacion
multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion: {multiplicacion}')

# Operador de division
division = operandoA / operandoB
print(f'El resultado de la division es: {division}')
division = operandoA // operandoB # Division entera
print(f'El resultado de la division (int) es: {division}')

# Operador de modulo
modulo = operandoA % operandoB
print(f'El resultado de la division o residuo (modulo) es: {modulo}')

# Operador de exponente
exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')

# OPERADORES ASIGNACION Y COMPARACION
# Operador de asignacion
miVariable3 = 10
print('Asignamos un valor a la variable: ', miVariable3)

# Operador de reasignacion
miVariable3 = miVariable3 + 1
print('Incremento por reasignacion: ', miVariable3)

# Otro metodo para reducir la sintaxis al reasignar
miVariable3 += 1
print('Otro incremento por reasignacion: ', miVariable3)

# Mas ejemplos con otros operadores aritmeticos

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print('Resta por reasignacion: ', miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print('Multiplicacion por reasignacion: ', miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print('Division por reasignacion: ', miVariable3)

# Operador de comparacion
d = 4
b = 2
resultado = d == b # Comprobamos si son iguales
print('Es verdadero que d es igual a b? ', resultado)

# Operador diferente
resultado = d != b
print('Es verdadero que d es diferente a b? ', resultado)

# Operador mayor que
resultado = d > b
print('Es verdadero que d es mayor que b? ', resultado)

# Operador menor que
resultado = d < b
print('Es verdadero que d es menor que b? ', resultado)

# Operador menor o igual que
resultado = d <= b
print('Es verdadero que d es menor o igual que b? ', resultado)

# Operador mayor o igual que
resultado = d >= b
print('Es verdadero que d es mayor o igual que b? ', resultado)