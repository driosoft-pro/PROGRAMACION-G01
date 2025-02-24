# Ejercicio III
´´´
Desarrolle un programa en Python que permita calcular el salario neto de un trabajador ingresando el número de horas trabajadas, la tarifa horaria y la tasa de impuestos. Desarrolle el pseudocódigo, el diagrama de flujo y el código.

´´´

## Descripción
Este pseudocódigo describe los pasos necesarios para calcular el salario neto de un trabajador. El programa solicita al usuario ingresar el número de horas trabajadas, la tarifa horaria y la tasa de impuestos. A partir de estos datos, calcula el salario bruto, aplica la tasa de impuestos y muestra el salario neto.

## Pseudocódigo
´´´
    Inicio  
        // Solicitar el número de horas trabajadas  
        Escribir "Ingrese el número de horas trabajadas:"  
        Leer horas_trabajadas  

        // Solicitar la tarifa horaria  
        Escribir "Ingrese la tarifa horaria:"  
        Leer tarifa_horaria  

        // Solicitar la tasa de impuestos (en porcentaje)  
        Escribir "Ingrese la tasa de impuestos (%):"  
        Leer tasa_impuestos  

        // Calcular el salario bruto  
        salario_bruto = horas_trabajadas * tarifa_horaria  

        // Calcular el impuesto  
        impuesto = salario_bruto * (tasa_impuestos / 100)  

        // Calcular el salario neto  
        salario_neto = salario_bruto - impuesto  

        // Mostrar el salario neto  
        Escribir "El salario neto es:", salario_neto  
    Fin  
´´´