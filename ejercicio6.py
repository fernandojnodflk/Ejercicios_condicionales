"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
"""

cadena = input("Introduce una letra: ")


if len(cadena) == 1 and cadena.isupper():
    print("La letra es mayúscula.")
else:
    print("La letra no es mayúscula o la entrada no es válida.")
