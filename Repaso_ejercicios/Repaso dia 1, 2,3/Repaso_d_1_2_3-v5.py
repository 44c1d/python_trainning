# EJERCICIO – Club nocturno (solo estructura)
# Escribí un programa que simule el ingreso a un club.

# Reglas:

# Preguntar "¿Tenés entrada? (si/no): ".

# Preguntar "¿Sos mayor de edad? (si/no): ".

# Preguntar "¿Vestís formal? (si/no): ".

# Condiciones de ingreso:

# Si no tiene entrada → mostrá "No podés pasar".

# Si tiene entrada:

# Si es menor → mostrá "No podés pasar".

# Si es mayor:

# Si viste formal → mostrá "Podés pasar".

# Si no viste formal → mostrá "Pasá, pero la próxima vení más formal".

# Requisitos:

# Usá if, elif, else (sin and/or, como acordamos).

# Todas las respuestas deben normalizarse con .lower().strip().

# No hace falta validar respuestas inválidas (por ahora).

entrada= input("Tenes entrada?: ").lower().strip()
rta_si= ["si","sí","s"]
rta_no= ["no","nó","n"]

if entrada in rta_si:
    edad = input("Sos mayor de edad? : ").lower().strip()
    if edad in rta_si:
        vestimenta=input("Vestís formal?: ").lower().strip()
        if vestimenta in rta_si:
            print("Podés pasar")
        elif vestimenta in rta_no:
            print("Pasá, pero la próxima vení más formal")
    elif edad in rta_no:
        print("No podés pasar")
elif entrada in rta_no:
    print("No podés pasar")


        





