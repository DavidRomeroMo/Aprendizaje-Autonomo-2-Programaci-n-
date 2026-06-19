#A continuacion realizare el juego del ahorcado, el cual es un juego de adivinanza de palabras.

import random

def obtener_palabra():
    palabras = ['python', 'programacion', 'ahorcado', 'juego', 'adivinanza']
    return random.choice(palabras)

def jugar_ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra. Tienes", intentos, "intentos.")

    while intentos > 0:
        mostrar_palabra(palabra, letras_adivinadas)
        letra = input("Ingresa una letra: ").lower()        #con lower() se convierte la letra a minuscula para evitar errores de mayusculas y minusculas

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Correcto!")
        else:
            intentos -= 1
            print("¡Incorrecto! Te quedan", intentos, "intentos.")

        if all(letra in letras_adivinadas for letra in palabra):
            print("¡Felicidades! Has adivinado la palabra:", palabra)
            break
    else:
        print("¡Has perdido! La palabra era:", palabra)

    
def mostrar_palabra(palabra, letras_adivinadas):
    palabra_mostrada = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra)
    print("Palabra:", palabra_mostrada)

if __name__ == "__main__":
    jugar_ahorcado()

