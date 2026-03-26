# EJERCICIO – Sistema de acceso a concierto
# Un concierto tiene diferentes tipos de entrada y restricciones por edad.

# Preguntar:

# "¿Qué tipo de entrada tenés? (vip / platea / campo): "

# "¿Cuántos años tenés? (ingresá el número): "

# "¿Tenés autorización de mayores? (si / no): "

# Reglas de acceso:

# VIP:

# Si es menor de 18 → "Acceso VIP solo con tutor"

# Si es 18 o más → "Acceso VIP libre"

# Platea:

# Si es menor de 12 → "Acceso a platea no permitido para menores de 12"

# Si es 12 o más → "Acceso a platea permitido"

# Campo:

# Si es menor de 16 y no tiene autorización → "Acceso a campo denegado"

# Si es menor de 16 y tiene autorización → "Acceso a campo con autorización"

# Si es 16 o más → "Acceso a campo libre"

# Validaciones:

# Tipo de entrada: debe ser "vip", "platea" o "campo"

# Edad: debe ser un número entero (asumí que el usuario lo pone bien)

# Autorización: debe ser "si" o "no"

# Estructura obligatoria:

# Pedir datos

# Validar todo primero

# Si todo está bien, aplicar reglas
# "¿Tenés autorización de mayores? (si / no): "

entrada = input("¿Qué tipo de entrada tenés? (vip / platea / campo): ").lower().strip()
edad = int(input("¿Cuántos años tenés? (ingresá el número): "))
rta_entrada = ["vip", "platea", "campo"]

#Validaciones

if entrada not in rta_entrada:
    print(f"{entrada} es un valor incorrecto")
elif edad <=0:
    print(f"{edad} es un valor incorrecto")
else:
    if entrada == "vip":
        if edad <18:
            print("Acceso VIP solo con tutor")
        elif edad >= 18:
            print("Acceso VIP libre") 
    elif entrada == "platea":
        if edad <12:
            print ("Acceso a platea no permitido para menores de 12")
        elif edad >=12:
            print("Acceso a platea permitido")
    elif entrada == "campo":
        if edad <16:
            autorizacion= input("¿Tenés autorización de mayores? (si / no): ").lower().strip()
            rta_autorizacion_si= ["si", "Si", "S", "SI"]
            rta_autorizacion_no= ["no", "No", "N", "NO"]
            if autorizacion in rta_autorizacion_no:
                print("Acceso a campo denegado")
            elif autorizacion in rta_autorizacion_si:
                print("Acceso a campo con autorización")
            else:
                print(f"{autorizacion} valor invalido")
        elif edad >= 16:
            print("Acceso a campo libre")






              


