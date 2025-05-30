import random
numero_secreto = random.randint(1, 50)

intentos_restantes = 5
rango_minimo = 1
rango_maximo = 50

print("¡Bienvenido a Adiviná el Número!")
print("Debes adivinar el número secreto entre 1 y 50.")
print("Tenes 5 intentos.\n")

while intentos_restantes > 0:
    print(f"Te quedan {intentos_restantes} intento(s).")
    entrada = input(f"Ingresá un número entre {rango_minimo} y {rango_maximo}: ")
    
    if not entrada.isdigit():
        print("Por favor, ingresa solo números.\n")
        continue

    numero_jugador = int(entrada)

    
    if numero_jugador < rango_minimo or numero_jugador > rango_maximo:
        print("¡Ese número está fuera del rango permitido!\n")
        continue

    
    if numero_jugador == numero_secreto:
        print(f"¡Correcto! Adivinaste el número secreto: {numero_secreto}")
        break
    elif numero_jugador < numero_secreto:
        print("El número secreto es MAYOR que ese.\n")
    else:
        print("El número secreto es MENOR que ese.\n")

    
    intentos_restantes -= 1


if intentos_restantes == 0:
    print(f"\n¡Se acabaron los intentos! El número secreto era {numero_secreto}.")
