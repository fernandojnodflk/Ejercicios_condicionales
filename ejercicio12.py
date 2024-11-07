"""
Realiza un programa que pida por teclado el resultado (dato entero) obtenido
al lanzar un dado de seis caras y muestre por pantalla el número en letras
(dato cadena) de la cara opuesta al resultado obtenido.
* Nota 1: En las caras opuestas de un dado de seis caras están los números:
1-6, 2-5 y 3-4.
* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6,
se mostrará el mensaje: "ERROR: número incorrecto.".
"""

print("HOLA :)")
numero_dado = int(input("Ingresa el número obtenido al lanzar el dado (1-6): "))

if numero_dado == 1:
    print("La cara opuesta es 6.")
elif numero_dado == 2:
    print("La cara opuesta es 5.")
elif numero_dado == 3:
    print("La cara opuesta es 4.")
elif numero_dado == 4:
    print("La cara opuesta es 3.")
elif numero_dado == 5:
    print("La cara opuesta es 2.")
elif numero_dado == 6:
    print("La cara opuesta es 1.")
else:
    print("ERROR: número incorrecto.")

print("gracias por usarme. Creado por fer➤")