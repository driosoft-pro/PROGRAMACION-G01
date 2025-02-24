# Constante de pi
pi = 3.14159

print("Programa para calcular el volumen de un cilindro")

# Solicitar el radio del cilindro
radio = float(input("Ingrese el radio del cilindro en metros: "))
if radio < 0:
    print("El dato ingresado debe ser positivo.")
    exit()

# Solicitar la altura del cilindro
altura = float(input("Ingrese la altura del cilindro en metros: "))
if altura < 0:
    print("El dato ingresado debe ser positivo.")
    exit()

# Calcular el volumen del cilindro
volumen = pi * radio**2 * altura

# Mostrar el volumen
print(f"El volumen del cilindro es: {volumen:.2f} metros cúbicos")

print("Fin del programa")