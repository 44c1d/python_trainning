# EJERCICIO 1 – Lanzamiento de dados (una sola tirada)
# Simulá el lanzamiento de dos dados de 6 caras.

# Preguntar:

# "¿Querés tirar los dados? (si/no): "

# Mostrar:

# text
# Dado 1: [X]
# Dado 2: [Y]
# Suma total: [X+Y]
# Conceptos: random.randint(), if, listas para respuestas.
import random

user =  input("¿Querés tirar los dados? (si/no): ").lower().strip()

user_si = ["si", "s"]

user_no = ["no", "n"]



if user not in user_si and user not in user_no:
    print(f"'{user.capitalize()}' no es una respueta válida.")
elif user in user_no:
    print("Gracias por participar!")
elif user in user_si:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(f"Primer dado: {dado1}\nSegundo dado: {dado2}\n Suma total: {dado1+dado2}" )



     