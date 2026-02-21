#Python Primitive Data Types

#Subscripting: Es la manera de sacar de un string un valor especifico basa en su posicion. 
# donde el primer caracter de un string tiene la posicion 0, el segundo caracter tiene la 
# posicion 1, y asi sucesivamente.

print("hello"[0])

#String Concatenation: Es la manera de unir dos o mas strings usando 
# el operador +.

print("Hola" + " " + "Tano" )


#Interger es un tipo de dato que representa numeros enteros, es decir,
# numeros sin decimales.

interger = 123
print(interger)

interger1 = 123

#Large numbers: Python tiene la capacidad de manejar numeros muy grandes s
# sin necesidad de usar una libreria externa.

large_number = 123_456_789
print(large_number)

#FLoat es un tipo de dato que representa numeros con decimales.
float_number = 3.14159
print(float_number) 

# boolean es un tipo de dato que representa valores de verdad, es decir,
# valores que pueden ser verdaderos o falsos. En Python, los booleanos 
# se representan con las palabras clave True y False.

boolean_true = True
boolean_false = False   
print(boolean_true)
print(boolean_false)    

#para verificar que tipeo de dato es una variable, 
# podemos usar la funcion type().

print(type("hello"))
print(type(123))
print(type(3.14))
print(type(True))



#ejercicio : HAcer que esta linea de codigo funcione

nombre = input("como te llamas?: ")

nro_letras = len(nombre)

print("Hola " + nombre + "! Tu nombre tiene " + str(nro_letras) + " letras.")