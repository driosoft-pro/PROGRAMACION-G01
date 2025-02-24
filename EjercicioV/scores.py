# Programa para determinar la calificación de un examen
print("Programa para determinar la calificación de un examen")

# Solicitar la puntuación del examen
score = float(input("Ingrese la puntuación del examen: "))
if score < 0 or score > 100:
    print("El dato ingresado debe estar entre 0 y 100.")
    exit()

# Determinar la nota correspondiente
if score < 60:
    nota = 'F'
elif score >= 60 and score < 70:
    nota = 'D'
elif score >= 70 and score < 80:
    nota = 'C'
elif score >= 80 and score < 90:
    nota = 'B'
elif score >= 90:
    nota = 'A'

# Mostrar la nota
print(f"La nota correspondiente es: {nota}")

