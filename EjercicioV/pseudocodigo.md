# Ejercicio V
´´´
El Dr. Suárez imparte una clase de literatura y utiliza la siguiente escala de calificación de 10 puntos para todos sus exámenes:

Test Score          Grade
90 and above        A
80-89               B
70-79               C
60-69               D
Below 60            F

Le ha pedido que escriba un programa que permita a un estudiante introducir la puntuación de un examen y luego la nota correspondiente.

´´´

## Descripción
Este pseudocódigo describe los pasos necesarios para implementar un programa que calcula un score para mostrar una nota dependiendo del valor del score.

## Pseudocódigo
´´´
    Inicio  
        // Solicitar la puntuación del examen
        Escribir "Ingrese la puntuación del examen:"
        Leer score

        // Determinar la nota correspondiente
        Si score < 60 Entonces
            nota = 'F'
        Sino Si score >= 60 y score < 70 Entonces
            nota = 'D'
        Sino Si score >= 70 y score < 80 Entonces
            nota = 'C'
        Sino Si score >= 80 y score < 90 Entonces
            nota = 'B'
        Sino Si score >= 90 Entonces
            nota = 'A'
        Fin Si

        // Mostrar la nota
        Escribir "La nota correspondiente es:", nota
    Fin  
´´´