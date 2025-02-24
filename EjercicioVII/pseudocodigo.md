# Ejercicio VII
´´´
3. Diseñe e implemente un programa en Python que tenga las siguientes características:

- Genere dos vectores aleatorios 
de un tamaño indicado por el usuario (cada elemento debe ser un número aleatorio que puede estar entre 1 y 100).
- Sume los dos vectores.
- Muestre los vectores y el resultado.

No use librerías especiales.
´´´

## Descripción
´´´
Este ejercicio consiste en implementar un programa en Python que permite al usuario generar dos vectores de tamaño especificado. Cada elemento de los vectores es un número aleatorio entre 1 y 100. El programa suma los vectores y muestra los vectores generados junto con el resultado de su suma.
´´´

## Pseudocódigo
´´´
    Inicio
        // Solicitar el tamaño de los vectores al usuario
        Escribir "Ingrese el tamaño de los vectores:"
        Leer tamanio

        // Inicializar vectores vacíos
        vector1 = []
        vector2 = []
        suma_vectores = []

        // Llenar los vectores con números aleatorios entre 1 y 100
        Para i desde 0 hasta tamanio - 1 Hacer
            vector1[i] = Aleatorio(1, 100)
            vector2[i] = Aleatorio(1, 100)
            suma_vectores[i] = vector1[i] + vector2[i]
        Fin Para

        // Mostrar los vectores y su suma
        Escribir "Vector 1:", vector1
        Escribir "Vector 2:", vector2
        Escribir "Suma de vectores:", suma_vectores
    Fin
´´´