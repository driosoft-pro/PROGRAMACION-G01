# Programa para calcular el salario neto
print("Programa para calcular el salario neto")

# Solicitar el número de horas trabajadas
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
if horas_trabajadas < 0:
    print("El dato ingresado debe ser positivo.")
    exit()

# Solicitar la tarifa horaria
tarifa_horaria = float(input("Ingrese la tarifa horaria en dólares: "))
if tarifa_horaria < 0:
    print("El dato ingresado debe ser positivo.")
    exit()

# Solicitar la tasa de impuestos en porcentaje
tasa_impuestos = float(input("Ingrese la tasa de impuestos (%): "))
if tasa_impuestos < 0:
    print("El dato ingresado debe ser positivo.")
    exit()

# Calcular el salario bruto
salario_bruto = horas_trabajadas * tarifa_horaria

# Calcular el impuesto
impuesto = salario_bruto * (tasa_impuestos / 100)

# Calcular el salario neto
salario_neto = salario_bruto - impuesto

# Mostrar el salario neto
print(f"El salario neto es: {salario_neto:.2f} dólares")

# Interpretar el salario neto
print("Fin del programa")