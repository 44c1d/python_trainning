# 🆕 EJERCICIO 2 – Calculadora de envíos (con recargos)
# Una tienda online cobra envío según el destino y el peso del paquete.

# Preguntar:

# "¿Peso del paquete? (en kg): "

# "¿Destino? (local / nacional / internacional): ".lower().strip()

# "¿Es envío express? (si/no): ".lower().strip()

# Reglas de costo base por destino:

# Local → $500

# Nacional → $1200

# Internacional → $3500

# Reglas de recargo:

# Si el peso supera los 10 kg → recargo del 8% sobre el costo base

# Si es envío express → recargo del 15% sobre el costo base

# Los recargos se suman (no se aplican por separado, se acumulan)

# Mostrar:

# text
# Destino: [local/nacional/internacional]
# Peso: [XX] kg
# Recargo por peso: [XX]%
# Recargo por express: [XX]%
# Total a pagar: $[total]
# Validaciones:

# Peso > 0

# Destino solo "local", "nacional", "internacional"

# Respuestas sí/no con listas

# ✅ Ejemplo de ejecución
# text
# ¿Peso del paquete? (en kg): 12
# ¿Destino? (local / nacional / internacional): internacional
# ¿Es envío express? (si/no): si

# Destino: internacional
# Peso: 12 kg
# Recargo por peso: 8%
# Recargo por express: 15%
# Total a pagar: $4305.00
# Cálculo:

# Base: $3500

# Recargo peso (8%) = $280

# Recargo express (15%) = $525

# Total = 3500 + 280 + 525 = $4305
# "¿Peso del paquete? (en kg): "

# "¿Destino? (local / nacional / internacional): ".lower().strip()

# "¿Es envío express? (si/no): ".lower().strip()

# Reglas de costo base por destino:

peso=float(input("¿Peso del paquete? (en kg): "))
destino= input("¿Destino? (local / nacional / internacional): ").lower().strip()
rta_destino=["local","nacional","internacional"]
express= input("¿Es envío express? (si/no): ").lower().strip()
rta_si=["si","sí","s"]
rta_no=["no","n"]

if destino in rta_destino == "internacional":
    total_destino = 3500
elif destino in rta_destino == "nacional":
    total_destino = 1200
elif destino in rta_destino == "local":  
    total_destino = 500
    if peso > 10:
            recargo_peso= 8          
            total = (total_destino*recargo_peso)/100
    elif peso <=9:
            recargo_peso= 0
            total= total_destino
    elif peso <=0:
        print("Valor equivocado")
        if express in rta_si:
            recargo_express= 15
            total = (destino *recargo_express)/100
        elif express in rta_no:
            recargo_express=0
            pass
        else:
            print("Valor equivocado")
else:
    print("Valor equivocado")

print(f"Destino: {destino}\nPeso: {peso}\nRecargo por peso: {recargo_peso}\nRecargo por express: {recargo_express}\nTotal a pagar: {total}")

            




               


