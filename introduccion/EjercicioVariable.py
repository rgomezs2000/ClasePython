nombre = "Roger"
saldo = 65000.00
tarjeta_valida = True

saludo = "Hola, " + nombre
print(saludo)

alerta = "Cuidado!\n" * 3
print(alerta)

mensaje = f"Cajero: Bienvenido {nombre}. Su saldo es de ${saldo}"
print(mensaje)

gasto = 500.50
nuevo_saldo = saldo - gasto
mensaje = f"{nombre}, tu nuevo saldo es: ${nuevo_saldo}"
print(mensaje)