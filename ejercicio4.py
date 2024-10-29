"""
Crea un programa que pida al usuario dos números y muestre su división 
si el segundo no es cero, o un mensaje de aviso en caso contrario
"""

numerador = float(input("Introduce el numerador: "))
denominador = float(input("Introduce el denominador: "))

if denominador != 0:
    division = numerador / denominador
    print(f"La división es: {division}")
else:
    print("Error: No se puede dividir entre cero.")
