"""
Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
la base y el exponente. Pueden ocurrir tres cosas:
 El exponente sea positivo, sólo tienes que imprimir la potencia.
 El exponente sea 0, el resultado es 1.
 El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""

base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))


if exponente > 0:
    resultado = base ** exponente
    print(f"La potencia de {base} elevado a {exponente} es: {resultado}")
elif exponente == 0:
    print("Cualquier número elevado a 0 es 1.")
else:  
    resultado = 1 / (base ** abs(exponente))
    print(f"La potencia de {base} elevado a {exponente} es: {resultado}")
