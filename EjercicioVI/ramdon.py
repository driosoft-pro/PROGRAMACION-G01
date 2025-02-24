import random

# Programa para adivinar un número aleatorio
print("Programa para adivinar un número aleatorio")

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Determinar si el número es par o impar
if numero_aleatorio % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Solicitar al usuario que intente adivinar el número
intento = int(input("Intente adivinar el número (entre 1 y 10): "))
if intento < 1 or intento > 10:
    print("El dato ingresado debe estar entre 1 y 10.")
    exit()

# Evaluar si el usuario adivinó el número
if intento == numero_aleatorio:
    print("¡Felicidades! Adivinaste el número.")
else:
    print(f"Lo siento, no adivinaste. El número era: {numero_aleatorio}")

