# EJERCICIO 1 – Simulador de lotería simple
# Un sorteo tiene 3 números ganadores (fijos, los ponés vos en una lista).

# Preguntar al usuario:

# "Elegí un número entre 1 y 10: "

# Reglas:

# Si el número está entre los ganadores → "Ganaste un premio chico"

# Si el número es el primero de la lista de ganadores → "Ganaste el premio grande"

# Si no está entre los ganadores → "Seguí participando"

# Mostrar al final:

# text
# Números ganadores: [X, Y, Z]
# Tu número: [N]
# Resultado: [mensaje]
# Bonus: Usá random.shuffle() para mezclar los números ganadores antes de mostrarlos (investigá cómo funciona).
import random

number = int(input("Elegí un número entre 1 y 10: "))

list_numbers = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(list_numbers)

winners = list_numbers[:3]

if number <1:
    print(number)
elif number >10:
    print(number)
else:

    if number == winners[0]:
        print(f"Números ganadores: {winners}")
        print(f"Tu número: {number}")
        print("Resultado:Ganaste el premio grande ")
        
    elif number in winners:
        print(f"Números ganadores: {winners}")
        print(f"Tu número: {number}")
        print("Resultado:Ganaste un premio chico ")
        
    else:
        print("Seguí participando")     



