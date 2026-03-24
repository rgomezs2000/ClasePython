def calcularPrecioConIVA(precio):
    total = precio * 1.16
    return total

precio = input("Precio total:\n")
precio = float(precio)

total = calcularPrecioConIVA(precio)

mensaje = f"El iva en base 16% de ${precio} es: ${total}"
print(mensaje)