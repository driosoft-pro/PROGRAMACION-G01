# Ejercicio II
´´´
Desarrolle un programa en Python que permita calcular el índice de masa corporal de una persona (los datos deben ser ingresados por el usuario). Desarrolle el pseudocódigo, el diagrama de flujo y el código.
´´´

## Descripción
Este pseudocódigo describe los pasos necesarios para calcular el índice de masa corporal (IMC) de una persona ingresando su peso y altura.

## Pseudocódigo
´´
    Inicio
        // Declarar variables Declarar peso como Real Declarar altura como Real Declarar imc como Real
        
        // Ingresar los datos de la persona
        Escribir "Ingrese el peso en kilogramos:"
        Leer peso
        Escribir "Ingrese la altura en metros:"
        Leer altura

        // Calcular el IMC
        imc <- peso / (altura * altura)

        // Mostrar el IMC
        Escribir "El índice de masa corporal (IMC) es:", imc
    Fin
´´´