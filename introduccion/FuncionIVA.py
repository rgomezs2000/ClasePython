def calcularIVA(precio):
    iva = precio * (1 + 16/100)
    return iva

precio = input("Precio total:\n")
precio = float(precio)

iva = calcularIVA(precio)

mensaje = f"El iva en base 16% de ${precio} es: ${iva}"
print(mensaje)