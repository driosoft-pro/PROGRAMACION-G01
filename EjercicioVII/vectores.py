import random  # Importamos el módulo para generar números aleatorios

# Paso 1: Solicitar el tamaño de los vectores
n = int(input("Ingrese el tamaño de los vectores: "))

# Paso 2: Inicializar los vectores vacíos
vector1 = []
vector2 = []
suma_vectores = []

# Paso 3: Llenar los vectores con números aleatorios entre 1 y 100
for i in range(n):
    num1 = random.randint(1, 100)  # Generar número aleatorio para vector1
    num2 = random.randint(1, 100)  # Generar número aleatorio para vector2
    vector1.append(num1)
    vector2.append(num2)
    suma_vectores.append(num1 + num2)  # Sumar los elementos correspondientes

# Paso 4: Mostrar los vectores y su suma
print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Suma de vectores:", suma_vectores)