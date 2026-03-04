# EJERCICIO – Tren turístico (descuentos por edad y residencia)
# Un tren turístico ofrece descuentos según la edad y si el pasajero es residente local.

# Reglas:

# Preguntar "¿Querés comprar un pasaje? (si/no): ".

# Preguntar "¿Sos residente local? (si/no): ".

# Preguntar "¿Cuántos años tenés? (ingresá el número): ".

# Condiciones de descuento:

# Si no quiere comprar → mostrá "Gracias por consultar".

# Si quiere comprar:

# Si es residente:

# Si edad < 12 → mostrá "Pasaje gratis (menor residente)".

# Si edad ≥ 60 → mostrá "50% de descuento (adulto mayor residente)".

# Si edad entre 12 y 59 → mostrá "10% de descuento (residente)".

# Si no es residente:

# Si edad < 12 → mostrá "50% de descuento (menor no residente)".

# Si edad ≥ 60 → mostrá "25% de descuento (adulto mayor no residente)".

# Si edad entre 12 y 59 → mostrá "Tarifa completa (sin descuento)".

# Requisitos:

# Usá if, elif, else.

# Usá listas rta_si y rta_no para las respuestas de sí/no.

# Para la edad, usá int() y validá que sea un número positivo.

# Normalizá todas las entradas de texto con .lower().strip().

# 🧠 ¿Qué vas a practicar?
# Misma estructura que el ejercicio anterior, pero con un nivel más de condiciones (edad con números).

# Uso combinado de if anidados y comparaciones numéricas.

# Seguir practicando la indentación y los caminos completos.

# ✅ Ejemplo de ejecución
# text
# ¿Querés comprar un pasaje? (si/no): si
# ¿Sos residente local? (si/no): si
# ¿Cuántos años tenés? 65
# 50% de descuento (adulto mayor residente)


# pasaje= input("¿Querés comprar un pasaje?").lower().strip()
# residente= input("¿Sos residente local?").lower().strip()
# edad= int(input("¿Cuántos años tenés?"))
# rta_si=["si", "sí","s"]
# rta_no=["no","nó","n"]

# if pasaje in rta_si:
#     if residente in rta_si:
#         if edad <12:
#             print("Pasaje gratis (menor residente)")
#         elif edad >=60:
#             print("50% de descuento (adulto mayor residente)")
#         elif edad ==12:
#             print("10% de descuento (residente)")
#         elif edad <=59:
#             print("10% de descuento (residente)")
#     elif residente in rta_no:
#         if edad <12:
#             print("50% de descuento (menor no residente)")
#         elif edad >=60:
#             print("25% de descuento (adulto mayor no residente)")
#         elif edad ==12:
#             print("Tarifa completa (sin descuento)")
#         elif edad <=59:
#             print("Tarifa completa (sin descuento)")
# elif pasaje in rta_no:
#     print("Gracias por consultar")
                           
           
# Version corregida y optimizada

pasaje = input("¿Querés comprar un pasaje? ").lower().strip()
residente = input("¿Sos residente local? ").lower().strip()
edad = int(input("¿Cuántos años tenés? "))
rta_si = ["si", "sí", "s"]
rta_no = ["no", "n"]

if edad < 0:
    print("Valor erróneo")
elif pasaje in rta_si:
    if residente in rta_si:
        if edad < 12:
            print("Pasaje gratis (menor residente)")
        elif edad <= 59:
            print("10% de descuento (residente)")
        else:
            print("50% de descuento (adulto mayor residente)")
    elif residente in rta_no:
        if edad < 12:
            print("50% de descuento (menor no residente)")
        elif edad <= 59:
            print("Tarifa completa (sin descuento)")
        else:
            print("25% de descuento (adulto mayor no residente)")
    else:
        print("Respuesta no válida para residencia")
elif pasaje in rta_no:
    print("Gracias por consultar")
else:
    print("Respuesta no válida para pasaje")s