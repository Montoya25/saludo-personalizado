#Se pide el nombre del usuario
nombre_ingresado = input("Ingresa tu nombre: ")

#Uso {} para ingresar los datos al mensaje
mensaje_final = "¡Hola, {nombre_ingresado}! Bienvenido a aprender Python."

#Se cambia el formato y se imprime
print(mensaje_final.format(nombre_ingresado=nombre_ingresado))