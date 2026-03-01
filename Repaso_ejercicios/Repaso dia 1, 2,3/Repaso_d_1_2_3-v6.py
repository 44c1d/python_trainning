# Escribí un programa que simule el alquiler de una película en un kiosco.

# Reglas:

# Preguntar "¿Querés alquilar una película? (si/no): ".

# Preguntar "¿Sos mayor de 18 años? (si/no): ".

# Preguntar "¿La película es para mayores? (si/no): ".

# Condiciones:

# Si no quiere alquilar → mostrá "Ok, gracias por venir".

# Si quiere alquilar:

# Si es menor:

# Si la película es para mayores → mostrá "No podés alquilar esta película".

# Si la película no es para mayores → mostrá "Podés alquilarla".

# Si es mayor:

# Cualquier película → mostrá "Podés alquilarla".

# Requisitos:

# Usá if, elif, else.

# Usá listas rta_si y rta_no para las respuestas válidas.

# Normalizá todas las entradas con .lower().strip().

rent=input("¿Querés alquilar una película? (si/no): ").lower().strip()
rta_si= ["si","sí","s"]
rta_no=["no", "nó","n"]

if rent in rta_si:
    edad= input("¿Sos mayor de 18 años? (si/no): ")
    if edad in rta_si:
        print("podes alquilarla")
    elif edad in rta_no:
        rent_mayores= input("¿La película es para mayores? (si/no): ")
        if rent_mayores in rta_si:
            print("No podes alquilarla")
        elif rent_mayores in rta_no:
            print("Podes alquilarla")
elif rent in rta_no:
    print("Ok, gracias por venir")


    
          
