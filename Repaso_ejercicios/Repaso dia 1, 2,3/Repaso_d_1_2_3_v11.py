# # # # EJERCICIO 1 – Cine
# # # # Un cine tiene descuentos según la edad y el día de la semana.

# # # # Preguntar:

# # # # "¿Qué día de la semana es? (lunes / martes / miércoles / jueves / viernes / sábado / domingo): "

# # # # "¿Cuántos años tenés? "

# # # # "¿Sos estudiante? (si / no): "

# # # # Reglas:

# # # # Si es miércoles → "2x1 en entradas"

# # # # Si es sábado o domingo y la persona es mayor de 65 → "Entrada gratuita para jubilados"

# # # # Si es estudiante y el día es entre semana (lunes a viernes) → "50% de descuento"

# # # # En cualquier otro caso → "Precio normal"

# # # # Validaciones:

# # # # Día de la semana: debe ser uno de los siete días (con lista)

# # # # Edad: debe ser un número positivo

# # # # Estudiante: debe ser "si" o "no"


# # # dia= input("¿Qué día de la semana es? (lunes / martes / miércoles / jueves / viernes / sábado / domingo): ").lower().strip()
# # # edad= int(input("¿Cuántos años tenés? "))
# # # estudiante= input("¿Sos estudiante? (si / no): ").lower().strip()

# # # rta_dias=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado" ,"domingo"]

# # # rta_si=["si", "Si", "SI","S","Sí","SÍ", "s"]
# # # rta_no=["no", "No", "NO","N","Nó","NÓ","n"]


# # # if dia not in rta_dias:
# # #     print(f"{dia} no es válido")
# # # elif estudiante not in rta_si and estudiante not in rta_no:
# # #     print (f"{estudiante} no es válido")
# # # elif edad <= 0:
# # #     print (f"{edad} no es válido")    
# # # else:
# # #     if dia =="miercoles":
# # #         print("2x1 en entradas")
# # #     elif (dia == "sabado" or dia == "domingo") and edad >= 65:
# # #             print("Entrada gratuita para jubilados")
# # #     elif dia  == rta_dias[:5] and estudiante in rta_si:
# # #             print("50% de descuento")  
# # #     else:
# # #         print("Precio normal")

# # EJERCICIO 2 – Heladería
# # Una heladería cobra según la cantidad de bochas y si el cliente es socio.

# # Preguntar:

# # "¿Cuántas bochas querés? (1, 2 o 3): "

# # "¿Sos socio? (si / no): "

# # "¿Es tu cumpleaños? (si / no): "

# # Reglas:

# # Precio por bocha: $200

# # Si es socio → 15% de descuento sobre el total

# # Si es su cumpleaños → bocha extra gratis (suma una bocha sin costo)

# # Si el total de bochas supera 5 → "No vendemos más de 5 bochas por persona"

# # Mostrar:
# # "Total: $[total]"
# # "Bochas: [cantidad]"

# # Validaciones:

# # Bochas: 1, 2 o 3 (con lista)

# # Socio: "si" o "no"

# # Cumpleaños: "si" o "no"


# EJERCICIO 1 – Estacionamiento (con descuentos acumulativos)
# Un estacionamiento cobra por hora, con descuentos según el tipo de vehículo y si es cliente frecuente.

# Preguntar:

# "¿Cuántas horas estuvo estacionado? "

# "¿Qué tipo de vehículo? (auto / moto / camioneta): "

# "¿Es cliente frecuente? (si / no): "

# Tarifas por hora:

# Auto: $200

# Moto: $100

# Camioneta: $300

# Descuentos:

# Si está más de 5 horas → 10% de descuento sobre el subtotal

# Si es cliente frecuente → 5% de descuento sobre el subtotal

# Los descuentos se suman (ej: 10% + 5% = 15% de descuento total)

# Mostrar:

# text
# Vehículo: [tipo]
# Horas: [X]
# Subtotal: $[X]
# Descuento total: [X]%
# Total a pagar: $[X]
# Validaciones:

# Horas > 0

# Tipo de vehículo válido

# Cliente frecuente: sí / no

horas= int(input("¿Cuántas horas estuvo estacionado?  "))
vehiculo= input("¿Qué tipo de vehículo? (auto / moto / camioneta): ").lower().strip()
cliente= input("¿Es cliente frecuente? (si / no): ").lower().strip()

rta_vehiculo= ["auto", "moto", "camioneta"]

rta_si= ["si", "Si", "SI","s","S"]
rta_no=["no","No","NO","N","n"]


if horas <=0 :
    print(f"{horas} es erroneo")
elif vehiculo not in rta_vehiculo and vehiculo not in rta_vehiculo:
    print(f"{vehiculo} no es valido")
elif cliente not in rta_si and cliente not in rta_no:
    print(f"{cliente} no es un cliente válido, pelotudo!")
else:

    if vehiculo == "camioneta":
        subtotal= horas * 300
        total= subtotal
        porc_desc = 0
        if horas >5:
            porc_desc +=10
            total_descuento_horas= total *0.10

            
            if cliente == "si":
                total_descuento_cliente= total * 0.05
                porc_desc += 5
                total_dtos= total_descuento_horas + total_descuento_cliente

                total = total - total_dtos
                
                print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")
            elif cliente == "no":
                total_descuento_cliente= 0
                porc_desc += 0
                total_dtos= total_descuento_horas + total_descuento_cliente

                total = total - total_dtos
                print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")
        else: 
            print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")        
    elif vehiculo == "auto":
        subtotal= horas * 200
        total= subtotal
        porc_desc = 0
        if horas >5:
            porc_desc +=10
            total_descuento_horas= total *0.10

            
            if cliente == "si":
                total_descuento_cliente= total * 0.05
                porc_desc += 5
                total_dtos= total_descuento_horas + total_descuento_cliente

                total = total - total_dtos
                
                print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")
            elif cliente == "no":
                total_descuento_cliente= 0
                porc_desc += 0
                total_dtos= total_descuento_horas + total_descuento_cliente

                total = total - total_dtos
                print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")
        else: 
            print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")
    elif vehiculo == "moto":
        subtotal= horas * 100
        total= subtotal
        porc_desc = 0
        if horas >5:
            porc_desc +=10
            total_descuento_horas= total *0.10

            
            if cliente == "si":
                total_descuento_cliente= total * 0.05
                porc_desc += 5
                total_dtos= total_descuento_horas + total_descuento_cliente

                total = total - total_dtos
                
                print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")
            elif cliente == "no":
                total_descuento_cliente= 0
                porc_desc += 0
                total_dtos= total_descuento_horas + total_descuento_cliente

                total = total - total_dtos
                print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")
        else: 
            print(f"Vehiculo: {vehiculo}.\nHoras: {horas}\nSubtotal: ${subtotal}\nDescuento total: %{porc_desc}\nTotal a pagar: {total}")                    


                


        




