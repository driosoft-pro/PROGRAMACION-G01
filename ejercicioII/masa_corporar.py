# Programa que calcula el índice de masa corporal (IMC) de una persona
print("Cálculo del índice de masa corporal (IMC)")

# Solicitar el peso de la persona
peso = float(input("Ingrese el peso en kilogramos: "))
if peso < 0:
    print("El dato ingresado debe ser positivo.")
    exit()

# Solicitar la altura de la persona
altura = float(input("Ingrese la altura en metros: "))
if altura < 0:
    print("El dato ingresado debe ser positivo.")
    exit()

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el IMC
print(f"El índice de masa corporal (IMC) es: {imc:.2f} kg/m²")

# Interpretar el IMC
print("Interpretación del IMC")