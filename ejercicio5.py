"""
Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
sino se da un error.
"""
print("HOLA :)")
usuario = input("Ingresa tu nombre de usuario: ")
contrasena = input("Ingresa tu contraseña: ")
if usuario == "pepe" and contrasena == "asdasd":
    print("Has entrado al sistema :)")
else:
    print("Error: Usuario o contraseña incorrectos :(")

print("gracias por usarme. Creado por fer➤")