# Día 1 – Variables y inputs
# Ejercicio:
# Crear un programa que:

# Pregunte el nombre de la persona.

# Pregunte su edad.

# Muestre un mensaje como:

# text
# Hola [nombre], el año que viene tendrás [edad+1] años.
# Conceptos: input(), print(), conversión de tipos (int()), operaciones matemáticas.

nombre=input (str("Cual es tu nombre?")).upper().strip()
edad=int(input("Cual es tu edad?"))

print(f"Hola {nombre}, el año que viene tendrás {edad + 1} años. ")
# Día 2 – Tipos de datos y operadores
# Ejercicio:
# Pedir al usuario un número de hasta 3 cifras (ej: 347).
# Calcular la suma de sus dígitos y mostrarla.

# Ejemplo:

# text
# Ingresá un número: 347
# La suma de sus dígitos es: 14
# (3 + 4 + 7 = 14)

# Conceptos: input(), int(), operador // (división entera), % (módulo), o manejo de strings con [0], [1], etc.
numero=int(input("Ingresá un numero de hasta 3 digitos:"))




# Día 3 – Control de flujo
# Ejercicio:
# Simular un semáforo peatonal:

# Preguntar si el semáforo está en verde (sí/no).

# Si está en verde, preguntar si viene un auto (sí/no).

# Reglas:

# Si está en verde y no viene auto → "Podés cruzar".

# Si está en verde y viene auto → "Esperá que pase el auto".

# Si no está en verde → "No cruces, esperá el verde".

# Conceptos: if/else, and, or, entrada de texto con lower() para normalizar respuestas.

pregunta1 = input("El semáforo está en verde? (sí/no): ").strip().upper()

if pregunta1 == "SI":
    pregunta2 = input("Viene un auto? (sí/no): ").strip().upper()
    if pregunta2 == "SI":
        print("Esperá que pase el auto.")
    else:
        print("Podés cruzar.")
else:
    print("No cruces, esperá el verde.")
