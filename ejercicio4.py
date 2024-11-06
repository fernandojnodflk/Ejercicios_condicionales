"""
Crea un programa que pida al usuario dos números y muestre su división 
si el segundo no es cero, o un mensaje de aviso en caso contrariogit add --all
"""
print("HOLA :)")
numerador = float(input("Ingresa el numerador: "))
denominador = float(input("Ingresa el denominador: "))
if denominador != 0:
    division = numerador / denominador
    print(f"La división es: {division}")
else:
    print("Error: No se puede dividir entre cero.")

print("gracias por usarme. Creado por fer➤")