"""
El director de una escuela está organizando un viaje de estudios, y requiere
determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de
viajes por el servicio. La forma de cobrar es la siguiente:
si son 100 alumnos o más, el costo por cada alumno es de 65 euros;
de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros,
sin importar el número de alumnos.
Realice un programa que permita determinar el pago a la compañía de autobuses
y lo que debe pagar cada alumno por el viaje.
"""
print("HOLA :)")
num_alumnos = int(input("Introduce el número de alumnos: "))

if num_alumnos >= 100:
    costo_por_alumno = 65
elif num_alumnos >= 50:
    costo_por_alumno = 70
elif num_alumnos >= 30:
    costo_por_alumno = 95
else:
    costo_por_alumno = 4000

if num_alumnos < 30:
    print(f"El costo de la renta del autobús es de 4000 euros.")
else:

    total_pago_alumnos = costo_por_alumno * num_alumnos

    total_pago_compania = costo_por_alumno * num_alumnos

    print(f"El costo por alumno es {costo_por_alumno} euros.")
    print(f"El total que deben pagar los alumnos es {total_pago_alumnos} euros.")
    print(f"El total que debe pagar la compañía de autobuses es {total_pago_compania} euros.")

print("gracias por usarme. Creado por fer➤")