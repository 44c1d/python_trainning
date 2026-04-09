import random


user_choice = input("Piedra, Papel o Tijeras? ").lower().strip()

rta_user = ["piedra","papel", "tijeras"]


computer_choice = random.choice(rta_user)

if user_choice not in rta_user:
    print(f"{user_choice.capitalize()} es inválido. Perdiste!")
else:
    print(f"Elegiste: {user_choice}!")
    print(f"La compu eleigió: {computer_choice}!")
    if user_choice =="piedra" and computer_choice == "tijeras":
        print("Ganaste!")
    elif user_choice =="piedra" and computer_choice == "papel":
        print("Perdiste!")         
    elif user_choice =="piedra" and computer_choice == "piedra":
        print("Empate!")
    elif user_choice =="papel" and computer_choice == "piedra":
        print("Ganaste!")
    elif user_choice =="papel" and computer_choice == "tijeras":
        print("Perdiste!")
    elif user_choice =="papel" and computer_choice == "papel":
        print("Empate!")        
    elif user_choice =="tijeras" and computer_choice == "papel":
        print("Ganaste!")
    elif user_choice =="tijeras" and computer_choice == "piedra":
        print("Perdiste!")
    elif user_choice =="tijeras" and computer_choice == "tijeras":
        print("Empate!")

            


# if juego == "Piedra" and random_juego =="Tijeras": 
#         print("Ganaste!")
#         if juego == "Piedra" and random_juego == "Papel":
#             print ("Perdiste!")
#         elif juego == "Piedra" and random_juego == "Piedra":
#             print("Empate!")
# elif juego == "Papel" and random_juego == "Piedra":
#         print ("Ganaste!")
#         if juego == "Papel" and random_juego == "Tijeras":
#             print("Perdiste!")
#         elif juego == "Papel" and random_juego == "Papel":
#             print("Empate!")
# elif juego == "Tijeras" and random_juego == "Papel":
#         print("Ganaste!")
#         if juego == "Tijeras" and random_juego == "Piedra":
#             print("Perdiste!")
#         elif juego == "Tijeras" and random_juego == "Tijeras":
#             print("Empate!")



