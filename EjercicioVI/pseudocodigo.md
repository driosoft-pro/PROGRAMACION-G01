# Ejercicio V
´´´
Implemente un programa que:
    1. Genere un número alearorio entre 1 y 10 (no muetre el número).
    2. Muetre si el número es par o impar.
    3. Intente el adivinar el número (ingrese un numero entre 1 y 10).
    4. Evalúe si lo adivinó, En caso negativo, muestre el número que debía adibinar.
´´´

## Descripción
Este pseudocódigo describe los pasos necesarios para implementar un programa que genera un número aleatorio entre 1 y 10, determina si es par o impar, permite al usuario intentar adivinar el número y evalúa si lo adivinó, mostrando el número correcto en caso de no adivinarlo.

## Pseudocódigo
´´´
    Inicio  
        // Generar un número aleatorio entre 1 y 10
        numero_aleatorio = Aleatorio(1, 10)

        // Determinar si el número es par o impar
        Si numero_aleatorio % 2 == 0 Entonces
            Escribir "El número es par."
        Sino
            Escribir "El número es impar."
        Fin Si

        // Solicitar al usuario que intente adivinar el número
        Escribir "Intente adivinar el número (entre 1 y 10):"
        Leer intento

        // Evaluar si el usuario adivinó el número
        Si intento == numero_aleatorio Entonces
            Escribir "¡Felicidades! Adivinaste el número."
        Sino
            Escribir "Lo siento, no adivinaste. El número era:", numero_aleatorio
        Fin Si
    Fin  
´´´