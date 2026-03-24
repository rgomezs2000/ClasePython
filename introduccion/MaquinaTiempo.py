from datetime import date

# pedimos el nombre
nombre = input("Como te llamas?")
edad_actual = input("Cuantos años tienes?")
edad_actual = int(edad_actual)
anoActual = date.today().year
anoActual = int(anoActual)

edad_futura = edad_actual + (2050 - anoActual)

mensaje = f"Hola {nombre}, en el año 2050 tendras {edad_futura} anios"

print(mensaje)