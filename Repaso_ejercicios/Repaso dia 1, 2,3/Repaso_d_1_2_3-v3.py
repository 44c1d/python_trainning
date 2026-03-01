# Día 1 – Variables, inputs, prints
# Ejercicio: Registro de usuario

# Escribí un programa que:

# Pregunte nombre, edad y ciudad.

# Muestre:

# text
# Usuario: [nombre]
# Edad: [edad]
# Ciudad: [ciudad]
# Además, muestre:

# text
# ¿Sabías que en 10 años vas a tener [edad+10] años?
# Bonus:
# Si la edad es mayor a 100, que muestre "¡Qué privilegio!".
nombre=input("Ingresá tu nombre: ")
edad=int(input("Ingresá tu edad: "))
ciudad=input("Ingresa tu ciudad natal:")

if edad <=99:
   print(f"Nombre: {nombre}\nEdad: {edad}\nCiudad: {ciudad}\n¿Sabías que en 10 años vas a tener {edad+10} años?")
else:
    print("¡Qué privilegio!") 

# 🟨 Día 2 – Operadores y validación
# Ejercicio: ¿El número es par o impar?

# Escribí un programa que:

# Pregunte un número entero.

# Muestre si es par o impar.

# Además, si el número es múltiplo de 4, que muestre "Y además es múltiplo de 4".

# Requisitos:

# Validar que el número sea entero positivo.

# Si no lo es, mostrar "Número inválido".
numero= int(input("Ingrese un número entero: "))
print(f"Número ingresado: {numero}")
if numero <0:
    print("Número inválido")
else:
    print(f"El numero {numero} es positivo")

    if numero %2==0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

    if numero %4 ==0:
        print(f"El numero {numero} multiplo de 4")
    else:
        print(f"El numero {numero} no es multiplo de 4") 

        
        





# 🟩 Día 3 – Control de flujo y lógica
# Ejercicio: Calculadora de índice de masa corporal (IMC) con categorías

# Escribí un programa que:

# Pregunte peso en kg (puede tener decimales) y altura en metros (ej: 1.75).

# Calcule el IMC = peso / altura².

# Muestre el IMC con 2 decimales y la categoría según esta tabla:

# IMC	Categoría
# < 18.5	Bajo peso
# 18.5 – 24.9	Peso normal
# 25 – 29.9	Sobrepeso
# ≥ 30	Obesidad
# Requisitos:

# Validar que peso y altura sean números positivos.

# Si no lo son, mostrar "Valor inválido".

peso= float(input("Ingresar peso: "))
altura= float(input("Ingresar altura: "))
imc= peso / (altura**2)

if imc <0 :
    print("Valor inválido")
elif imc >=30:
        print("Obesidad")
elif imc <=29.9:
            print("Sobrepeso")
elif imc <=24.9:
                print("Peso normal")
else:
                print("Bajo peso")    
print(f"Tu IMC es: {imc:.2f}")   



