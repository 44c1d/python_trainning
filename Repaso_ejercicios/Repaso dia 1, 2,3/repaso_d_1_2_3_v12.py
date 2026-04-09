# EJERCICIO 2 – Calculadora de envíos
# Una tienda online cobra envío según el destino y el peso.

# Preguntar:

# "¿Cuál es el destino? (local / nacional / internacional): "

# "¿Cuánto pesa el paquete? (en kg): "

# "¿Es envío express? (si / no): "

# Costo base por destino:

# Local: $500

# Nacional: $1200

# Internacional: $3500

# Recargos:

# Si el peso supera los 10 kg → 8% de recargo sobre el costo base

# Si es envío express → 15% de recargo sobre el costo base

# Los recargos se suman (ej: 8% + 15% = 23% de recargo total)

# Mostrar:

# text
# Destino: [local/nacional/internacional]
# Peso: [X] kg
# Recargo total: [X]%
# Total a pagar: $[X]
# Validaciones:

# Peso > 0

# Destino válido (local / nacional / internacional)

# Express: sí / no



destino= input("¿Cuál es el destino? (local / nacional / internacional): ").lower().strip()

peso= float(input("¿Cuánto pesa el paquete? (en kg): "))

express=input("¿Es envío express? (si / no): ").lower().strip()

rta_destino= ["local", "nacional", "internacional"]

rta_si= ["si","Si", "SI", "S","s"]
rta_no= ["no", "No", "NO", "N", "n"]

if destino not in rta_destino:
    print(f"{destino} es invalido")
elif express not in rta_si and express not in rta_no:
    print(f"{express} es invalido")
elif peso <=0:
    print(f"como vas a poner {peso} de peso, pelotudo")
else:

    if destino == "internacional":
        subtotal= 3500
    elif destino == "nacional":
        subtotal= 1200
    else:
        subtotal= 500

    if peso >10:
        recargo_total+= 8
    if express in rta_si:
        recargo_total+= 15

    total = subtotal + (1+recargo_total/100) 
        

