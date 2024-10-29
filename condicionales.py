"""
condicionsles if
    evaluan expresiones booleanas

Estructura:
    if expresion:
        instrucciones 

if expresion:
    instrucciones
else:
    instrucciones 
if exprecion:
    instrucciones

elif exprecion:
    instrucciones 

else:
    instrucciones 

"""
print('Programa que verifica si un número es positivo')
num = int(input('Ingresa un número: '))

# Preguntar si el número es mayor a 0:
if num > 0:
    print('El número es positivo')
else:
    print('El número es negativo')

print('Fin del programa')
