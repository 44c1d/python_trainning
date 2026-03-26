# # Día 1 (variables, inputs, prints)
# # Ejercicio:
# # Preguntar:

# # Ciudad de nacimiento

# # Nombre de mascota

# # Mostrar:
# # "Tu nombre de usuario podría ser: [ciudad][mascota]"
# # Ejemplo: "BuenosAiresLuna"

# # Bonus: que el resultado se muestre todo en minúsculas y sin espacios.

ciudad= input("Dame tu ciudad de nacimiento").lower().strip()

mascota= input("Decime el nombre de tu mascota").lower().strip() 

print(ciudad+mascota)


# # 🔹 Día 2 (tipos de datos, operadores)
# # Ejercicio:
# # Pedir un número de 3 cifras.
# # Calcular y mostrar el producto de sus dígitos (multiplicación, no suma).

# # Ejemplo:
# # Ingresa 235 → 2 * 3 * 5 = 30

# # Bonus: si el número tiene menos de 3 cifras, que avise "Número inválido".
# numero = input("Ingresá un numero de tres cifras: ")

if len(numero) ==3 and numero.isdigit():
    digito1= int(numero[0])
    digito2= int(numero[1])
    digito3= int(numero[2])
    producto= digito1*digito2*digito3
    print(f"El producto de los digitos ingresados es: {producto}")
else:
    print("Numero correcto")

   




# # 🔹 Día 3 (if/elif/else, lógica)
# Ejercicio:
# Simulá un sistema de acceso:

# Preguntar: "¿Tenés entrada? (sí/no)"

# Si tiene entrada, preguntar: "¿Sos mayor de edad? (sí/no)"

# Si tiene entrada y es mayor → "Podés pasar"

# Si tiene entrada pero es menor → "Pasá con un adulto"

# Si no tiene entrada → "No podés pasar"

# Bonus: aceptá respuestas como "s", "si", "sí", "no", "n" usando .lower() y condiciones flexibles.

pregunta1= input("Tenes entrada?: ")

opciones_si= ["si", "sí","s"]
opciones_no= ["no","nó","n"]

if pregunta1 in opciones_si:
    pregunta2 = input("¿Sos mayor de edad? (sí/no)")
    if pregunta2 in opcion_si:
        pregunta3= input("Podés pasar")
    elif pregunta2 in opciones_no:
        print("Pasá con un adulto")   
else:
     print("No podés pasar")         

