# Programa que sumar dos matrices de n cantidades
print("Suma de matriz")

# Pedimos al usuario que ingrese la dimensión de las matrices (n)
n = int(input("Ingrese la dimensión de las matrices (n): "))

# Creamos las matrices A y B, inicializadas con ceros
matriz_A = []
for i in range(n):
    fila = [0] * n  # Crea una fila de n ceros
    matriz_A.append(fila)

matriz_B = []
for i in range(n):
    fila = [0] * n  # Crea una fila de n ceros
    matriz_B.append(fila)

# Pedimos al usuario que ingrese los valores para la matriz A
print("Ingrese los valores para la matriz A:")
for i in range(n):
    for j in range(n):
        matriz_A[i][j] = int(input(f"Ingrese el valor para el elemento [{i}][{j}]: "))

# Pedimos al usuario que ingrese los valores para la matriz B
print("Ingrese los valores para la matriz B:")
for i in range(n):
    for j in range(n):
        matriz_B[i][j] = int(input(f"Ingrese el valor para el elemento [{i}][{j}]: "))

# Creamos la matriz resultante C, inicializada con ceros
matriz_C = []
for i in range(n):
    fila = [0] * n  # Crea una fila de n ceros
    matriz_C.append(fila)

# Sumamos las matrices A y B elemento por elemento
for i in range(n):
    for j in range(n):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]

# Mostramos la matriz resultante C
print("La matriz resultante C es:")
for i in range(n):
    print(matriz_C[i])