# Ejercicio IX
´´´
Diseñe e implemente un programa que permita sumar dos matrices matriz de nxn. Productos:

Pseudocódigo.
Código en Python.
Nota: No usar algún paquete Python especializado.
´´´

## Descripción
´´´
Este programa en Python permite al usuario ingresar dos matrices cuadradas de tamaño nxn. El programa realiza la suma de las dos matrices elemento por elemento y muestra la matriz resultante. No se utilizan paquetes especializados de Python para realizar la suma de matrices.
´´´

## Pseudocódigo
´´´
    Inicio
        // Solicitar la dimensión de las matrices al usuario
        Escribir "Ingrese la dimensión de las matrices (n):"
        Leer n

        // Inicializar las matrices A y B con tamaño nxn
        matriz_A = crear_matriz(n)
        matriz_B = crear_matriz(n)

        // Llenar la matriz A con valores ingresados por el usuario
        Escribir "Ingrese los valores para la matriz A:"
        llenar_matriz(matriz_A)

        // Llenar la matriz B con valores ingresados por el usuario
        Escribir "Ingrese los valores para la matriz B:"
        llenar_matriz(matriz_B)

        // Crear la matriz resultante C con tamaño nxn
        matriz_C = crear_matriz(n)

        // Sumar las matrices A y B elemento por elemento
        Para i desde 0 hasta n - 1 Hacer
            Para j desde 0 hasta n - 1 Hacer
                matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]
            Fin Para
        Fin Para

        // Mostrar la matriz resultante C
        Escribir "La matriz resultante C es:"
        mostrar_matriz(matriz_C)
    Fin

    // Función para crear una matriz de nxn
    crear_matriz(n)
        // Inicializar una matriz vacía de tamaño nxn
        matriz = []
        Para i desde 0 hasta n - 1 Hacer
            fila = []
            Para j desde 0 hasta n - 1 Hacer
                fila[j] = 0 // Inicializar los elementos con 0
            Fin Para
            matriz[i] = fila
        Fin Para
        Devolver matriz

    // Función para llenar una matriz con valores ingresados por el usuario
    llenar_matriz(matriz)
        Para i desde 0 hasta n - 1 Hacer
            Para j desde 0 hasta n - 1 Hacer
                Escribir "Ingrese el valor para el elemento [" + i + "][" + j + "]:"
                Leer matriz[i][j]
            Fin Para
        Fin Para

    // Función para mostrar una matriz
    mostrar_matriz(matriz)
        Para i desde 0 hasta n - 1 Hacer
            Escribir matriz[i]
        Fin Para
´´´
