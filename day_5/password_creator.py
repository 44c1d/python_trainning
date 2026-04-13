# import random

# password= ""

# letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# numeros = ["0","1","2","3","4","5","6","7","8","9"]

# caracteres_esp = ["!","#","$","%","&","(",")","*","+"]

# print("Bienvenidos a mi generador de contraseñas!")


# nro_letras = int(input("¿Cuántas letras querés que haya en tu contraseña?\n"))

# nro_caract = int(input("¿Cuántos caracteres querés que haya en tu contraseña?\n"))

# nro_numeros = int(input("¿Cuántas números querés que haya en tu contraseña?\n"))

 

# # 

# # easy level
# for let in range (0,nro_letras):
#     password +=  random.choice(letras)
   

# for num in range (0,nro_numeros):
#     password += random.choice(numeros)
  
    
    
# for carac in range (0,nro_caract) :
#     password +=  random.choice(caracteres_esp)
    

  
# print(password)



    # Hard level

import random

password= []

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numeros = ["0","1","2","3","4","5","6","7","8","9"]

caracteres_esp = ["!","#","$","%","&","(",")","*","+"]

print("Bienvenidos a mi generador de contraseñas!")


nro_letras = int(input("¿Cuántas letras querés que haya en tu contraseña?\n"))

nro_caract = int(input("¿Cuántos caracteres querés que haya en tu contraseña?\n"))

nro_numeros = int(input("¿Cuántas números querés que haya en tu contraseña?\n"))

 




for let in range (0,nro_letras):
    password +=  random.choice(letras)
   

for num in range (0,nro_numeros):
    password += random.choice(numeros)
  
    
    
for carac in range (0,nro_caract) :
    password +=  random.choice(caracteres_esp)





random.shuffle(password)

F_password = ""

for clave in password:
    F_password += clave



print(f"Tu nueva clave es ésta: {F_password}")


    

  
