"""
Juego Piedra Papel y Tijera
Programa que lea las opciones de 2 jugadores, y muestra el resultado
Empate, gana jugador 1 o gana jugador 2
Si introducimos una opción que no coindica con piedra, papel o tijera
Diga que opción Incorrecta
"""
print("HOLA :)")
jugador1 = input("Jugador 1, elige Piedra, Papel o Tijera: ").lower()
jugador2 = input("Jugador 2, elige Piedra, Papel o Tijera: ").lower()


if jugador1 not in ['piedra', 'papel', 'tijera'] or jugador2 not in ['piedra', 'papel', 'tijera']:
    print("Opción incorrecta.")
else:

    if jugador1 == jugador2:
        print("Empate.")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        print("Gana Jugador 1.")
    else:
        print("Gana Jugador 2.")

print("gracias por usarme. Creado por fer➤")