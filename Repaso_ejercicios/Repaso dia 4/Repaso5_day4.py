# EJERCICIO 2 – Ruleta de colores
# Creá una lista con 4 colores ("rojo", "verde", "azul", "amarillo").

# Preguntar al usuario:

# "Adiviná qué color va a salir: "

# La computadora elige un color al azar con random.choice().

# Reglas:

# Si el usuario adivina exactamente el color → "Ganaste 10 puntos"

# Si el usuario elige "azul" y sale "rojo" → "Casi, pero no"

# Si el usuario elige "verde" y sale "amarillo" → "Seguí participando"

# Cualquier otro caso → "Perdiste"

# Mostrar:

# text
# Tu elección: [color]
# Color sorteado: [color]
# Resultado: [mensaje]
import random

colors = ["rojo", "verde", "azul", "amarillo"]

user_color = input("Adiviná qué color va a salir (Rojo,Verde,Azul,Amarillo): "  ).lower().strip()

random_color = random.choice(colors)

if user_color not in colors:
    print (f"{user_color.capitalize()} no es un color válido")
else:
    if user_color == random_color:
        print(f"Tu elección: {user_color.capitalize()}")
        print(f"Color sorteado: {random_color.capitalize()}")
        print("Ganaste 10 puntos")
    elif user_color == "azul" and random_color == "rojo":
        print(f"Tu elección: {user_color.capitalize()}")
        print(f"Color sorteado: {random_color.capitalize()}")
        print("Casi, pero no")
    elif user_color == "verde" and random_color == "amarillo":
        print(f"Tu elección: {user_color.capitalize()}")
        print(f"Color sorteado: {random_color.capitalize()}")
        print("Seguí participando")    


