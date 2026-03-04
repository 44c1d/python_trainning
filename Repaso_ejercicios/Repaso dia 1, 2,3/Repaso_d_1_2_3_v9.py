# # # # # NUEVO EJERCICIO 1 – Calculadora de propina (versión rápida)
# # # # # python
# # # # # # Reglas ya las tenés escritas arriba
# # # # # # Solo te marco los puntos clave:
# # # # # Validaciones importantes:

# # # # # total tiene que ser float y mayor a 0.

# # # # # Si no es válido → "Total inválido".

# # # # # porcentaje solo acepta 10, 15 o 20 (como entero).

# # # # # # Si el porcentaje no es válido → "Porcentaje no válido".

# # total_original = float(input("Total de la cuenta: $"))
# # propina= input("¿Querés dejar propina? (si/no): ").lower().strip()
# # redondeo= input("¿Querés redondear el total? (si/no): ").lower().strip()

# # rta_si = ["si", "sí", "s"]
# # rta_no = ["no", "nó", "n"]
# # porcen = [10, 15, 20]

# # if total_original <=0:
# #     print(f"{total_original} no es un importe válido, intentar de nuevo")
# # else:
# #     total = total_original
# #     porc_prop= 0
# #     total_prop= 0 

# #     if propina in rta_si:
# #         porc_prop= int(input("¿Que procentaje querés dejar?: "))
# #         if porc_prop in porcen:
# #             total_prop= (total_original*porc_prop)/100
# #             total += total_prop
# #         else:
# #             print(f"{porc_prop} no es un porcentaje válido. Los porcentajes validos son: %10, %15, %20")     
           

# #     if redondeo in rta_si:
# #         total= round(total)
# #     elif redondeo in rta_no:
# #         pass    
    
# #     print(f"Total sin propina: ${total_original}\nProcentaje de propina aplicado: %{porc_prop}\nTotal propina: ${total_prop}\nTotal a pagar: ${total}")                    


# # # #     EJERCICIO 2 – ¿Puedo comprar?
# # # # Preguntar:

# # # # "¿Tenés dinero suficiente? (si/no): "

# # # # "¿Tenés tarjeta de crédito? (si/no): "

# # # # "¿El producto está en oferta? (si/no): "

# # # # Reglas:

# # # # Si no tiene dinero:

# # # # Si tiene tarjeta y está en oferta → "Podés comprar con tarjeta".

# # # # Si no → "No podés comprar".

# # # # Si tiene dinero:

# # # # Si está en oferta → "Podés comprar (y aprovechás el descuento)".

# # # # Si no → "Podés comprar (precio normal)".

# # # # Validar todo con listas.
            
# # dinero= input("¿Tenés dinero suficiente? (si/no): ").lower().strip()
# # oferta= input("¿El producto está en oferta? (si/no): ").lower().strip()
# # rta_si=["si", "sí","s"]
# # rta_no=["no","n"]

# # if dinero in rta_si:
# #     if oferta in rta_si:
# #         print("Podés comprar (y aprovechás el descuento)")
# #     elif oferta in rta_no:
# #         print("Podés comprar (precio normal)")
# #     else:
# #         print("Respesta no válida")    
# # elif dinero in rta_no:
# #     TC=input("¿Tenés tarjeta de crédito? (si/no): ").lower().strip()

# #     if TC in rta_si:
# #         if oferta in rta_si:
# #             print("Podés comprar con tarjeta")
# #         elif oferta in rta_no:
# #             print("No podés comprar")
# #         else:
# #             print("Respuesta no válida")    

# #     elif TC in rta_no:
# #         print("No podés comprar")
# #     else:
# #         print("Respesta no válida")            
# # else:
# #     print("Respesta no válida")


# # # EJERCICIO 3 – Acceso a streaming (completo)
# # # Reglas:

# # # Si no tiene cuenta activa → "Necesitás una cuenta".

# # # Si tiene cuenta activa:

# # # Si hay contenido y tiene tiempo → "A mirar!".

# # # Si hay contenido pero no tiene tiempo → "Agendalo para después".

# # # Si no hay contenido → "Busquemos algo nuevo".

# # # Validaciones:

# # # Usá rta_si y rta_no para todas las respuestas.

# # # Si alguna respuesta no es válida → "Respuesta no válida".

# # cuenta=input("¿Tenés cuenta activa? (si/no): ").lower().strip()
    
# # rta_si=["si","sí","s"]
# # rta_no=["no","nó","n"]

# # if cuenta in rta_si:
# #     contenido=input("¿Hay contenido que te interese? (si/no): ").lower().strip()
# #     if contenido in rta_si:
# #         tiempo=input("¿Poseés de tiempo para ver el contenido? (si/no): ").lower().strip()
# #         if tiempo in rta_si:
# #             print("A mirar!")
# #         elif tiempo in rta_no:
# #             print("Agendalo para después")
# #         else:
# #             print("Respuesta no válida")    
# #     elif contenido in rta_no:
# #         print("Busquemos algo nuevo")
# #     else:
# #         print("Respuesta no válida")    
# # elif cuenta in rta_no:
# #     print("Necesitás una cuenta")
# # else:
# #     print("Respuesta no válida")



            

#  EJERCICIO 1 – Día 1 (variables y prints)
# Preguntá:

# "¿Cómo te llamás?"

# "¿En qué año naciste?"

# Mostrá:

# text
# Hola [nombre], vas a cumplir [edad] años este año (o el próximo).
# Pista: la edad la calculás con 2026 - año_nacimiento.

nombre=str(input("¿Cómo te llamás?")).upper()
año_nacimiento=int(input("¿En qué año naciste?"))
edad= 2026-año_nacimiento

print(f"Hola {nombre}, vas a cumplir {edad} años este año (o el próximo)")

 


# 🟨 EJERCICIO 2 – Día 2 (operadores)
# Preguntá un número de 3 cifras.
# Mostrá el resto de dividirlo por 5.

# Ejemplo:
# Número: 127 → Resto: 2 (porque 127 / 5 = 25, resto 2)
numero=int(input("Ingrese un numero de tres cifras: "))

resto= numero%5

print(resto)


# 🟥 EJERCICIO 3 – Día 3 (if/else)
# Preguntá:

# "¿Está lloviendo? (si/no)"

# "¿Tenés paraguas? (si/no)"

# Reglas:

# Si no llueve → "Podés salir sin paraguas"

# Si llueve y tenés paraguas → "Salí nomás"

# Si llueve y no tenés paraguas → "Quedate en casa"

llueve=input("¿Está lloviendo? (si/no)").lower().strip()
paraguas= input("¿Tenés paraguas? (si/no)").lower().strip()
rta_si=["si","sí","s"]
rta_no=["no","n"]
if llueve in rta_si:
    if paraguas in rta_si:
        print("Salí nomás")
    elif paraguas in rta_no:
        print("Quedate en casa")    
    else:
        print("Respuesta inválida")
elif llueve in rta_no:
    print("Podés salir sin paraguas")
else:
    print("Respuesta inválida")                




    



                