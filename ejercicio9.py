"""
Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
"""
# Pedir tres números al usuario
print("HOLA :)")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
numeros = [num1, num2, num3]
numeros.sort(reverse=True)
print("Los números ordenados de mayor a menor son:", numeros)

print("gracias por usarme. Creado por fer➤")