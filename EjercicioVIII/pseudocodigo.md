# Ejercicio VIII
´´´
Diseñe e implemente un programa que permita generar una matriz de nxm, donde cada elemento de la matriz es un número aleatorio entre un número mínimo y un número máximo. Productos:

Pseudocódigo.
Código en Python.
Nota: No usar algún paquete Python especializado.
´´´

## Descripción
´´´
Este ejercicio consiste en implementar un programa en Python que permite al usuario generar una matriz de tamaño `nxm`. Cada elemento de la matriz es un número aleatorio entre un valor mínimo y un valor máximo especificados por el usuario. El programa muestra la matriz generada.
´´´

## Pseudocódigo
´´´
    Inicio
        // Solicitar las dimensiones de la matriz al usuario
        Escribir "Ingrese el número de filas (n):"
        Leer n
        Escribir "Ingrese el número de columnas (m):"
        Leer m

        // Solicitar el rango de números aleatorios
        Escribir "Ingrese el valor mínimo para los números aleatorios:"
        Leer minimo
        Escribir "Ingrese el valor máximo para los números aleatorios:"
        Leer maximo

        // Inicializar una matriz vacía de tamaño nxm
        matriz = []

        // Llenar la matriz con números aleatorios entre minimo y maximo
        Para i desde 0 hasta n - 1 Hacer
            fila = []
            Para j desde 0 hasta m - 1 Hacer
                fila[j] = Aleatorio(minimo, maximo)
            Fin Para
            matriz[i] = fila
        Fin Para

        // Mostrar la matriz generada
        Escribir "Matriz generada:"
        Para i desde 0 hasta n - 1 Hacer
            Escribir matriz[i]
        Fin Para
    Fin
´´´