# EJERCICIO – Máquina de café (versión simplificada)
# Una máquina de café pregunta:

# "¿Querés un café? (si/no): "

# "¿Querés que sea grande? (si/no): "

# "¿Querés leche? (si/no): "

# Reglas:

# Si no quiere café → mostrá "Que tengas buen día".

# Si quiere café:

# Si quiere grande:

# Si quiere leche → mostrá "Café grande con leche: $150"

# Si no quiere leche → mostrá "Café grande solo: $120"

# Si no quiere grande (chico):

# Si quiere leche → mostrá "Café chico con leche: $100"

# Si no quiere leche → mostrá "Café chico solo: $80"

# Requisitos:

# Usá if, elif, else.

# Usá listas rta_si y rta_no.

# Normalizá con .lower().strip().

# Validá que las respuestas sean válidas. Si no, mostrá "Respuesta no válida".

# 🧠 ¿Qué vas a practicar?
# Misma estructura de anidamiento que venís usando.

# Confirmar que entendiste el orden de las validaciones.

# Cerrar el día con un ejercicio completo y funcional.

# ✅ Ejemplo de ejecución
# text
# ¿Querés un café? (si/no): si
# ¿Querés que sea grande? (si/no): si
# ¿Querés leche? (si/no): no
# Café grande solo: $120

cafe= input("¿Querés un café? (si/no)").lower().strip()
tamaño=input("¿Querés que sea grande? (si/no):").lower().strip()
leche=input("¿Querés leche? (si/no):").lower().strip()
rta_si=["si","sí","s"]
rta_no=["no","no","n"]

if cafe in rta_si:
    if tamaño in rta_si:
        if leche in rta_si:
            print("Café grande con leche: $150")
        elif leche in rta_no:
            print("Café grande solo: $120")
        else:
            print("Respuesta no válida")    
    elif tamaño in rta_no:
        if leche in rta_si:
            print("Café chico con leche: $100")
        elif leche in rta_no:
            print("Café chico solo: $80")
    else:
            print("Respuesta no válida")    
elif cafe in rta_no:
    print("Que tengas buen día")
else:
    print("Respuesta no válida")

                





