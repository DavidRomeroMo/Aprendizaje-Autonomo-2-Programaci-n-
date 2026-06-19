import random

# Esta es una lista de las palaras que se sortearan en el juego 
palabras = ["python", "computadora", "programacion", "universidad", "teclado"]

# con esto mediante la libreria random se escoge al azar una palabra de la lista de arriba
palabra = random.choice(palabras)

# Aqui creo una lista con los guiones correspondientes a cada letra que contenga la palabra seleccionada
oculta = ["_"] * len(palabra)

# Intentos
intentos = 6

print("=== JUEGO DEL AHORCADO ===")

while intentos > 0 and "_" in oculta:

    print("Palabra:", " ".join(oculta))
    print("Intentos restantes:", intentos)

    letra = input("Ingrese una letra: ").lower()

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                oculta[i] = letra
        print("¡Correcto!")
    else:
        intentos -= 1
        print("Letra incorrecta.")

    print()

# Aqui esta el resulta, ya sea si gana o no el jugador 
if "_" not in oculta:
    print("¡Felicidades! Has ganado.")
    print("La palabra era:", palabra)
else:
    print("Has perdido.")
    print("La palabra era:", palabra)