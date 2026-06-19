import random

# Esta es una lista de las palaras que se sortearan en el juego 
palabras = ["python", "computadora", "programacion", "universidad", "teclado"]

# con esto mediante la libreria random se escoge al azar una palabra de la lista de arriba
palabra = random.choice(palabras)

# Aqui creo una lista con los guiones correspondientes a cada letra que contenga la palabra seleccionada
oculta = ["_"] * len(palabra)

# Intentos
intentos = 6

# Son los dibujos que saldran en la terminal dependiendo de los intentos que le queden al jugador 
ahorcado = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]

print("=== JUEGO DEL AHORCADO ===")

#Mientras los intentos sean mayores a 0 va a seguir el juego
while intentos > 0 and "_" in oculta:

    print(ahorcado[6 - intentos])
    print("Palabra:", " ".join(oculta))
    print("Intentos restantes:", intentos)

#el .lower convierte todos los caracteres que se ingresen en minusculas 
    letra = input("Ingrese una letra: ").lower()

#Si la letra esta en la palabra, entonces se reemplaza el guion correspondiente por la letra y si no se resta un intento
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
    print(ahorcado[6])
    print("Has perdido.")
    print("La palabra era:", palabra)