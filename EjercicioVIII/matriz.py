# Importar el módulo random para generar números aleatorios
import random

# Solicitar al usuario el número de filas (n) de la matriz
n = int(input("Ingrese el número de filas (n): "))

# Solicitar al usuario el número de columnas (m) de la matriz
m = int(input("Ingrese el número de columnas (m): "))

# Solicitar al usuario el valor mínimo para los números aleatorios
minimo = int(input("Ingrese el valor mínimo para los números aleatorios: "))

# Solicitar al usuario el valor máximo para los números aleatorios
maximo = int(input("Ingrese el valor máximo para los números aleatorios: "))

# Inicializar una lista vacía para almacenar la matriz
matriz = []

# Llenar la matriz con números aleatorios
for i in range(n):  # Recorrer cada fila
    fila = []  # Inicializar una lista vacía para la fila actual
    for j in range(m):  # Recorrer cada columna de la fila actual
        # Generar un número aleatorio entre minimo y maximo y agregarlo a la fila
        fila.append(random.randint(minimo, maximo))
    # Agregar la fila completada a la matriz
    matriz.append(fila)

# Mostrar la matriz generada
print("\nMatriz generada:")
for fila in matriz:  # Recorrer cada fila de la matriz
    print(fila)  # Imprimir la fila actual