from datetime import date

# pedimos la edad
edad_actual = input("Cuantos años tienes?")
edad_actual = int(edad_actual)

if edad_actual >= 18:
    mensaje = "Eres un adulto"
elif edad_actual >= 13 and edad_actual <= 17:
    mensaje = "Eres un adolescente"
elif edad_actual >=0 and edad_actual <= 12:
    mensaje = "Eres un niño"
else:
    mensaje = "Vienes del futuro! Es imposible!"

print(mensaje)