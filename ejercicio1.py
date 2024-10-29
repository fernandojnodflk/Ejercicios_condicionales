"""
dos números e indique Cuál es el mayor 
Si los dos son iguales que muestre el mensaje "Son iguales" 
"""
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El mayor es: {num1}")
elif num1 < num2:
    print(f"El mayor es: {num2}")
else:
    print("Son iguales")
