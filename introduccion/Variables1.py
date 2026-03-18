# DATOS DEL PERSONAJE
nombre = "Aragon"   # String (Texto): Siempre va en comillas
nivel = 15          # Int (Entero): Un número sin decimales
puntos_vida = 94.5  # Float (Decimal): usar puntos, no comas
esta_vivo = True    # Bool (Booleano): Solo puede ser true o false

# OPERACIONES CON VARIABLES

#Podemos subir niveles
nuevo_nivel = nivel + 1

#Podemos unir textos
saludos = "Bienvenido, " + nombre

#MOSTRAR RESULTADOS
print(saludos)
print("Tu nivel actual es:")
print(nuevo_nivel)