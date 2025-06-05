# Clase 2 de Python

# Variable con Referencia
a: str = "Hola alumnos" # class str

print(type(a)) #Imprimimos el tipo de variable

a = 10.78 # class float

print(type(a))

a = True # class bool

print(type(a))

# Tipos int, float, String, Bool
x = 10 # class int
print(x)
print(type(x))

x = 14.5 # class float
print(x)
print(type(x))

x = "Hola Alumnos" # class str
print(x)
print(type(x))

x = True # class bool
print(x)
print(type(x))

x = False # class bool
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "Hernan Cattaneo:"
caracteristicas = "The best Tech DJ"
print("Mi grupo favorito es: "+miGrupoFavorito+" "+caracteristicas) # Concatenamos con el operador +
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas) # Concatenamos con la ,

# Que pasa al sumar dos strings
numero1 = "7"
numero2 = "8"
print(numero1 + numero2) # No suma, concatena las dos variables
print(int(numero1) + int(numero2)) # Cerramos las variables  y la transformamos a numeros enteros con int

# Tipos Boleanos (bool)
miBooleano = 1 > 2 # False
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

miBooleano = 3 > 2 # True
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# Funcion input
resultado = input("Digite un numero: ") # Regresa un dato tipo string
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
