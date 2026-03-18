# Pedimos el dato (python lo recibira como texto)
cuenta_texto = input("¿Cuanto costó la cena?")

# Lo transformamos a número decimal (float) para poder operar
cuenta_numero = float(cuenta_texto)

propina = cuenta_numero * 0.10
print(f"Deberías dejar ${propina} de propina")