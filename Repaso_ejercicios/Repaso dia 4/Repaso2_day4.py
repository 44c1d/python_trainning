# EJERCICIO 2 – Elegir un ganador de una lista
# Creá una lista con 3 nombres de personas (inventados por vos).

# Usá random.choice() para elegir una persona al azar como ganadora.

# Mostrar:

# text
# Participantes: [lista completa]
# El ganador es: [nombre]
import random

Participantes = ["Juan", "Pedro", "María"]

Ganador = random.choice(Participantes)
if Ganador == "Juan":
   print(f"Y el ganador es....{Ganador}!!!Felicidades!!!")
elif Ganador == "Pedro":
   print(f"Y el ganador es....{Ganador}!!!Felicidades!!!")
elif Ganador == "María":
   print(f"Y la ganadora es....{Ganador}!!!Felicidades!!!")      