import random

# random_interger = random.randint(1, 10)

# print(random_interger)

# random_n_0_to_1 = random.random() *10
# print(random_n_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

#Crear un juego de cara o cruz

cara_o_seca = random.randint(0,1)
# if cara_o_seca == 0:
#     print("Cara")
# else:
#     print("Seca")


#Quien paga la cuenta?

amigos= ["Lucas", "Sergio", "Fernanda", "Seba","Dari", "Maga", "Mariano"]

# random_amigos = random.randint(0, 6)

# if random_amigos == 0:
#     print(amigos[0])
# elif random_amigos == 1:
#     print(amigos[1])
# elif random_amigos == 2:
#     print(amigos[2])
# elif random_amigos == 3:
#     print(amigos[3])
# elif random_amigos == 4:
#     print(amigos[4])
# elif random_amigos == 5:
#     print(amigos[5])    
# else:
#     print(amigos[6])                    

# print(random.choice(amigos))

# random = random.randint(0,5)
# print(amigos[random]) 


# #Juego de la botellita

# chicos= ["Gustavo", "Marcelo", "Carlos", "Gastón","Facundo"]

# chicas = ["Maria", "Clara", "Paula", "Lucia", "Florencia"]



# print(f"{random.choice(chicos)} y {random.choice(chicas)}")


# #Dados del catán (ciudades y caballeros)

# primer_dado = ["*","**","***","****", "*****", "******"]

# segundo_dado = ["*","**","***","****", "*****", "******"]

# dados_barcos = ["barco verde", "barco amarillo", "barco azul", "barco negro", "barco negro", "barco negro"]
# print(random.choice(primer_dado))

# print(random.choice(segundo_dado))

# print(random.choice(dados_barcos))

#Checho es...

checho = ["gato revirado","gato naranjoso", "gato mio", "checho", "miau miau"]

print(f"Checho es un {random.choice(checho)}")