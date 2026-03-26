markdown
# Feedback de práctica – Días 1, 2 y 3

## 📝 Día 1 – Variables, inputs y prints

**Ejercicio:**  
Solicitar ciudad de nacimiento y nombre de mascota, y generar un nombre de usuario concatenando ambos valores.

**Código entregado:**
```python
ciudad = input("Dame tu ciudad de nacimiento").lower().strip()
mascota = input("Decime el nombre de tu mascota").lower().strip()
print(ciudad + mascota)
Resultado: ✅ Correcto.
Funciona, aplica normalización con .lower().strip() y cumple con el bonus.
Nota: 10/10

🔢 Día 2 – Tipos de datos y operadores
Ejercicio:
Solicitar un número de 3 cifras y mostrar el producto de sus dígitos. Validar que sea de exactamente 3 dígitos.

Código entregado:

python
numero = input("Ingresá un numero de tres cifras: ")

if len(numero) == 3 and numero.isdigit():
    digito1 = int(numero[0])
    digito2 = int(numero[1])
    digito3 = int(numero[2])
    producto = digito1 * digito2 * digito3
    print(f"El producto de los digitos ingresados es: {producto}")
else:
    print("Numero correcto")
Observaciones:

La validación está bien planteada (len() == 3 y isdigit()).

El else contiene un mensaje incorrecto: debería decir "Número inválido" en lugar de "Numero correcto".

Nota: 8/10 (se descuenta por error en mensaje de validación).

🧠 Día 3 – Control de flujo y condiciones flexibles
Ejercicio:
Simular un sistema de acceso según tenencia de entrada y mayoría de edad, aceptando múltiples variantes de respuesta ("s", "si", "sí", "no", "n").

Código entregado:

python
pregunta1 = input("Tenes entrada?: ")

opciones_si = ["si", "sí", "s"]
opciones_no = ["no", "nó", "n"]

if pregunta1 in opciones_si:
    pregunta2 = input("¿Sos mayor de edad? (sí/no)")
    if pregunta2 in opcion_si:
        pregunta3 = input("Podés pasar")
    elif pregunta2 in opciones_no:
        print("Pasá con un adulto")
else:
    print("No podés pasar")
Observaciones:

No se normalizó la segunda entrada (pregunta2).

Error en el nombre de la lista (opcion_si no existe).

Se usó input() en lugar de print() para mostrar el mensaje de acceso.

Faltó manejar el caso de respuesta no válida en la segunda pregunta.

Nota: 6/10 (estructura base presente, pero múltiples errores de implementación).

📊 Resumen de notas
Día	Tema	Nota
1	Variables, inputs, prints	10
2	Operadores y validación	8
3	Control de flujo	6
🚀 Recomendaciones generales
Siempre normalizar entradas con .lower().strip().

Verificar nombres de variables y listas antes de usarlas.

Distinguir entre input() (para preguntar) y print() (para mostrar mensajes).

Probar el código con distintos casos de prueba (válidos, inválidos, límites).
🟨 DÍA 1 ✅ (casi perfecto)

Tu lógica:

if edad <= 99:

Funciona, pero el requerimiento decía:

Si la edad es mayor a 100 → mostrar "¡Qué privilegio!"

Tu condición debería ser:

if edad > 100:
    print("¡Qué privilegio!")
else:
    print(...)

Ahora mismo, si alguien tiene exactamente 100 años, no entra en el privilegio.

Pequeño detalle lógico.

🟨 DÍA 2 ✅ (bien estructurado)

Muy bien separado por bloques 👏

Solo detalle técnico:

El requisito decía:

Validar que el número sea entero positivo.

Vos validás:

if numero < 0:

Eso deja pasar el 0 como válido.

Si querés estrictamente positivo debería ser:

if numero <= 0:

Pero estructuralmente está correcto 👍

🟩 DÍA 3 ❌ (acá hay error lógico)

La validación que hacés es incorrecta.

Mirá esto:

if imc < 0:

El requisito decía:

Validar que peso y altura sean números positivos.

Vos estás validando el IMC, no el peso y la altura.

Si alguien pone:

peso = -70

altura = 1.75

El IMC puede dar negativo, pero la validación debería hacerse antes.

❌ Segundo error: Orden de condiciones

Esto está mal ordenado:

elif imc >=30:
elif imc <=29.9:
elif imc <=24.9:

Porque Python evalúa de arriba hacia abajo.

Si imc es 22, cumple:

elif imc <=29.9

Y nunca llega a Peso normal.

🔥 Versión correcta y profesional
peso = float(input("Ingresar peso: "))
altura = float(input("Ingresar altura: "))

if peso <= 0 or altura <= 0:
    print("Valor inválido")

else:
    imc = peso / (altura ** 2)

    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc <= 24.9:
        categoria = "Peso normal"
    elif imc <= 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    print(f"Tu IMC es: {imc:.2f}")
    print(f"Categoría: {categoria}")
🎯 Lo que hiciste bien

✔ Uso correcto de f-strings
✔ Uso correcto de %
✔ Uso correcto de elif
✔ Buena indentación

📊 Evaluación

Día 1: 8/10
Día 2: 8.5/10
Día 3: 6.5/10 (por validación y orden lógico)

Promedio general: 7.6 → Bueno (aprobado)

Si querés, te subo ahora el nivel a:

👉 Validación con try/except
👉 Manejo de errores reales
👉 Loop hasta que el usuario ingrese datos válidos

Decime si seguimos subiendo dificultad 🚀
