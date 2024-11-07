"""
Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
"""
# Pedir tres números al usuario
print("HOLA :)")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
numeros = [num1, num2, num3]
numeros.sort(reverse=True)
print("Los números ordenados de mayor a menor son:", numeros)

print("gracias por usarme. Creado por fer➤")