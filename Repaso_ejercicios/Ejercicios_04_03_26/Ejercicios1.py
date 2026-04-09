# JERCICIO 3 – Calculadora de estacionamiento
# Un estacionamiento cobra por hora, con descuentos según el tipo de vehículo y tiempo de estadía.

# Preguntar:

# "¿Cuántas horas estuvo estacionado? (ej: 2.5): "

# "¿Qué tipo de vehículo? (auto / moto / camioneta): ".lower().strip()

# "¿Es cliente frecuente? (si/no): ".lower().strip()

# Tarifas por hora según vehículo:

# Auto → $200 por hora

# Moto → $100 por hora

# Camioneta → $300 por hora

# Reglas de descuento:

# Si está más de 5 horas → 10% de descuento sobre el subtotal

# Si es cliente frecuente → 5% de descuento sobre el subtotal

# Los descuentos se suman (ej: 10% + 5% = 15% de descuento total)

# Mostrar:

# text
# Vehículo: [auto/moto/camioneta]
# Horas: [XX]
# Subtotal: $[XX]
# Descuento aplicado: [XX]%
# Total a pagar: $[XX]
# Validaciones:

# Horas > 0

# Tipo de vehículo válido (auto, moto, camioneta)

# Respuesta de cliente frecuente válida (sí/no)

# ✅ Ejemplo de ejecución
# text
# ¿Cuántas horas estuvo estacionado? 6
# ¿Qué tipo de vehículo? (auto / moto / camioneta): auto
# ¿Es cliente frecuente? (si/no): si

# Vehículo: auto
# Horas: 6.0
# Subtotal: $1200.00
# Descuento aplicado: 15%
# Total a pagar: $1020.00
# Cálculo:

# Subtotal: 6 × $200 = $1200

# Descuento: 10% (por +5h) + 5% (frecuente) = 15%

# Total: $1200 × 0.85 = $1020

# ¿Lo hacés? Acordate:

# Validar primero

# Calcular después

# Mostrar al final

# Cuando lo tengas, me lo pasás.

#-----------Input--------------#

horas=float(input("¿Cuántas horas estuvo estacionado? (ej: 2.5): "))
vehiculo=input("¿Qué tipo de vehículo? (auto / moto / camioneta): ").lower().strip()
rta_vehiculo=["auto","moto","camioneta"]
cliente=input("¿Es cliente frecuente? (si/no): ").lower().strip()
rta_si=["si","sí","s"]
rta_no=["no","n"]

#----------Validaciones--------#

if horas <=0:
    print(f"{horas} es un valor incorrecto")
elif vehiculo not in rta_vehiculo:
    print(f"{vehiculo} es un valor incorrecto")
elif cliente not in rta_si + rta_no:
    print(f"{cliente} es un valor incorrecto")
else:

    if vehiculo == "auto":
        base= 200
    elif vehiculo =="moto":
        base = 100
    elif vehiculo =="camioneta":
        base = 300
    elif horas >=5:
        total= (base*10)/100
    elif cliente in rta_si:
        total= (total*5)/100

                   