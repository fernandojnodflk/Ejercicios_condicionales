"""
La política de cobro de una compañía telefónica es: cuando se realiza una 
llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un programa para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.
"""

print("HOLA :)")
duracion_llamada = int(input("Introduce la duración de la llamada en minutos: "))
dia_semana = int(input("Introduce el día de la semana (1 = lunes, 7 = domingo): "))
turno = input("Introduce el turno (mañana/tarde): ").lower()


if duracion_llamada <= 5:
    costo_llamada = 1
elif duracion_llamada <= 8:
    costo_llamada = 1 + (duracion_llamada - 5) * 0.80
elif duracion_llamada <= 10:
    costo_llamada = 1 + 3 * 0.80 + (duracion_llamada - 8) * 0.70
else:
    costo_llamada = 1 + 3 * 0.80 + 2 * 0.70 + (duracion_llamada - 10) * 0.50

if dia_semana == 7:
    costo_llamada *= 1.03
elif turno == "mañana":
    costo_llamada *= 1.15
elif turno == "tarde":
    costo_llamada *= 1.10

print(f"El costo de la llamada es: {costo_llamada:.2f} euros.")

print("gracias por usarme. Creado por fer➤")