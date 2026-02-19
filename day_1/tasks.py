#Printing


print("Hello World!")

# Ejercicios de printing del curso.

#1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
# 2. Knead the dough for 10 minutes.
# 3. Add 3g of Salt.
# 4. Leave to rise for 2 hours.
# 5. Bake at 200 degrees C for 30 minutes.

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#String Manipulation
 #Salto de linea \n
print("Hello World!\nHelloworld!\nHello World!")

#Ejemplo de string manipulation con el ejercicio de la receta de pan

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")

#Concatenacion de strings
print("Hola " + "Tano")
print("Hola" +" " + "Tano")
print("Hola" + " Tano")


#Debugging Pratice - ejercicio del curso
### Fix the code below 👇

# print(Notes from Day 1") error de sintaxis, falta la comilla al inicio de la cadena
#  print("The print statement is used to output strings") error de indentacion, el print no debe estar indentado
# print("Strings are strings of characters" error de sintaxis, falta el parentesis al final de la cadena
# priint("String Concatenation is done with the + sign") error de sintaxis, la palabra print esta mal escrita
# print(("New lines can be created with a \ and the letter n") error de sintaxis, hay un parentesis de mas al inicio de la cadena.

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")


#Input function

input("Como te llamas?: ")


#problema:agregar un input de nombre que tenga respuesta de saludo y un signo de exclamacion al final.

print("Hola " + input("¿Como te llamas?: ") + "!") 

#Variables

nombre = input("¿Como te llamas?: ")
print("Hola " + nombre + "!")

#Problema: imprimir la cantidad de caracteres que tiene el nombre ingresado por el usuario.

nombre = input("¿Como te llamas?: ")
print("Hola " + nombre + "!")
print(len(nombre))# solucion creada por mi

print(len(input("¿Como te llamas?: "))) # solucion creada por el curso, es mas eficiente porque no necesita una variable intermedia para almacenar el nombre.   

#Pensandolo bien, creo que la solucion del curso no está mal, pero no esta el saludo...creo que puedo agregarle eso 

nombre = input("¿Como te llamas?: ")
saludo = "Hola " + nombre + "!"
print(saludo + "Tu nombre tiene " + str(len(nombre)) + " caracteres.")


#Ejercicio de Variables del curso

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
# Write 3 lines of code to switch the contents of the variables. 
# You are not allowed to type the words "milk" or "juice". You are only allowed to use 
# variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"
glass1, glass2 = glass2, glass1
print("Glass1: "+ glass1 + " " + "glass2: " + glass2)
