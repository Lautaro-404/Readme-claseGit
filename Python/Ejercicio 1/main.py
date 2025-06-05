# Ejercicio: Número par o impar
# 1. Solicitamos que el usuario ingrese un número
# 2. Este se asigna a una variable
# 3. Utilizaremos la estructura ‘if else’
# 4. La formula: <num> % 2 == 0 Esta operación nos dice si es un número par
# 5. Si es True imprimimos que es par
# 6. Si es False imprimimos que es impar

num = int(input('Ingrese un numero: '))
print(f'El residuo de la division es: {num % 2}')
if num % 2 == 0:
    print(f'El numero {num} es PAR')
else:
    print(f'El numero {num}  IMPAR')