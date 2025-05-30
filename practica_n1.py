# Se busca crear un juego para adivinar un numero generado de manera
# random, para ello deberemos implementar lo siguiente:
# Variables
# Bucles
# Condicionales
# Operadores Logicos
# Operadores Aritmeticos
# Asignación de valores
# Input
# Print

# Requisitos a cumplir:
# El juego termina cuando el Jugador acierta el numero o hace 5 intentos.
# Cuando se pide ingresar el número se le debe indicar al  jugador el rango máximo y mínimo.
# Si el jugador falla, se debe indicar si el número es mayor o menor.
# Al perder se le enviara un mensaje indicandole que ha perdido y cual era el número.

# Como ayuda inicial les voy a brindar las dos primeras lineas de su codigo
import random
numero_secreto = random.randint(1, 50)
acierto = False

print(numero_secreto)

for intento in range(5):
    numero_ingresado = float(input(f"Intento {intento + 1}.Ingrese el numero entre el rango 1-50: "))
    # if 1 < numero_ingresado > 50:
    #     print("El número debe estar entre 1 y 50. Intenta de nuevo.")

    if numero_ingresado == numero_secreto:
        print("Acertaste!")
        acierto = True
        break
    elif numero_ingresado > numero_secreto:
        print(f"El número secreto es menor que {numero_ingresado}")
    elif numero_ingresado < numero_secreto:
        print(f"El número secreto es mayor que {numero_ingresado}")

if acierto == False:
    print(f"Intentos acabados. El número secreto era: {numero_secreto}")